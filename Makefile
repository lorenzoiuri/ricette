
all:
	@echo "specificare categoria e modalita'"
	@echo "make <course> MODE=<mode>"
	@echo "    <course>: primi | secondi | dolci | antipasti"
	@echo "    <mode>  : old | new"

primi secondi antipasti dolci:
	./src/convert.sh $@ $(MODE)
	./src/make_list.sh $@
	pdflatex --jobname=$@ compileme.tex
	rm -f *.log *.aux *.out

clean:
	echo -n "" > recipes.tex
	rm -f content/*/*.tex
	rm -f *.log *.aux *.out *.pdf
