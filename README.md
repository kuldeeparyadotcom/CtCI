It simply my answers to CtCI (Cracking the Coding Interviews book by Gayle Laakmann McDowell)


Docker container with Python 3 and juypter notebook
Build docker image
docker build -t kd/mypy:latest .
docker build -t kd/mypy:withtmux .

#Mount program directory and run disposable container in interactive mode
docker run --rm -it -v $(PWD):/data kd/mypy:latest /bin/bash
docker run --rm -it -v $(PWD):/data kd/mypy:withtmux /bin/bash
