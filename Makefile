# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = _build
COMPILEDIR    = docs
LOCALES       = es fr

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile html-all

# Build the English source plus every translated locale into the same
# build directory ($(BUILDDIR)/html/<lang>).
html-all: html
	@for lang in $(LOCALES); do \
		echo "Building locale: $$lang"; \
		$(SPHINXBUILD) -b html "locales/$$lang" "$(BUILDDIR)/html/$$lang" $(SPHINXOPTS) $(O); \
	done

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# remove build folders
clean:
	rm -rf $(COMPILEDIR)
	rm -rf $(BUILDDIR)
