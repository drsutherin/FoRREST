#include <stdlib.h>
#include <fcntl.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define _NUM_CHARS_ 43

pid_t pids[8];

void report(int n)
{
	char b[10];
	sprintf(b, "  %d%%\r", (int)((n  * 100)/_NUM_CHARS_));
	write(1, b, strlen(b));
}

void wrong()
{
	printf("[!] Wrong serial number..\n");
	exit(1);
}

void good()
{
	printf("[!] Registered x)\n");
	exit(0);
}

void launch(char *s, int *i, int a, int b, int c, int sig)
{
	int t = *i;

	if (t == _NUM_CHARS_)
	{
		kill(getppid(), sig);
	}
	else
	{
		*i = *i + 1;
		switch (s[t])
		{
			case 'a': write(a, i, sizeof(*i)); break;
			case 'b': write(b, i, sizeof(*i)); break;
			case 'c': write(c, i, sizeof(*i));
		}
	}
}

void retrieve(char *s, int *v)
{
	int len;
	unsigned int n;

	n = 0;
	len = strlen(s);
	while (len > 0)
	{
		n = (n + s[len-1]) * 37;
		len--;
	}

	v[1] = n % 17 + 1;
	v[2] = n % 16 + 1;
	v[0] = _NUM_CHARS_ - v[1] - v[2];
}

void flush()
{
	while (getchar() != '\n');
}

void lastalive()
{
	int i;

	for (i = 0; i < 8; i++) kill(pids[i], SIGKILL);
}

void hand(int sig)
{
	switch (sig)
	{
		case SIGUSR1: lastalive(); good(); break;
		case SIGUSR2: lastalive(); wrong();
	}
}

int main(int argc, char *argv[], char *env[])
{
	char name[51];
	char serial[51];
	int v[3], df[2];
	int i, a, b, c, count;
	
	printf("eSn-mIn's crackme #4\n--------------------\n\n");

	printf("[*] Input your user name: ");
	scanf("%50s", name);
	flush();

	printf("[*] Input serial number: ");
	scanf("%50s", serial);
	flush();

	retrieve(name, v);

	a = b = c = 0;
	for (i = 0; i < strlen(serial); i++)
	{
		switch (serial[i])
		{
			case 'a': a++; break;
			case 'b': b++; break;
			case 'c': c++; break;
			default: wrong();
		}
	}

	if (v[0] != a || v[1] != b || v[2] != c) wrong();

	printf("[*] Verifying serial number..\n");
	
	count = 0;

	pipe(df);
	pipe(df);
	pipe(df);
	fcntl(3, F_SETFL, O_NONBLOCK);
	fcntl(5, F_SETFL, O_NONBLOCK);
	fcntl(7, F_SETFL, O_NONBLOCK);

	if ((pids[0] = fork()) == 0)
	{
		for (;;)
		{
			while (read(3, &count, sizeof(count)) == -1 &&
			       read(5, &count, sizeof(count)) == -1);
			
			report(count);
			launch(serial, &count, 6, 6, 8, SIGUSR1);
		}
	}
	close(3); close(5); close(6); close(8);
	
	pipe(df);
	pipe(df);
	pipe(df);
	pipe(df);
	pipe(df);
	pipe(df);
	fcntl(3, F_SETFL, O_NONBLOCK);
	fcntl(6, F_SETFL, O_NONBLOCK);
	fcntl(9, F_SETFL, O_NONBLOCK);
	fcntl(11, F_SETFL, O_NONBLOCK);
	fcntl(13, F_SETFL, O_NONBLOCK);
	fcntl(15, F_SETFL, O_NONBLOCK);

	if ((pids[1] = fork()) == 0)
	{
		for (;;)
		{
			while (read(7, &count, sizeof(count)) == -1 &&
			       read(9, &count, sizeof(count)) == -1 &&
			       read(13, &count, sizeof(count)) == -1 &&
			       read(15, &count, sizeof(count)) == -1);

			report(count);
			launch(serial, &count, 8, 12, 5, SIGUSR1);
		}
	}
	close(5); close(7); close(8); close(9); close(12); close(13); close(15);
	
	pipe(df);
	pipe(df);
	pipe(df);
	fcntl(5, F_SETFL, O_NONBLOCK);
	fcntl(8, F_SETFL, O_NONBLOCK);
	fcntl(12, F_SETFL, O_NONBLOCK);

	if ((pids[2] = fork()) == 0)
	{
		for (;;)
		{
			while (read(6, &count, sizeof(count)) == -1 &&
			       read(8, &count, sizeof(count)) == -1);

			report(count);
			launch(serial, &count, 10, 7, 13, SIGUSR1);
		}
	}
	close(6); close(7); close(8); close(10); close(13);
	
	pipe(df);
	pipe(df);
	pipe(df);
	fcntl(6, F_SETFL, O_NONBLOCK);
	fcntl(8, F_SETFL, O_NONBLOCK);
	fcntl(13, F_SETFL, O_NONBLOCK);

	if ((pids[3] = fork()) == 0)
	{
		for (;;)
		{
			while (read(5, &count, sizeof(count)) == -1 &&
			       read(13, &count, sizeof(count)) == -1);

			report(count);
			launch(serial, &count, 10, 9, 7, SIGUSR1);
		}
	}
	close(5); close(7); close(9); close(10); close(13);
	
	pipe(df);
	fcntl(5, F_SETFL, O_NONBLOCK);

	if ((pids[4] = fork()) == 0)
	{
		for (;;)
		{
			while (read(8, &count, sizeof(count)) == -1 &&
			       read(11, &count, sizeof(count)) == -1);

			report(count);
			launch(serial, &count, 15, 14, 7, SIGUSR1);
		}
	}
	close(7); close(8); close(11); close(14); close(15);
	
	pipe(df);
	pipe(df);
	fcntl(7, F_SETFL, O_NONBLOCK);
	fcntl(9, F_SETFL, O_NONBLOCK);

	if ((pids[5] = fork()) == 0)
	{
		for (;;)
		{
			while (read(6, &count, sizeof(count)) == -1 &&
			       read(9, &count, sizeof(count)) == -1);

			report(count);
			launch(serial, &count, 8, 8, 16, SIGUSR1);
		}
	}
	close(6); close(8); close(9); close(16);
	
	pipe(df);
	fcntl(6, F_SETFL, O_NONBLOCK);

	if ((pids[6] = fork()) == 0)
	{
		for (;;)
		{
			while (read(7, &count, sizeof(count)) == -1);

			report(count);
			launch(serial, &count, 10, 10, 8, SIGUSR1);
		}
	}
	close(7); close(8); close(10);

	pipe(df);
	fcntl(7, F_SETFL, O_NONBLOCK);

	if ((pids[7] = fork()) == 0)
	{
		for (;;)
		{
			while (read(3, &count, sizeof(count)) == -1 &&
			       read(5, &count, sizeof(count)) == -1 &&
			       read(6, &count, sizeof(count)) == -1 &&
			       read(7, &count, sizeof(count)) == -1 &&
			       read(12, &count, sizeof(count)) == -1);
			
			report(count);
			launch(serial, &count, 8, 8, 8, SIGUSR2);
		}
	}
	close(3); close(5); close(6); close(7); close(8); close(12);

	signal(SIGUSR1, hand);
	signal(SIGUSR2, hand);
	
	write(4, &count, sizeof(count));
	close(4);
	for (;;);
}
