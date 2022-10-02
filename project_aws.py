#!/bin/python3

import boto3
from time import sleep

def deploy instance():
	ec2 = boto3.resource('ec2')
	instances = ec2.create_instances(
		ImageId=input("Enter ami ID: \n"),
		MinCount=1,
		MaxCount=int(input("How many instances?\n")),
		InstanceType=input("Which type instance?\n"),
		KeyName='idan_kp'
)

def descrbe instance():
	client = boto3.client('ec2')
	response = client.describe_instances()
	for i response['Reservations']:
		for i in r['Instances']:
			print("ID: " + i['InstanceId'] + "\nIpAddress: " + i['PrivateIpAddress'] + "\n----------------------\n")

def destroy instance():
	instances=input("Enter the ids of the instances that you want to destroy:")
	ids = [instances]
	ec2 = boto3.resource('ec2')

	ec2.instances.filter(InstanceIds = ids).terminate()

def stop instance():
	instances=input("Enter the ids of the instances that you want to stop:")
        ids = [instances]
        ec2 = boto3.resource('ec2')

        ec2.instances.filter(InstanceIds = ids).stop()


def start instance():
	instances=input("enter the ids of the instances that you want to start:")
        ids = [instances]
        ec2 = boto3.resource('ec2')

        ec2.instances.filter(InstanceIds = ids).start()

def menu():
	while(True):
		choice=input("Menu:\n1.Describe EC2\n2.Deploy EC2\n3.Destroy instance\n4.Stop instance\n5.Start instance\n")
		if (choice=="1"):
			print("Now we will show your instances:..\n")
			sleep(3)
			def describe instance()
		elif (choice=="2"):
			print("Now we will deploy instances:..\n")
			def deploy instance()
		elif (choice=="3"):
			print("Now we will destroy instances:..\n")
			def destroy instance()
		elif (choice=="4"):
			print("Now we will stop instances:..\n")
			def stop instance()
		elif (choice=="5"):
			print("Now we will start instances:..\n")
			def start instance()
		else:
			print("Enter 1-5 only!!!\n")
			continue
		exit=input("Do you want to exit? yes/no\n")
		if (exit=="yes"):
			print("Bye...\n")
			break



menu()
