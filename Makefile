
all:
	@echo "specificare categoria"
	@echo "make primi | secondi | antipasti | dolci"

primi secondi antipasti dolci:
	./src/convert.sh $@
	./src/make_list.sh $@
	pdflatex --jobname=$@ compileme.tex
	rm -f *.log *.aux *.out

clean:
	rm -f content/*/*.tex
	rm -f *.log *.aux *.out *.pdf