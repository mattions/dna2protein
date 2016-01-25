# Build the image: 

Ee call it dna2protein, so it easy to refer to:

	docker build -t dna2protein .
	
# Launch a container with our program (to test)

	docker run -it dna2protein bash
	
# Launch our scripts from the container:

	docker run dna2protein transcribe.py
	docker run dna2protein translate.py