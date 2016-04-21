FROM jupyter/systemuser

RUN apt-get update && \
        DEBIAN_FRONTEND=noninteractive apt-get install -q -y \
	texlive-latex-extra \
	texlive-generic-recommended \
	texlive-xetex

ADD resystemuser.sh /srv/singleuser/resystemuser.sh

RUN pip install --ignore-installed datascience==0.5.19
RUN pip install okpy==1.5.1
RUN pip install pypandoc

# For geospatial connector ; pfrontiera
RUN conda install --yes gdal==2.0.0 libgdal==2.0.0
RUN pip install geopy==1.11.0
RUN pip install pyproj==1.9.4
RUN pip install shapely==1.5.13

# For ecology connector ; cboettig
RUN conda install --yes numexpr==2.5

# For humanities connector ; troland
RUN conda install --yes nltk==3.2
# models
RUN python -m nltk.downloader -d /usr/local/share/nltk_data averaged_perceptron_tagger
RUN python -m nltk.downloader -d /usr/local/share/nltk_data maxent_ne_chunker
# corpora
RUN python -m nltk.downloader -d /usr/local/share/nltk_data cmudict
RUN python -m nltk.downloader -d /usr/local/share/nltk_data wordnet
RUN python -m nltk.downloader -d /usr/local/share/nltk_data words
#
RUN python -m nltk.downloader -d /usr/local/share/nltk_data punkt
# 20160331
RUN conda install --yes gensim==0.12.4

# For ecology connector ; cboettig
RUN conda install --yes psycopg2=2.6.1

# Disable Python 2 kernel
RUN mv /usr/local/share/jupyter/kernels/python2 /var/tmp/

# For plt.xkcd()
RUN cd /usr/share/fonts && \
	wget --quiet https://github.com/shreyankg/xkcd-desktop/raw/master/Humor-Sans.ttf
RUN fc-cache --system-only

# For geospatial connector ; pfrontiera
RUN conda install --yes pysal==1.11.1

# Hack to use xelatex instead of pdflatex
RUN sed -i -e '/ *latex_command =/s/pdflatex/xelatex/' /opt/conda/lib/python*/site-packages/nbconvert/exporters/pdf.py

CMD ["sh", "/srv/singleuser/resystemuser.sh"]
