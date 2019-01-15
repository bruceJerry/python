#include <sys/types.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <stdio.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>

int Socketpair(int family, int type, int protocol, int fd[2])
{
    int32_t server_fd = -1;
    int32_t client1_fd = -1;
    int32_t client2_fd = -1;
    struct sockaddr_in listen_addr;
    struct sockaddr_in connect_addr;
    unsigned int size;

    if (protocol || (family != AF_INET && family != AF_LOCAL))
    {
        fprintf(stderr, "EAFNOSUPPORT\n");
        return -1;
    }
    if (!fd)
    {
        fprintf(stderr, "EINVAL\n");
        return -1;
    }

    /*创建listener，监听本地地址，端口由内核分配*/
    server_fd = socket(AF_INET, type, 0);
    if (server_fd < 0)
        return -1;
    printf("server_fd = %d\n", server_fd);
    memset(&listen_addr, 0, sizeof(listen_addr));
    listen_addr.sin_family      = AF_INET;
    listen_addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK); //127.0.0.1
    listen_addr.sin_port        = 0;    /* kernel chooses port.    */
    if (bind(server_fd, (struct sockaddr *) &listen_addr, sizeof(listen_addr)) == -1)
        goto fail;
    if (listen(server_fd, 1) == -1)
        goto fail;

    /*client1_fd, 连接到listener, 作为Socketpair的一端*/
    client1_fd = socket(AF_INET, type, 0);
    if (client1_fd < 0)
        goto fail;
    /* We want to find out the port number to connect to.  */
    size = sizeof(connect_addr);
    getsockname(server_fd, (struct sockaddr *) &connect_addr, &size);
    printf("connnect_addr ip = [%08x]\n", connect_addr.sin_addr.s_addr);
    connect(client1_fd, (struct sockaddr *) &connect_addr, sizeof(connect_addr));

    size = sizeof(listen_addr);
    /*调用accept函数接受connector的连接，将返回的文件描述符作为Socketpair的另一端*/
    client2_fd = accept(server_fd, (struct sockaddr *) &listen_addr, &size);
    if (client2_fd < 0)
        goto fail;
    printf("listen_addr ip = [%08x]\n", listen_addr.sin_addr.s_addr);
    printf("client2_fd = %d\n", client2_fd);
    close(server_fd);

    /*至此，我们已经创建了两个连接在一起的文件描述符，
     *通过向其中任意一个发送数据，都会“转发”到另一个，即可以实现进程间的通信 */

    fd[0] = client1_fd;
    fd[1] = client2_fd;

    return 0;

fail:
    if (server_fd != -1)
        close(server_fd);
    if (client1_fd != -1)
        close(client1_fd);
    if (client2_fd != -1)
        close(client2_fd);

    return -1;
}

int main(void)
{
    int fds[2];
    int r = Socketpair(AF_INET, SOCK_STREAM, 0, fds);
    if(r < 0)
    {
        perror("scoketpair()");
        exit(1);
    }
    pid_t p = fork();
    if(p)
    {
        /*  Parent process: echo client */
        printf("main thread = [%d]\n", p);
        int val = 0;
        close( fds[1] );
        while ( 1 )
        {
            sleep(1);
            ++val;
            printf( "Sending data: %d\n", val );
            write( fds[0], &val, sizeof(val) );
            read( fds[0], &val, sizeof(val) );
            printf( "Data received: %d\n", val );
        }
    }
    else
    {
        printf("sub thread = [%d]\n",p);
        int val;
        close( fds[0] );
        while ( 1 )
        {
            read( fds[1], &val, sizeof(val) );
            ++val;
            write( fds[1], &val, sizeof(val) );
        }
    }
    return 0;
}
