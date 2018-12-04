import usb
import usb.util
import usb.core
import usb.control
import array
import socketserver
import struct
import binhex

""" 
#  struct test
struct Header
{
    unsigned short id;
    char[4] tag;
    unsigned int version;
    unsigned int count;
}
"""
ss = b"1212 1212121212"
for x in ss:
    print(x)
idx, tag, version, count = struct.unpack("!H4s2l", ss)
print(idx, tag, version, count)


my_array = array.array("B", [0, 1, 2, 3, 4, 4])
my_array.append(5)
print(my_array.count(4), my_array.itemsize, my_array.buffer_info(), my_array.typecode)  # 数组中元素的个数

dev = usb.core.find(idVendor=0x413c, idProduct=0x301a)
config = usb.control.get_configuration(dev)  # 获取配置数量
print("config num = {}".format(config))
# cfg = dev.get_active_configuration()
endpoint = dev[0][(0, 0)][0]
print(endpoint)

langs = usb.util.get_langids(dev)   # 获取描述符的语言列表
print(langs)

string = usb.util.get_string(dev, 2, 0x0409)   # 获取usb设备的string描述符
print(string)

if dev.is_kernel_driver_active(0) is True:
    dev.detach_kernel_driver(0)
    usb.util.claim_interface(dev, 0)
    print("-----------------------")

res = usb.control.get_interface(dev, 0)  # 获取接口，必须在usb.util.claim_interface后面
print("interface = %s" % res)

collected = 0
print(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
while collected < 500:
    try:
        data = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        collected += 1
        print(data.tolist())  # type(data) = array.array
    except usb.core.USBError as e:
        data = None
        if e.strerror == "Operation timed out":  # (110, 'Operation timed out')
            # print(e.errno)
            continue
    except usb.core.USBError as e:
        if e.strerror == "Entity not found":
            print("error exit")
            break
    except KeyboardInterrupt as e:
            print("user exit")
            break

usb.util.release_interface(dev, 0)
dev.attach_kernel_driver(0)
