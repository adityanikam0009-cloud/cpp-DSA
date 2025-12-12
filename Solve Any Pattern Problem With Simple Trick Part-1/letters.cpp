#include <iostream>
using namespace std;

int main(){
    char name = 'a';
    int i,j;
    
    for( i=1;i<=5;i++ ){
        for( j=1;j<=5;j++){
        cout<<char (name+(i-1))<<" "; 
    }
    cout<<endl;
}
}