FROM jupyter/systemuser

# Install terminado
RUN pip3.4 install terminado

RUN pip3.4 install datascience==0.4.0.post1
RUN pip3.4 install okpy==1.5.1

# Disable Python 2 kernel
RUN mv /usr/local/share/jupyter/kernels/python2 /var/tmp/
