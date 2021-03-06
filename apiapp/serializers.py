# SE ENCARGA DE HACER EL CRUD EN EL JSON

from app.models import *
from rest_framework import serializers

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    nombre_tipo = serializers.CharField(read_only=True, source="tipo.nombre")
    tipo = TipoProductoSerializer(read_only=True)
    


    class Meta:
        model = Producto
        fields = '__all__'