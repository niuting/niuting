#include <stdio.h>

void print(void);

void print(void)
{
	printf("******************************\n");
}

void main(void)
{
	print();

	printf("hello ");
	printf("world\n");

	print();
}
