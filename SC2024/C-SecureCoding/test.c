// 소스 : test.c
// 컴파일 -> test.exe [arg1]
// 컴파일&링킹 : C -> C -> ASM -> OBJ -> EXE

#include <stdio.h>

#define HELLO_STR   "Hello\n" // 매크로
#define SUM(x, y)   (x, y)    // 매크로 함수

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