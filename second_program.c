#include <stdio.h>

int main()
{
	int a;
	int b;
	int i;
	int x = 0;
	
	int prim[b];


	for(i = 0; i<100; i++)
	{
		int es = 1;

		if(i>2)
		{
		  a=2;

		  while(a < sizeof(prim) && es == 1)
		  {
		   int temp = i%prim[a];

		   if(temp == 0)
		   {
		    es = 0;
	 	   }

		   a++;
		  }
                }
		
		if(es)
		 {
		  prim[x]=i;
		  x++;
		 }		
	}

	for(i = 0; i<x; i++)
	{
		printf("%d \n", prim[i]);		
	}

	getchar();
	return 0;
}
