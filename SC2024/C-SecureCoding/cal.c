#include <stdio.h>

int main(){
    int i = 0;
    int j = (i++ + ++i + ++i);

    printf("%d, %d", i, j);  // 콤마 추가

    return 0;  // main 함수에서 반환값 명시
}
