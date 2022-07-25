class dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height

    def bark(self):
        print ("{} goes woof".format(self.name))
   
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!!!".format)
    



davids_dog=dog("Rex", 50)
davids_dog.jump()
davids_dog.bark()

sarahs_dog=dog("Teacup", 20)
sarahs_dog.jump()
sarahs_dog.bark()



