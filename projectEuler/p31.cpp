#include<iostream>
#include<list>
#include<iterator>
using namespace std;

std::list<int> currency = {1,2,5,10,20,50,100,200};
std::list<int> current = {0,0,5,1,0,0,0,0};

int pos(list <int> g,int n){
  int i=0;
  list <int> :: iterator it;
  for(it = g.begin();it!= g.end();it++){
    if(i==n){
      return *it;
    }
    it++;
  }
}

int sum(list <int> g){
  list <int> :: iterator it;
  int s = 0,i=0;;
  for(it = g.begin();it!= g.end();it++){
    s+=(*it) * pos(currency,i);
    i++;
  }
  return s;
}



int main(){
  cout<<sum(current);
}
