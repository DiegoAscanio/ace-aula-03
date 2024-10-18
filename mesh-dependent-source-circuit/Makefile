all: original_circuit step_1 step_2

create_latex_out_dir:
	mkdir -p latex.out

original_circuit: create_latex_out_dir
	python build_tex_circuit.py original-circuit.tex

step_1: create_latex_out_dir
	python build_tex_circuit.py circuit-step-1.tex

step_2: create_latex_out_dir
	python build_tex_circuit.py circuit-step-2.tex

clean:
	rm -rf latex.out
	rm *.png
