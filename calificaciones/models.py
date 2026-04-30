from django.db import models


class Calificacion(models.Model):
	nombre_estudiante = models.CharField(max_length=100)
	identificacion = models.CharField(max_length=20)
	asignatura = models.CharField(max_length=100)
	nota1 = models.FloatField()
	nota2 = models.FloatField()
	nota3 = models.FloatField()
	promedio = models.FloatField(blank=True, null=True)

	def calcular_promedio(self):
		return round((self.nota1 + self.nota2 + self.nota3) / 3, 2)

	def save(self, *args, **kwargs):
		self.promedio = self.calcular_promedio()
		super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.nombre_estudiante} - {self.asignatura}"

	class Meta:
		verbose_name = 'Calificación'
		verbose_name_plural = 'Calificaciones'
