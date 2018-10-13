#include <iostream>
#include <cstdint>

int global = 0;

int main()
{
    int* heap = (int*) malloc(sizeof(int));
    
    std::cout << std::hex << (uint64_t) main << '\n';
    std::cout << std::hex << (uint64_t) &global << '\n';
    std::cout << std::hex << (uint64_t) heap << '\n';
    std::cout << std::hex << (uint64_t) &heap << '\n';
    
    char c;
    std::cin >> c;
    return 0;
}
