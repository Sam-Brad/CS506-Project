# ========================
# Variables
# ========================
NOTEBOOK=code.ipynb

# ========================
# Run the notebook
# ========================
install:
	pip install -r requirements.txt
run:
	mkdir -p output
	jupyter nbconvert --to notebook --execute $(NOTEBOOK) \
	--output executed.ipynb \
	--output-dir output

# ========================
# Clean outputs
# ========================
clean:
	rm -f executed.ipynb