from django.db import models

status = (('Em andamento',u'Em andamento'), ('Concluído',u'Concluído'), ('Não Finalizado',u'Não Finalizado'))

class Aluno(models.Model):
    nomeAluno = models.CharField(max_length=100)

class Professor(models.Model):
    nomeProfessor = models.CharField(max_length=100)

class Projeto(models.Model):
    nomeProjeto = models.CharField(max_length=100)
    anoProjeto = models.DateField()
    infoProjeto = models.TextField()
    atvEnvolvidas = models.CharField(max_length=100)
    statusProjeto = models.CharField(max_length=100, choices=status)
    id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

class Grupo(models.Model):
    nomeGrupo = models.CharField(max_length=100)
    anoGrupo = models.DateField()
    infoGrupo = models.TextField()
    atvEnvolvidas = models.CharField(max_length=100)
    statusGrupo = models.CharField(max_length=20, choices=status)
    id_professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

class AlunoProjeto(models.Model):
    id_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    tipoAluno = models.CharField(max_length=20)


