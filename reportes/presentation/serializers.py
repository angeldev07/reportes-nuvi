from rest_framework import serializers

# Serializador para la clase CondominioHouse
class CondominioHouseSerializer(serializers.Serializer):
    id = serializers.CharField()
    nombre_cliente = serializers.CharField()
    propiedad = serializers.CharField()

# Serializador para la clase BillPayInfo
class BillPayInfoSerializer(serializers.Serializer):
    total = serializers.FloatField()
    fecha = serializers.DateTimeField()

# Serializador para la clase BillConcepts
class BillConceptsSerializer(serializers.Serializer):
    descripcion = serializers.CharField()
    valorTotal = serializers.FloatField()

# Serializador para la clase Bill
class BillSerializer(serializers.Serializer):
    periodo = serializers.CharField()
    prontoPago = BillPayInfoSerializer()
    despuesPago = BillPayInfoSerializer()
    conceptos = BillConceptsSerializer(many=True)
    propietario = CondominioHouseSerializer()