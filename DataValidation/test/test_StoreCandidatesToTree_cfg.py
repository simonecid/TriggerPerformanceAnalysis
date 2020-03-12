import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils # ADDED
process = cms.Process("MATCH")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource",
  # fileNames = cms.untracked.vstring("file:/hdfs/user/sb17498/CMS_Phase_2/jetMETStudies/ComputePhase1AndAK4L1TJetsFromPfCandidates_10_0_4_MTD/ComputeUncalibratedPhase1AndAK4L1TJetsFromPfCandidates_10_0_4_MTD_7x7Jets.root"),
  # fileNames = cms.untracked.vstring("file:myOutputFile.root"),
  fileNames = cms.untracked.vstring("file:/hdfs/user/sb17498/CMS_Phase_2/jetMETStudies/TTBar_200_10_4_0_MTD/inputs104X_1.root"),
)

process.TFileService = cms.Service('TFileService', fileName = cms.string("pfdump.root"))

process.out = cms.OutputModule("PoolOutputModule",
  fileName = cms.untracked.string('test.root'),
  outputCommands = cms.untracked.vstring(
    "drop *",
    "keep *_ak4GenJetsNoNu_*_*",
    "keep *_Phase1L1TJetCalibrator_*_*",
    "keep *_AK4L1TJetCalibrator_*_*",
    "keep *_ntuplizer_*_*",
  ),
)

process.ntuplizer = cms.EDAnalyzer(
    "StoreCandidatesToTree", 
    candidateCollectionTag = cms.InputTag("l1pfCandidates", "Puppi", "IN"),
    treeName = cms.string("PuppiCandidates"),
    maxNumberOfCandidates = cms.uint32(3456) # 24 * 144 regions
 )

process.p = cms.Path(process.ntuplizer)

process.e = cms.EndPath(process.out)