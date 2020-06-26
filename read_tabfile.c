#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LINE_LENGTH 1000

int main(int argc, char *argv[]) {
	char line[LINE_LENGTH];

	if (argc < 3) {
		fprintf(stderr, "USAGE: read_tabfile filename numcols");
		exit(1);
	}
	FILE *tabfile = fopen(argv[1], "r");
	FILE *res = fopen("result.csv", "w");

	if (tabfile == NULL || res == NULL) {
		fprintf(stderr, "File could not be opened or does not exist");
		exit(1);
	}
	while (fgets(line, sizeof(line), tabfile) != NULL) {
		char *token = strtok(line, "\t");
		int numcols = atoi(argv[2]);
		int curr_cols = 0;
		while (token != NULL) {
			if (numcols == curr_cols) {
				fprintf(res, "\n");
				curr_cols = 0;
			}
			fprintf(res, "%s,", token);
			token = strtok(NULL, "\t");
			curr_cols++;
		}
	}
	int c1 = fclose(tabfile);
	int c2 = fclose(res);
	if (c1 != 0 || c2 != 0) {
		fprintf(stderr, "Error closing files");
	}
	return 0;

}
