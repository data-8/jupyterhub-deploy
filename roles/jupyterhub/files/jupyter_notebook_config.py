#------------------------------------------------------------------------------
# NotebookNotary(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## The sqlite file in which to store notebook signatures. By default, this will
#  be in your Jupyter runtime directory. You can set it to ':memory:' to disable
#  sqlite writing to the filesystem.
c.NotebookNotary.db_file = ':memory:'

