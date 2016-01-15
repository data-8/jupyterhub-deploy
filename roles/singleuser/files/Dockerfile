FROM jupyter/systemuser

# This isn't done by conda? Otherwise the container will fail to start with
# "/usr/bin/env: python3: No such file or directory" since
# /srv/singleuser/systemuser.sh (/bin/sh) launches jupyterhub-singleuser
# which is /usr/bin/env python3.
RUN echo 'export PATH=/opt/conda/bin:${PATH}' >> /root/.bashrc
ENV PATH /opt/conda/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUN sed -i \
	-e 's@jupyterhub-singleuser@/opt/conda/bin/python3 /usr/local/bin/jupyterhub-singleuser@' \
	/srv/singleuser/systemuser.sh

RUN sed -i \
	-e '/^backend/s/Qt4Agg/svg/' \
	/opt/conda/lib/python3.4/site-packages/matplotlib/mpl-data/matplotlibrc

RUN pip install datascience==0.3.dev22

RUN mkdir /root/.jupyter
RUN pip install notebook-ok-extension

RUN pip install okpy

# Disable Python 2 kernel
RUN mv /usr/local/share/jupyter/kernels/python2 /var/tmp/

# Download ok.css and ok.js and install into an ok extension directory.
# This is utilized by files created through /etc/skel/.
ADD https://raw.githubusercontent.com/data-8/notebook-ok-extension/master/ok/ok.css https://raw.githubusercontent.com/data-8/notebook-ok-extension/master/ok/ok.js /usr/local/share/jupyter/nbextensions/ok/

# ADD uses 0600 by default
RUN chmod 0644 /usr/local/share/jupyter/nbextensions/ok/ok.css /usr/local/share/jupyter/nbextensions/ok/ok.js
