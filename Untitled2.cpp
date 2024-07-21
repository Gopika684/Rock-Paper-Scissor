#include<stdio.h>
int main()
{
	int n,r,placevalue=10000;
	printf("Enter any number");
	scanf("%d",&n);
	r=(n/placevalue)%10;
	
	 
	printf("%d",r);
	return 0;
}
