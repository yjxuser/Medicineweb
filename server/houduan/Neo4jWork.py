import py2neo
from py2neo import Graph, Node, Relationship, Subgraph


def get_nodes(list_2D):
    # 传入的为2D的list，包括N个三元组
    N = len(list_2D)
    names = []
    for triple in list_2D:
        names.append(triple[0])
        names.append(triple[2])
    names = list(set(names))
    return names


def create_graph(list_2D, node_type='database'):
    # 与neo4j数据库建立联系
    # try:
    graph = Graph('bolt://localhost:7687', auth=('neo4j', 'password'))
    # graph.delete_all()
    # except:
    #     return [{'status': 'Neo4jConnectFail', 'details': 'Failed to Connect Neo4j'}]
    #


    nl = []
    relation_ls = []
    try:
        nodes = get_nodes(list_2D)
        for name in nodes:
            node = Node(node_type, name, name=name)
            nl.append(node)
        subnodes = Subgraph(nl)
        graph.create(subnodes)

        for triple in list_2D:
            x = graph.nodes.match(node_type, triple[0]).first()
            y = graph.nodes.match(node_type, triple[2]).first()

            relation = Relationship(x, triple[1], y)
            print(relation)
            relation_ls.append(relation)

        # 结点和关系汇总
        subgraph = Subgraph(relationships=relation_ls)
        # 创建知识图谱
        graph.create(subgraph)
    except:
        return [{'status': 'CreateGraphFail', 'details': 'Fail to Create Graph'}]

    return [{'status': 'SuccessCreateGraph', 'details': 'Everything is OK'}]



