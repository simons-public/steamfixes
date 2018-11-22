#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dlfcn.h>

#define LOADER "/usr/bin/steamfixes"

typedef ssize_t (*execve_func_t)(const char* filename, char* const argv[], char* const envp[]);
static execve_func_t sys_execve = NULL;

int execve(const char* filename, char* const argv[], char* const envp[]) {

    char* appid;
    appid = secure_getenv("SteamAppId");

    /* checking for LOADER in the filename prevents infinite looping */
    if (appid != NULL && strcmp(filename, LOADER) != 0)
    {
        #ifdef DEBUG
        printf("Hooked SteamAppId: %s\n", appid);
        printf("Running %s with %s\n", filename, LOADER);
        #endif

        char new_fn[] = LOADER; 
        char *new_argv[20];

        new_argv[0] = LOADER;

        int i = 1;
        while(*argv != NULL)
        {
            new_argv[i] = *argv;
            argv++;
            i++;
        }

        sys_execve = dlsym(RTLD_NEXT, "execve");
        return sys_execve(new_fn, new_argv, envp);
    } else {
        /* return origininal execve */
        sys_execve = dlsym(RTLD_NEXT, "execve");
        return sys_execve(filename, argv, envp);
    }
}
