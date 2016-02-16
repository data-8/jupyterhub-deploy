FROM jupyter/systemuser

RUN apt-get update && \
        DEBIAN_FRONTEND=noninteractive apt-get install -q -y \
	texlive-latex-extra \
	texlive-generic-recommended

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

RUN pip install --ignore-installed datascience==0.5.6
RUN pip install okpy==1.5.1
RUN pip install pypandoc

RUN conda install --yes gdal==2.0.0 libgdal==2.0.0
RUN pip install geopy==1.11.0

# Disable Python 2 kernel
RUN mv /usr/local/share/jupyter/kernels/python2 /var/tmp/
