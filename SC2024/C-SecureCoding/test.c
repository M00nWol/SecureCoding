// 소스 : test.c
// 컴파일 -> test.exe [arg1]


#include <stdio.h>

#define HELLO_STR "Hello"

int sum(int i, int j){
    return (i + j);
}

int main(int argc, int *argv, char *env){
// argc = 인자값 몇 개이니
// argv = 인자값 배열
// env = 환경변수
    printf("Hello\n");

    return sum(1, 2);
}