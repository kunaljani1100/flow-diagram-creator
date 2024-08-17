import glob
import os

import pandas as pd


def createDependencyDiagram(moduleToSystemCallGraph):
    """
    This function is used to create a dependency diagram based on the call graph.
    :param moduleToSystemCallGraph: A python dictionary containing the module name and the systems called by the module.
    :return: The graph representation in a visual format.
    """

    dependencyDiagram = ''
    for module in moduleToSystemCallGraph.keys():
        dependencyDiagram += module + '\n'
        for system in moduleToSystemCallGraph[module]:
            dependencyDiagram += '|\n|\n'
            dependencyDiagram += '------------------>' + system + '\n'
        dependencyDiagram += '\n'
    return dependencyDiagram


def createModuleToSystemCallGraph(moduleDependenciesDataset):
    """
    This function is used to generate a call graph python dictionary based on the column names that are present.
    :param moduleDependenciesDataset: The data frame object that is read from a CSV file.
    :return: The python dictionary that contains the call graph.
    """

    moduleToSystemCallGraph = {}

    modules = moduleDependenciesDataset['Module']
    systems = moduleDependenciesDataset['System']

    for i in range(len(modules)):
        if modules[i] not in moduleToSystemCallGraph:
            moduleToSystemCallGraph[modules[i]] = set()
        moduleToSystemCallGraph[modules[i]].add(systems[i])

    return moduleToSystemCallGraph


def createDependencyGraphOutputFiles(csvFiles):
    """
    This function is used to generate output files based on the CSV files that are read from the project directory.
    :param csvFiles: The CSV files that are present in the project directory.
    :return: The list of all the test files that contain the dependency graphs in a visual format.
    """
    for csvFile in csvFiles:
        moduleDependenciesDataset = pd.read_csv(csvFile)

        moduleToSystemCallGraph = createModuleToSystemCallGraph(moduleDependenciesDataset)
        dependencyDiagram = createDependencyDiagram(moduleToSystemCallGraph)

        file = open('dependency-graph-' + csvFile + '.txt', 'w')
        file.write(dependencyDiagram)
        file.close()


os.chdir("/Users/kunaljani/PycharmProjects/flow-diagram-creator")
csvFiles = glob.glob("*.csv")
createDependencyGraphOutputFiles(csvFiles)
