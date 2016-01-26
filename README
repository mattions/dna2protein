# Build the image: 

We create an image, called `dna2protein`, and build it using the `Dockerfile`:

	docker build -t dna2protein .
	
# We can launch a container, and see if we have everything we need.

	docker run -it dna2protein bash
	
# Launch our scripts from the container:

	docker run dna2protein transcribe.py
	docker run dna2protein translate.py
	
Now our scripts are dockerized and we can use it directly from the image.