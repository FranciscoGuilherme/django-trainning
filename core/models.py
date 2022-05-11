from django.db import models

class Atom(models.Model):
    term = models.CharField('Term', max_length = 255)
    createdAt = models.DateTimeField("Created At", auto_now_add = True)
    deletedAt = models.DateTimeField("Deleted at", blank = True, null = True)
    
    def __str__(self):
        return self.term

class Axiom(models.Model):
    valid = models.BooleanField(default = True)
    sentence = models.CharField('Sentence', max_length = 255)
    createdAt = models.DateTimeField("Created At", auto_now_add = True)
    deletedAt = models.DateTimeField("Deleted at", blank = True, null = True)

    def __str__(self):
        return self.sentence

class Action(models.Model):
    description = models.CharField('Description', max_length = 255)
    atom_id = models.ForeignKey(Atom, on_delete = models.CASCADE)
    axiom_id = models.ForeignKey(Axiom, on_delete = models.CASCADE)
    createdAt = models.DateTimeField("Created At", auto_now_add = True)
    deletedAt = models.DateTimeField("Deleted at", blank = True, null = True)

    def __str__(self):
        return self.description

class Knowledge(models.Model):
    valid = models.BooleanField(default = True)
    sentence = models.CharField('Sentence', max_length = 255)
    createdAt = models.DateTimeField("Created At", auto_now_add = True)
    deletedAt = models.DateTimeField("Deleted at", blank = True, null = True)

    def __str__(self):
        return self.sentence

class Context(models.Model):
    description = models.CharField('Description', max_length = 255)
    action_id = models.ForeignKey(Action, on_delete = models.CASCADE)
    knowledge_id = models.ForeignKey(Knowledge, on_delete = models.CASCADE)
    createdAt = models.DateTimeField("Created At", auto_now_add = True)
    deletedAt = models.DateTimeField("Deleted at", blank = True, null = True)

    def __str__(self):
        return self.description
