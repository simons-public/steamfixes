all: loader.so

loader.so:
	gcc -std=c99 -DDEBUG -g -o loader.so --shared loader.c -Wall

install: loader.so steamfixes
	@echo 'installing loader.so to /usr/lib/steamfixes/loader.so'
	install -Dm644 loader.so /usr/lib/steamfixes/loader.so
	@echo 'installing steamfixes to /usr/bin/steamfixes'
	install -Dm755 steamfixes /usr/bin/steamfixes

clean:
	rm loader.so
