from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from gqlapp.models import ProductModel
import graphene

class Products(DjangoObjectType):
	class Meta:
		model=ProductModel
		filter_fields=['id', 'Subsistema','Datetime']
		interfaces = (relay.Node, )

class Query(graphene.ObjectType):
	prodinfo=relay.Node.Field(Products)
	DadosDiarios = DjangoFilterConnectionField(Products)

	def resolve_prod(self, info):
		return ProductModel.objects.all()

schema = graphene.Schema(query=Query)