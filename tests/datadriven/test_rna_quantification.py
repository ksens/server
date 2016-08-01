"""
Data-driven tests for rna quantification.
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ga4gh.datarepo as datarepo
import ga4gh.datamodel as datamodel
import ga4gh.datamodel.datasets as datasets
import ga4gh.datamodel.references as references
import ga4gh.datamodel.rna_quantification as rna_quantification
import ga4gh.protocol as protocol
import tests.datadriven as datadriven
import tests.paths as paths


_datasetName = "ds"


_rnaQuantSetTestData = {
    "name": "ENCFF305LZB"
}


_rnaQuantTestData = {
    "feature_set_ids": ["Gencodev16"],
    "description": "RNAseq data from ENCODE evaluation",
    "name": "ENCFF305LZB",
    "read_group_ids": ["test_reads"]
}


_expressionTestData = {
    "bad_id": "MWtnLXAzLXN1YnNldDpybmFfZXhhbXBsZV8yOm1tOV9leGFtcGxlXzI=",
    "name": "ENSG00000076984.13",
    "rna_quantification_id": "",
    "expression": 24.52,
    "feature_id": "ENSG00000076984.13",
    "is_normalized": True,
    "raw_read_count": 4317.0,
    "score": 24.35,
    "units": 2,
    "conf_interval_low": 24.1,
    "conf_interval_hi": 24.6,
    "num_expression_entries": 2,
    "num_entries_over_threshold": 1
}


def _buildCompoundId(splits):
    """
    Returns a compoundId built from an ordered list of localIds.
    """
    joined = datamodel.CompoundId.join(splits)
    obfuscated = datamodel.CompoundId.obfuscate(joined)
    return obfuscated


def _getRnaQuantCompoundId(dataSetName, quantSetName, rnaQuant):
    splits = [dataSetName, quantSetName, rnaQuant]
    return _buildCompoundId(splits)


def _getExpressionCompoundId(
        dataSetName, quantSetName, rnaQuant, expressionId):
    splits = [dataSetName, quantSetName, rnaQuant, expressionId]
    return _buildCompoundId(splits)


def testRnaQuantification():
    testDataDir = "tests/data/datasets/dataset1/rnaQuant"
    for test in datadriven.makeTests(
            testDataDir, RnaQuantificationTest, '*.db'):
        yield test


class RnaQuantificationTest(datadriven.DataDrivenTest):
    """
    Data driven test class for rna quantification. Builds an alternative model
    of a rna quantification, and verifies that it is consistent with the model
    built by the rna_quantification.RNASeqResult object.
    """
    def __init__(self, rnaQuantificationLocalId, baseDir):
        self._dataset = datasets.Dataset(_datasetName)
        self._repo = datarepo.SqlDataRepository(paths.testDataRepo)
        self._repo.open(datarepo.MODE_READ)
        self._referenceSet = references.AbstractReferenceSet("test_rs")
        rnaQuantificationId = rnaQuantificationLocalId[:-3]  # remove '.db'
        super(RnaQuantificationTest, self).__init__(
            rnaQuantificationId, baseDir)

    def getDataModelInstance(self, localId, dataPath):
        rnaQuantSet = rna_quantification.RnaQuantificationSet(
            self._dataset, localId)
        rnaQuantSet.setReferenceSet(self._referenceSet)
        rnaQuantSet.populateFromFile(dataPath)
        return rnaQuantSet

    def getProtocolClass(self):
        return protocol.RnaQuantificationSet

    def testRnaQuantificationObject(self):
        rnaQuant = self._gaObject.getRnaQuantificationByIndex(0)
        gaRnaQuant = rnaQuant.toProtocolElement()
        idString = _buildCompoundId([
            _datasetName,
            _rnaQuantSetTestData["name"],
            _rnaQuantTestData["name"]])
        compoundId = datamodel.RnaQuantificationCompoundId.parse(idString)
        self.assertEqual(gaRnaQuant.id, str(compoundId))
        self.assertEqual(
            gaRnaQuant.feature_set_ids, _rnaQuantTestData["feature_set_ids"])
        self.assertEqual(
            gaRnaQuant.description, _rnaQuantTestData["description"])
        self.assertEqual(gaRnaQuant.name, _rnaQuantTestData["name"])

    def testGetExpressionLevelById(self):
        rnaQuantification = self._gaObject.getRnaQuantificationByIndex(0)
        idString = _buildCompoundId([
            _datasetName,
            _rnaQuantSetTestData["name"],
            _rnaQuantTestData["name"],
            _expressionTestData["name"]])
        compoundId = datamodel.ExpressionLevelCompoundId.parse(idString)
        gaExpression = rnaQuantification.getExpressionLevel(compoundId)
        self.assertExpressionEqual(gaExpression, _expressionTestData)

    def assertExpressionEqual(self, gaExpressionObj, testData):
        gaExpression = gaExpressionObj.toProtocolElement()
        idString = _buildCompoundId([
            _datasetName,
            _rnaQuantSetTestData["name"],
            _rnaQuantTestData["name"],
            _expressionTestData["name"]])
        compoundId = datamodel.ExpressionLevelCompoundId.parse(idString)
        self.assertEqual(gaExpression.id, str(compoundId))
        self.assertEqual(gaExpression.name, testData["name"])
        self.assertEqual(gaExpression.feature_id, testData["feature_id"])
        self.assertEqual(
            gaExpression.rna_quantification_id,
            str(gaExpressionObj.getParentContainer().getCompoundId()))
        self.assertEqual(
            gaExpression.expression, testData["expression"])
        self.assertEqual(
            gaExpression.is_normalized, testData["is_normalized"])
        self.assertEqual(
            gaExpression.raw_read_count, testData["raw_read_count"])
        self.assertEqual(gaExpression.score, testData["score"])
        self.assertEqual(gaExpression.units, testData["units"])
        self.assertEqual(
            gaExpression.conf_interval_low, testData["conf_interval_low"])
        self.assertEqual(
            gaExpression.conf_interval_high, testData["conf_interval_hi"])

    def testSearchExpressionLevels(self):
        rnaQuantification = self._gaObject.getRnaQuantificationByIndex(0)
        rnaQuantID = rnaQuantification.getLocalId()
        expressionLevels = rnaQuantification.getExpressionLevels(rnaQuantID)
        self.assertEqual(
            _expressionTestData["num_expression_entries"],
            len(expressionLevels))
        overThreshold = rnaQuantification.getExpressionLevels(
            rnaQuantID, threshold=100.0)
        self.assertEqual(
            _expressionTestData["num_entries_over_threshold"],
            len(overThreshold))
