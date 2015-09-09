FROM jupyter/systemuser

# Install nbgrader
RUN pip3.4 install git+git://github.com/jhamrick/nbgrader.git@compmodels

# Install terminado
RUN pip2.7 install terminado
RUN pip3.4 install terminado

# Install datascience
RUN pip2.7 install datascience==0.3.4
RUN pip3.4 install datascience==0.3.4

RUN pip2.7 install notebook-ok-extension
RUN pip3.4 install notebook-ok-extension

RUN pip2.7 install okpy
RUN pip3.4 install okpy

# Disable Python 2 kernel
RUN mv /usr/local/share/jupyter/kernels/python2 /var/tmp/

# Download ok.css and ok.js and install into an ok extension directory.
# This is utilized by files created through /etc/skel/.
ADD https://raw.githubusercontent.com/dsten/notebook-ok-extension/master/ok/ok.css https://raw.githubusercontent.com/dsten/notebook-ok-extension/master/ok/ok.js /usr/local/share/jupyter/nbextensions/ok/

# ADD uses 0600 by default
RUN chmod 0644 /usr/local/share/jupyter/nbextensions/ok/ok.css /usr/local/share/jupyter/nbextensions/ok/ok.js
