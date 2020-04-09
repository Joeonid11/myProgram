//joeonid11_
#include <stdio.h>
#include <string.h>
int main(){
    char user[100];
    int k;
    printf("Enter Name : ");
    fgets(user,100,stdin);
    for(k=0;k<strlen(user);k++){
        if(user[k]=='a'||user[k]=='u'||user[k]=='e'||user[k]=='o'){
            user[k]='i';
        }
    }
    puts(user);

    return 0;
}