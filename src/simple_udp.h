#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>

#include <cstring>
#include <string>

class simple_udp {
private:
    int sock;
    struct sockaddr_in addr;
    const int BUFFER_MAX = 400;

public:
    simple_udp(std::string address, int port) : sock(0), addr{} {
        sock = socket(AF_INET, SOCK_DGRAM, 0);
        addr.sin_family = AF_INET;
        addr.sin_addr.s_addr = inet_addr(address.c_str());
        addr.sin_port = htons(port);
    }
    void udp_send(std::string word) {
        sendto(sock, word.c_str(), word.length(), 0,
               reinterpret_cast<struct sockaddr *>(&addr), sizeof(addr));
    }

    void udp_bind() {
        bind(sock, reinterpret_cast<struct sockaddr *>(&addr), sizeof(addr));
    }
    std::string udp_recv() {
        char buf[BUFFER_MAX];
        memset(buf, 0, sizeof(buf));
        recv(sock, buf, sizeof(buf), 0);
        return std::string(buf);
    }
    void udp_recv(char *buf, int size) const {
        memset(buf, 0, size);
        recv(sock, buf, size, 0);
    }

    ~simple_udp() { close(sock); }
};
