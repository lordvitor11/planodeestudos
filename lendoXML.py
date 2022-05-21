from xml.dom import minidom

doc = minidom.parse("important/ifba.sea.2022v1_subgroups.xml")

turmas = doc.getElementsByTagName("Subgroup")
 # for turma in turmas:
#     name = turma.getAttribute("name")
#     print(name)
#     for i in range(6):
#         print(turma.getElementsByTagName("Day")[i].getAttribute("name"))

#exemplo de pegar cada um dos dados do xml da turma
print(turmas[0].getAttribute("name"))
print(turmas[0].getElementsByTagName("Day")[0].getAttribute("name"))
print(turmas[0].getElementsByTagName("Hour")[0].getAttribute("name"))
print(turmas[0].getElementsByTagName("Teacher")[0].getAttribute("name"))
print(turmas[0].getElementsByTagName("Subject")[0].getAttribute("name"))
print(turmas[0].getElementsByTagName("Activity_Tag")[0].getAttribute("name"))
