#include <thread>
#include <stdio.h>
using namespace std;

unsigned long long tebak1 = 55620114;
unsigned long long tebak2 = 65288691;
thread_local unsigned long long state = 0;
const unsigned long long MAX = 4295032832;

void setup(unsigned long long seed)
{
	state = 0;
	unsigned long long cur = 0LL;
	for (int i = 0; i < 16; i++)
	{
		cur = seed & 3LL;
		seed >>= 2;
		state = (state << 4) | ((state & 3LL) ^ cur);
		state |= cur << 2;
	}
}

unsigned long long next(int bits)
{
	unsigned long long ret = 0LL;
	for (int i = 0; i < bits; i++)
	{
		ret <<= 1;
		ret |= state & 1LL;
		state = (state << 1) ^ (state >> 61);
		state &= 0xFFFFFFFFFFFFFFFFLL;
		state ^= 0xFFFFFFFFFFFFFFFFLL;

		unsigned long long cur;

		for (int j = 0; j < 64; j += 4)
		{
			cur = (state >> j) & 0xFLL;
			cur = (cur >> 3) | ((cur >> 2) & 2LL) | ((cur << 3) & 8LL) | ((cur << 2) & 4LL);
			state ^= cur << j;
		}
	}
	return ret;
}

void run(unsigned long long start, unsigned long long end)
{
	unsigned long long seed = start;

	while (seed <= end)
	{
		setup(seed);

		if (next(26) == tebak1)
		{
			printf("Cek 1, seed: %lld\n", seed);
			if (next(26) == tebak2)
			{
				printf("Finished, hasil: %lld\n", next(26));
				exit(1);
			}
		}
		seed++;
	}
}

int main()
{
	thread th1(run, 0, 1073758208);
	thread th2(run, 1073758209, 2147516416);
	thread th3(run, 2147516417, 3221274624);
	thread th4(run, 3221274625, 4295032832);
	th1.join();
	th2.join();
	th3.join();
	th4.join();
}