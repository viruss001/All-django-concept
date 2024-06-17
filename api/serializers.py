from rest_framework import serializers

from .models import *  # import model

# now we have create another serialzer for userid


class useridserlizer(serializers.ModelSerializer):
    class Meta:
        model = Userid
        fields = ["uid"]
        userid = useridserlizer()


class usernameserlizer(serializers.ModelSerializer):
    class Meta:
        # now we have to pass model name and feild which want to serializ

        model = username
        fields = "__all__"
        # we use depth when we have fore reletionship
        # depth = 1
        # field=['fname','age']selective filedsare serialized
        # exclude = [pass feilds which we dont wont to serailze]

    def validate(self, data):
        if data["age"] < 18:
            raise serializers.ValidationError("age must be grater then 18")
        return data

    """def validate_age(self, age):
        pass
    for validation on single things"""

    def create(self, validated_data):
        author_data = validated_data.pop("userid")
        userid, created = Userid.objects.get_or_create(**author_data)
        book = username.objects.create(userid=userid, **validated_data)
        return book

    """we create this method we created nested serializer
    basiclay this function issetvalue of userid"""


from django.contrib.auth.models import User


class Registerus(serializers.Serializer):
    username = serializers.CharField()

    password = serializers.CharField()

    def validate(self, data):
        if data["username"]:
            if User.objects.filter(name=data["username"]).exists():
                raise serializers.ValidationError("user already taken")
        return data

    # now again we have to create the method to set value in user models
    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        return validated_data
