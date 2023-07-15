contents = ["All carrots are to be sliced longitudionally",
            "The carrots were repotedly sliced",
            "The slicing process was well presented"]
filenames = ["doc.text", "report.txt" , "presentation.txt"]


for content , filename in zip(contents, filenames):
    file = open(f"file/{filenames}" , 'w')
    file.write(content)