"""
Functions which are not listed in the maya documentation, such as commands created by plugins,
as well as the name parsing classes `DependNodeName`, `DagNodeName`, and `AttributeName`.
"""

from pymel.internal.pmcmds import xgmCache
from pymel.internal.pmcmds import sbs_GetGlobalTextureWidth
from pymel.internal.pmcmds import notifyPostRedo
from pymel.internal.pmcmds import FBXImportShowUI
from pymel.internal.pmcmds import GetHIKMatrixDecomposition
from pymel.internal.pmcmds import xgmSplineGeometryConvert
from pymel.internal.pmcmds import FBXProperties
from pymel.internal.pmcmds import xgmBifrostBrushToolCmd
from pymel.internal.pmcmds import FBXExportHardEdges
from pymel.internal.pmcmds import ptexBake
from pymel.internal.pmcmds import xgmCopyDescription
from pymel.internal.pmcmds import xgmSetArchiveSize
from pymel.internal.pmcmds import sbs_GetAllInputsFromSubstanceNode
from pymel.internal.pmcmds import xgmPointRender
from pymel.internal.pmcmds import symmetrizeUV
from pymel.internal.pmcmds import pushPinning
from pymel.internal.pmcmds import arnoldRenderView
from pymel.internal.pmcmds import xgmSplineBaseDensityScaleChangeCmd
from pymel.internal.pmcmds import xgmFileRender
from pymel.internal.pmcmds import OneClickAcknowledge
from pymel.internal.pmcmds import dR_testCmd
from pymel.internal.pmcmds import FBXExportCameras
from pymel.internal.pmcmds import sbs_GetChannelsNamesFromSubstanceNode
from pymel.internal.pmcmds import dgdebug
from pymel.internal.pmcmds import timeSliderCustomDraw
from pymel.internal.pmcmds import polyWarpImage
from pymel.internal.pmcmds import FBXUIShowOptions
from pymel.internal.pmcmds import xgmSculptLayerInit
from pymel.internal.pmcmds import FBXImportAxisConversionEnable
from pymel.internal.pmcmds import bifSaveFrame
from pymel.internal.pmcmds import FBXExportBakeComplexEnd
from pymel.internal.pmcmds import debugVar
from pymel.internal.pmcmds import u3dTopoValid
from pymel.internal.pmcmds import FBXExportAxisConversionMethod
from pymel.internal.pmcmds import xgmExportSplineDataInternal
from pymel.internal.pmcmds import xgmLengthBrushToolCmd
from pymel.internal.pmcmds import agFormatOut
from pymel.internal.pmcmds import typeManipContextCommand
from pymel.internal.pmcmds import arnoldImportAss
from pymel.internal.pmcmds import cMuscleSimulate
from pymel.internal.pmcmds import flushThumbnailCache
from pymel.internal.pmcmds import FBXExportGenerateLog
from pymel.internal.pmcmds import nexOpt
from pymel.internal.pmcmds import deformerEvaluator
from pymel.internal.pmcmds import journal
from pymel.internal.pmcmds import muMessageAdd
from pymel.internal.pmcmds import testPassContribution
from pymel.internal.pmcmds import FBXExportConvert2Tif
from pymel.internal.pmcmds import iGroom
from pymel.internal.pmcmds import LoadHIKEffectorSetState
from pymel.internal.pmcmds import hikRigSync
from pymel.internal.pmcmds import memoryDiag
from pymel.internal.pmcmds import ogsdebug
from pymel.internal.pmcmds import psdConvSolidTxOptions
from pymel.internal.pmcmds import xgmSplineCache
from pymel.internal.pmcmds import xgmDirectionBrushToolCmd
from pymel.internal.pmcmds import meshIntersectTest
from pymel.internal.pmcmds import dgPerformance
from pymel.internal.pmcmds import sbs_GetEngine
from pymel.internal.pmcmds import removeListItem
from pymel.internal.pmcmds import renderLayerMembers
from pymel.internal.pmcmds import FBXExportColladaSingleMatrix
from pymel.internal.pmcmds import FBXExport
from pymel.internal.pmcmds import xgmMakeGuideDynamic
from pymel.internal.pmcmds import FBXImportSetTake
from pymel.internal.pmcmds import GetHIKEffectorCount
from pymel.internal.pmcmds import retimeHelper
from pymel.internal.pmcmds import arnoldExportAss
from pymel.internal.pmcmds import FBXExportInstances
from pymel.internal.pmcmds import FBXImportAudio
from pymel.internal.pmcmds import invertShape
from pymel.internal.pmcmds import FBXExportColladaFrameRate
from pymel.internal.pmcmds import OneClickExecute
from pymel.internal.pmcmds import hikCharacterToolWidget
from pymel.internal.pmcmds import OneClickSetupMotionBuilderCharacterStream
from pymel.internal.pmcmds import FBXImportOCMerge
from pymel.internal.pmcmds import xgmSelectedPrims
from pymel.internal.pmcmds import nodeGrapher
from pymel.internal.pmcmds import sbs_SetGlobalTextureHeight
from pymel.internal.pmcmds import reproInstancer
from pymel.internal.pmcmds import FBXExportAnimationOnly
from pymel.internal.pmcmds import gpuCache
from pymel.internal.pmcmds import Unfold3DuvUpdateCommand
from pymel.internal.pmcmds import xgmSelectBrushToolCmd
from pymel.internal.pmcmds import xgmPlaceBrushToolCmd
from pymel.internal.pmcmds import arnoldScene
from pymel.internal.pmcmds import xgmGuideRender
from pymel.internal.pmcmds import artFluidAttr
from pymel.internal.pmcmds import hikRigAlign
from pymel.internal.pmcmds import xgmCombBrushToolCmd
from pymel.internal.pmcmds import manipComponentPivot
from pymel.internal.pmcmds import FBXImportForcedFileAxis
from pymel.internal.pmcmds import sbs_GetEnumValue
from pymel.internal.pmcmds import webViewCmd
from pymel.internal.pmcmds import xgmPartBrushToolCmd
from pymel.internal.pmcmds import sbs_AffectTheseAttributes
from pymel.internal.pmcmds import FBXExportInputConnections
from pymel.internal.pmcmds import polySuperShape
from pymel.internal.pmcmds import FBXImportConvertDeformingNullsToJoint
from pymel.internal.pmcmds import GetHIKChildCount
from pymel.internal.pmcmds import FBXExportSkeletonDefinitions
from pymel.internal.pmcmds import xgmClumpMap
from pymel.internal.pmcmds import meshRemap
from pymel.internal.pmcmds import bifrost
from pymel.internal.pmcmds import adskSceneMetadataCmd
from pymel.internal.pmcmds import prependListItem
from pymel.internal.pmcmds import directConnectPath
from pymel.internal.pmcmds import cMuscleWeightDefault
from pymel.internal.pmcmds import xgmGuideSculptToolCmd
from pymel.internal.pmcmds import polyGear
from pymel.internal.pmcmds import isDescendentPulling
from pymel.internal.pmcmds import adskAsset
from pymel.internal.pmcmds import sbs_GetGraphsNamesFromSubstanceNode
from pymel.internal.pmcmds import dR_multiCutSlicePointCmd
from pymel.internal.pmcmds import FBXGetTakeCount
from pymel.internal.pmcmds import xgmBakeGuideVertices
from pymel.internal.pmcmds import readPDC
from pymel.internal.pmcmds import igBrush
from pymel.internal.pmcmds import iterOnNurbs
from pymel.internal.pmcmds import blend
from pymel.internal.pmcmds import FBXImportConvertUnitString
from pymel.internal.pmcmds import adskAssetLibrary
from pymel.internal.pmcmds import sbs_GetPackageFullPathNameFromSubstanceNode
from pymel.internal.pmcmds import hikGetEffectorIdFromName
from pymel.internal.pmcmds import polyPlatonic
from pymel.internal.pmcmds import xgmParticleRender
from pymel.internal.pmcmds import paintPointsCmd
from pymel.internal.pmcmds import GetHIKChildId
from pymel.internal.pmcmds import FBXImportFillTimeline
from pymel.internal.pmcmds import dgstats
from pymel.internal.pmcmds import OneClickGetState
from pymel.internal.pmcmds import greasePencil
from pymel.internal.pmcmds import xgmSplineApplyRenderOverride
from pymel.internal.pmcmds import xgmBakeGuideToUVSpace
from pymel.internal.pmcmds import FBXExportQuickSelectSetAsCache
from pymel.internal.pmcmds import xgmPatchInfo
from pymel.internal.pmcmds import xgmSplineSetCurrentDescription
from pymel.internal.pmcmds import xgmMelRender
from pymel.internal.pmcmds import cMuscleWeightSave
from pymel.internal.pmcmds import FBXExportBakeResampleAnimation
from pymel.internal.pmcmds import sbs_GetWorkflow
from pymel.internal.pmcmds import renderSetupSelect
from pymel.internal.pmcmds import FBXExportUseTmpFilePeripheral
from pymel.internal.pmcmds import xgmPushOver
from pymel.internal.pmcmds import clearShear
from pymel.internal.pmcmds import xgmFreezeBrushToolCmd
from pymel.internal.pmcmds import renderSetupPostApply
from pymel.internal.pmcmds import artSetPaint
from pymel.internal.pmcmds import hikManip
from pymel.internal.pmcmds import sbs_GetBakeFormat
from pymel.internal.pmcmds import FBXExportUseSceneName
from pymel.internal.pmcmds import ResetProperty2State
from pymel.internal.pmcmds import arnoldRenderToTexture
from pymel.internal.pmcmds import xgmSplinePreset
from pymel.internal.pmcmds import arnoldLicense
from pymel.internal.pmcmds import dR_nexCmd
from pymel.internal.pmcmds import editImportedStatus
from pymel.internal.pmcmds import FBXGetTakeName
from pymel.internal.pmcmds import xgmPolyToGuide
from pymel.internal.pmcmds import myTestCmd
from pymel.internal.pmcmds import FBXImportScaleFactor
from pymel.internal.pmcmds import dispatchGenericCommand
from pymel.internal.pmcmds import HIKInitAxis
from pymel.internal.pmcmds import FBXProperty
from pymel.internal.pmcmds import syncSculptCache
from pymel.internal.pmcmds import FBXImportSkins
from pymel.internal.pmcmds import xgmBrushManip
from pymel.internal.pmcmds import TrenderSetupStates
from pymel.internal.pmcmds import FBXExportInAscii
from pymel.internal.pmcmds import subgraph
from pymel.internal.pmcmds import FBXGetTakeComment
from pymel.internal.pmcmds import u3dAutoSeam
from pymel.internal.pmcmds import sbs_GetEnumName
from pymel.internal.pmcmds import dR_multiCutPointCmd
from pymel.internal.pmcmds import renderSetupFind
from pymel.internal.pmcmds import OneClickMotionBuilderSendToCurrentScene
from pymel.internal.pmcmds import dagCommandWrapper
from pymel.internal.pmcmds import bifMeshExport
from pymel.internal.pmcmds import FBXImportGenerateLog
from pymel.internal.pmcmds import poseInterpolator
from pymel.internal.pmcmds import xgmSmoothBrushToolCmd
from pymel.internal.pmcmds import pointCloudInfo
from pymel.internal.pmcmds import renderSetupSwitchVisibleRenderLayer
from pymel.internal.pmcmds import xgmFindAttachment
from pymel.internal.pmcmds import FBXExportTriangulate
from pymel.internal.pmcmds import xgmNoiseBrushToolCmd
from pymel.internal.pmcmds import xgmSetAttr
from pymel.internal.pmcmds import sbs_GetGlobalTextureHeight
from pymel.internal.pmcmds import GetHIKEffectorName
from pymel.internal.pmcmds import arnoldPlugins
from pymel.internal.pmcmds import xgmPromoteRender
from pymel.internal.pmcmds import FBXExportAudio
from pymel.internal.pmcmds import dgcontrol
from pymel.internal.pmcmds import sbs_AffectedByAllInputs
from pymel.internal.pmcmds import sbs_GetEditionModeScale
from pymel.internal.pmcmds import unapplyOverride
from pymel.internal.pmcmds import FBXExportSplitAnimationIntoTakes
from pymel.internal.pmcmds import addIK2BsolverCallbacks
from pymel.internal.pmcmds import arnoldIpr
from pymel.internal.pmcmds import dR_contextChanged
from pymel.internal.pmcmds import debugNamespace
from pymel.internal.pmcmds import xgmDensityComp
from pymel.internal.pmcmds import polyPrimitiveMisc
from pymel.internal.pmcmds import AbcImport
from pymel.internal.pmcmds import FBXImportUnlockNormals
from pymel.internal.pmcmds import polyIterOnPoly
from pymel.internal.pmcmds import mouldMesh
from pymel.internal.pmcmds import u3dOptimize
from pymel.internal.pmcmds import evalContinue
from pymel.internal.pmcmds import OneClickSetCallback
from pymel.internal.pmcmds import xgmSculptLayerMerge
from pymel.internal.pmcmds import cMuscleWeightMirror
from pymel.internal.pmcmds import subdDisplayMode
from pymel.internal.pmcmds import caddyManip
from pymel.internal.pmcmds import muMessageDelete
from pymel.internal.pmcmds import flushIdleQueue
from pymel.internal.pmcmds import mirrorShape
from pymel.internal.pmcmds import FBXExportQuaternion
from pymel.internal.pmcmds import vectorize
from pymel.internal.pmcmds import testPa
from pymel.internal.pmcmds import FBXExportBakeComplexStep
from pymel.internal.pmcmds import polySpinEdge
from pymel.internal.pmcmds import FBXGetTakeIndex
from pymel.internal.pmcmds import arnoldCopyAsAdmin
from pymel.internal.pmcmds import FBXPopSettings
from pymel.internal.pmcmds import muMessageQuery
from pymel.internal.pmcmds import sbs_GetAutoBake
from pymel.internal.pmcmds import ikSpringSolverCallbacks
from pymel.internal.pmcmds import polyUVStackSimilarShellsCmd
from pymel.internal.pmcmds import assignShaderToType
from pymel.internal.pmcmds import insertListItemBefore
from pymel.internal.pmcmds import FBXExportFinestSubdivLevel
from pymel.internal.pmcmds import FBXImportResamplingRateSource
from pymel.internal.pmcmds import GetHIKNodeName
from pymel.internal.pmcmds import adskRepresentation
from pymel.internal.pmcmds import renderSetupLocalOverride
from pymel.internal.pmcmds import FBXExportConvertUnitString
from pymel.internal.pmcmds import cMuscleQuery
from pymel.internal.pmcmds import artAttrSkinPaintCmd
from pymel.internal.pmcmds import HIKComputeReference
from pymel.internal.pmcmds import FBXResamplingRate
from pymel.internal.pmcmds import cMuscleCompIndex
from pymel.internal.pmcmds import subdToNurbs
from pymel.internal.pmcmds import sbs_GetSubstanceBuildVersion
from pymel.internal.pmcmds import FBXExportConstraints
from pymel.internal.pmcmds import xgmGroomConvert
from pymel.internal.pmcmds import cMuscleAbout
from pymel.internal.pmcmds import LoadHIKCharacterState
from pymel.internal.pmcmds import crashInfoCmd
from pymel.internal.pmcmds import sbs_IsSubstanceRelocalized
from pymel.internal.pmcmds import FBXExportScaleFactor
from pymel.internal.pmcmds import sbs_SetAutoBake
from pymel.internal.pmcmds import FBXExportLights
from pymel.internal.pmcmds import GetHIKNode
from pymel.internal.pmcmds import xgmRebuildCurve
from pymel.internal.pmcmds import polyDisc
from pymel.internal.pmcmds import FBXClose
from pymel.internal.pmcmds import FBXExportBakeComplexAnimation
from pymel.internal.pmcmds import greasePencilHelper
from pymel.internal.pmcmds import xgmUISelectionSync
from pymel.internal.pmcmds import renderSetupLegacyLayer
from pymel.internal.pmcmds import mtkShrinkWrap
from pymel.internal.pmcmds import mouldSrf
from pymel.internal.pmcmds import igConvertToLogical
from pymel.internal.pmcmds import FBXImportHardEdges
from pymel.internal.pmcmds import FBXImportAutoAxisEnable
from pymel.internal.pmcmds import xgmSplineSelect
from pymel.internal.pmcmds import FBXExportColladaTriangulate
from pymel.internal.pmcmds import FBXImportConstraints
from pymel.internal.pmcmds import SymmetrizeUVUpdateCommand
from pymel.internal.pmcmds import appendListItem
from pymel.internal.pmcmds import cMuscleRayIntersect
from pymel.internal.pmcmds import sbs_GetEnumCount
from pymel.internal.pmcmds import dynTestData
from pymel.internal.pmcmds import cMuscleCache
from pymel.internal.pmcmds import FBXLoadImportPresetFile
from pymel.internal.pmcmds import manipComponentUpdate
from pymel.internal.pmcmds import xgmNop
from pymel.internal.pmcmds import copyNode
from pymel.internal.pmcmds import FBXExportUpAxis
from pymel.internal.pmcmds import FBXExportDeleteOriginalTakeOnSplitAnimation
from pymel.internal.pmcmds import sbs_SetGlobalTextureWidth
from pymel.internal.pmcmds import geoUtils
from pymel.internal.pmcmds import GPUBuiltInDeformerControl
from pymel.internal.pmcmds import xgmBindPatches
from pymel.internal.pmcmds import shaderfx
from pymel.internal.pmcmds import FBXExportSkins
from pymel.internal.pmcmds import FBXImportMode
from pymel.internal.pmcmds import xgmGuideGeom
from pymel.internal.pmcmds import FBXExportFileVersion
from pymel.internal.pmcmds import xgmCutBrushToolCmd
from pymel.internal.pmcmds import meshReorder
from pymel.internal.pmcmds import artSelect
from pymel.internal.pmcmds import mtkQuadDrawPoint
from pymel.internal.pmcmds import ikSpringSolverRestPose
from pymel.internal.pmcmds import rampWidgetAttrless
from pymel.internal.pmcmds import FBXResetExport
from pymel.internal.pmcmds import FBXGetTakeLocalTimeSpan
from pymel.internal.pmcmds import u3dLayout
from pymel.internal.pmcmds import xgmDraRender
from pymel.internal.pmcmds import adskAssetList
from pymel.internal.pmcmds import cMuscleWeightPrune
from pymel.internal.pmcmds import sbs_EditSubstance
from pymel.internal.pmcmds import OneClickAcknowledgeCallback
from pymel.internal.pmcmds import FBXImport
from pymel.internal.pmcmds import LoadHIKCharacterDefinition
from pymel.internal.pmcmds import FBXImportProtectDrivenKeys
from pymel.internal.pmcmds import FBXLoadExportPresetFile
from pymel.internal.pmcmds import xgmRebuildSplineDescription
from pymel.internal.pmcmds import xgmWrapXGen
from pymel.internal.pmcmds import polySetVertices
from pymel.internal.pmcmds import SaveHIKCharacterDefinition
from pymel.internal.pmcmds import xgmMoveDescription
from pymel.internal.pmcmds import dagObjectHit
from pymel.internal.pmcmds import xgmExportToP3D
from pymel.internal.pmcmds import OneClickFetchRemoteCharacter
from pymel.internal.pmcmds import xgmDataQueryHelperForTest
from pymel.internal.pmcmds import LoadHIKPropertySetState
from pymel.internal.pmcmds import polyTestPop
from pymel.internal.pmcmds import FBXGetTakeReferenceTimeSpan
from pymel.internal.pmcmds import hotkeyMapSet
from pymel.internal.pmcmds import debug
from pymel.internal.pmcmds import polySelectEditCtxDataCmd
from pymel.internal.pmcmds import FBXImportSetLockedAttribute
from pymel.internal.pmcmds import hikBodyPart
from pymel.internal.pmcmds import polyColorSetCmdWrapper
from pymel.internal.pmcmds import xgmClumpBrushToolCmd
from pymel.internal.pmcmds import insertListItem
from pymel.internal.pmcmds import FBXImportSkeletonDefinitionsAs
from pymel.internal.pmcmds import FBXImportUpAxis
from pymel.internal.pmcmds import hotkeyEditor
from pymel.internal.pmcmds import nop
from pymel.internal.pmcmds import characterizationToolUICmd
from pymel.internal.pmcmds import xgmGrabBrushToolCmd
from pymel.internal.pmcmds import cMuscleRelaxSetup
from pymel.internal.pmcmds import xgmCreateSplineDescription
from pymel.internal.pmcmds import xgmDensityBrushToolCmd
from pymel.internal.pmcmds import sbs_SetBakeFormat
from pymel.internal.pmcmds import GetHIKParentId
from pymel.internal.pmcmds import FBXLoadMBImportPresetFile
from pymel.internal.pmcmds import sbs_GoToMarketPlace
from pymel.internal.pmcmds import agFormatIn
from pymel.internal.pmcmds import setDynamicsInitialState
from pymel.internal.pmcmds import FBXImportMergeAnimationLayers
from pymel.internal.pmcmds import renderSetup
from pymel.internal.pmcmds import polySelectSp
from pymel.internal.pmcmds import fontAttributes
from pymel.internal.pmcmds import hikGetNodeIdFromName
from pymel.internal.pmcmds import arnoldUpdateTx
from pymel.internal.pmcmds import xgmModifierGuideOp
from pymel.internal.pmcmds import moduleDetectionLogic
from pymel.internal.pmcmds import groupParts
from pymel.internal.pmcmds import gameExporter
from pymel.internal.pmcmds import xgmWidthBrushToolCmd
from pymel.internal.pmcmds import FBXImportShapes
from pymel.internal.pmcmds import FBXImportQuaternion
from pymel.internal.pmcmds import FBXExportReferencedContainersContent
from pymel.internal.pmcmds import xgmSplineQuery
from pymel.internal.pmcmds import FBXExportShapes
from pymel.internal.pmcmds import FBXExportShowUI
from pymel.internal.pmcmds import FBXExportCacheFile
from pymel.internal.pmcmds import xgmSyncPatchVisibility
from pymel.internal.pmcmds import dgControl
from pymel.internal.pmcmds import cMuscleSplineBind
from pymel.internal.pmcmds import xgmSetActive
from pymel.internal.pmcmds import OneClickGetContactingAppName
from pymel.internal.pmcmds import dR_DoCmd
from pymel.internal.pmcmds import polyToCurve
from pymel.internal.pmcmds import createMeshFromPoints
from pymel.internal.pmcmds import arnoldListAttributes
from pymel.internal.pmcmds import sbs_SetEngine
from pymel.internal.pmcmds import paint3d
from pymel.internal.pmcmds import movieCompressor
from pymel.internal.pmcmds import FBXPushSettings
from pymel.internal.pmcmds import arnoldViewOverrideOptionBox
from pymel.internal.pmcmds import xgmInterpSetup
from pymel.internal.pmcmds import GamePipeline
from pymel.internal.pmcmds import xgmPoints
from pymel.internal.pmcmds import popListItem
from pymel.internal.pmcmds import FBXLoadMBExportPresetFile
from pymel.internal.pmcmds import FBXExportTangents
from pymel.internal.pmcmds import hikGetNodeCount
from pymel.internal.pmcmds import GetProperty2StateAttrNameFromHIKEffectorId
from pymel.internal.pmcmds import greaseRenderPlane
from pymel.internal.pmcmds import artAttrSkinPaint
from pymel.internal.pmcmds import FBXRead
from pymel.internal.pmcmds import createCurveWarp
from pymel.internal.pmcmds import bifMeshImport
from pymel.internal.pmcmds import OneClickDisconnect
from pymel.internal.pmcmds import artAttr
from pymel.internal.pmcmds import FBXExportIncludeChildren
from pymel.internal.pmcmds import FBXExportApplyConstantKeyReducer
from pymel.internal.pmcmds import texSculptCacheSync
from pymel.internal.pmcmds import xgmNullRender
from pymel.internal.pmcmds import arnoldTemperatureToColor
from pymel.internal.pmcmds import mouldSubdiv
from pymel.internal.pmcmds import TanimLayer
from pymel.internal.pmcmds import sbs_SetWorkflow
from pymel.internal.pmcmds import hikCustomRigToolWidget
from pymel.internal.pmcmds import FBXExportSmoothingGroups
from pymel.internal.pmcmds import arnoldBakeGeo
from pymel.internal.pmcmds import FBXImportCacheFile
from pymel.internal.pmcmds import addDynamicAttribute
from pymel.internal.pmcmds import xgmPreview
from pymel.internal.pmcmds import FBXImportCameras
from pymel.internal.pmcmds import arnoldFlushCache
from pymel.internal.pmcmds import licenseCheck
from pymel.internal.pmcmds import xgmSetGuideCVCount
from pymel.internal.pmcmds import FBXImportSetMayaFrameRate
from pymel.internal.pmcmds import GetFKIdFromEffectorId
from pymel.internal.pmcmds import arnoldRender
from pymel.internal.pmcmds import FBXExportSmoothMesh
from pymel.internal.pmcmds import FBXResetImport
from pymel.internal.pmcmds import xgmExport
from pymel.internal.pmcmds import FBXExportReferencedAssetsContent
from pymel.internal.pmcmds import extendFluid
from pymel.internal.pmcmds import createPtexUV
from pymel.internal.pmcmds import cMuscleBindSticky
from pymel.internal.pmcmds import OneClickDispatch
from pymel.internal.pmcmds import renderSetupHighlight
from pymel.internal.pmcmds import FBXUICallBack
from pymel.internal.pmcmds import xgmCurveToGuide
from pymel.internal.pmcmds import nurbsCurveRebuildPref
from pymel.internal.pmcmds import sbs_SetEditionModeScale
from pymel.internal.pmcmds import xgmGeoRender
from pymel.internal.pmcmds import notifyDecorator
from pymel.internal.pmcmds import adpAnalyticsDialog
from pymel.internal.pmcmds import OneClickMenuExecute
from pymel.internal.pmcmds import HIKGetRemoteCharacterList
from pymel.internal.pmcmds import xgmGroomTransfer
from pymel.internal.pmcmds import aiViewRegionCmd
from pymel.internal.pmcmds import xgmAddGuide
from pymel.internal.pmcmds import FBXExportEmbeddedTextures
from pymel.internal.pmcmds import notifyPostUndo
from pymel.internal.pmcmds import popPinning
from pymel.internal.pmcmds import HIKUiControl
from pymel.internal.pmcmds import mayaDpiSettingAction
from pymel.internal.pmcmds import FBXImportLights
from pymel.internal.pmcmds import FBXExportBakeComplexStart
from pymel.internal.pmcmds import FBXImportMergeBackNullPivots
from pymel.internal.pmcmds import interactionStyle
from pymel.internal.pmcmds import rampWidget
from pymel.internal.pmcmds import cMuscleWeight
from pymel.internal.pmcmds import u3dUnfold
from pymel.internal.pmcmds import AbcExport

if False:
    from typing import Dict, List, Tuple, Union, Optional


class NameParser(str):
    def __getattr__(self, attr):
        """
        >>> NameParser('foo:bar').spangle
        AttributeName(u'foo:bar.spangle')
        """
        pass

    def __repr__(self): pass

    def addPrefix(self, prefix):
        """
        addPrefixToName
        """
        pass

    def attr(self, attr):
        """
        access to AttributeName of a node. returns an instance of the
        AttributeName class for the given AttributeName.
        
            >>> NameParser('foo:bar').attr('spangle')
            AttributeName(u'foo:bar.spangle')
        """
        pass

    def namespace(self):
        """
        Returns the namespace of the object with trailing colon included
        """
        pass

    def namespaceList(self):
        """
        Useful for cascading references.
        
        Returns all of the namespaces of the calling object as a list
        """
        pass

    def stripGivenNamespace(self, namespace, partial='True'):
        """
        Returns a new instance of the object with any occurrences of the given namespace removed.  The calling instance is unaffected.
        The given namespace may end with a ':', or not.
        If partial is True (the default), and the given namespace has parent namespaces (ie, 'one:two:three'),
        then any occurrences of any parent namespaces are also stripped - ie, 'one' and 'one:two' would
        also be stripped.  If it is false, only namespaces
        
            >>> NameParser('foo:bar:top|foo:middle|foo:bar:extra:guy.spangle').stripGivenNamespace('foo:bar')
            AttributeName(u'top|middle|extra:guy.spangle')
        
            >>> NameParser('foo:bar:top|foo:middle|foo:bar:extra:guy.spangle').stripGivenNamespace('foo:bar', partial=False)
            AttributeName(u'top|foo:middle|extra:guy.spangle')
        """
        pass

    def stripNamespace(self, levels='0'):
        """
        Returns a new instance of the object with its namespace removed.  The calling instance is unaffected.
        The optional levels keyword specifies how many levels of cascading namespaces to strip, starting with the topmost (leftmost).
        The default is 0 which will remove all namespaces.
        
            >>> NameParser('foo:bar.spangle').stripNamespace()
            AttributeName(u'bar.spangle')
        """
        pass

    def swapNamespace(self, prefix):
        """
        Returns a new instance of the object with its current namespace
        replaced with the provided one.
        
        The calling instance is unaffected.
        """
        pass

    @staticmethod
    def __new__(cls, strObj):
        """
        Casts a string to a pymel class.
        
        Use this function if you are unsure which class is the right one to use
        for your object.
        """
        pass

    PARENT_SEP = '|'

    __dict__ = None

    __weakref__ = None


class DependNodeName(NameParser):
    def exists(self, **kwargs):
        """
        objExists
        """
        pass

    def extractNum(self):
        """
        Return the trailing numbers of the node name.
        
        If no trailing numbers are found an error will be raised.
        """
        pass

    def nextName(self):
        """
        Increment the trailing number of the object by 1
        """
        pass

    def nextUniqueName(self):
        """
        Increment the trailing number of the object until a unique name is found
        
        If there is no trailing number, appends '1' to the name.
        Will always return a different name than the current name, even if the
            current name already does not exist.
        """
        pass

    def node(self):
        """
        for compatibility with AttributeName class
        """
        pass

    def nodeName(self):
        """
        for compatibility with DagNodeName class
        """
        pass

    def prevName(self):
        """
        Decrement the trailing number of the object by 1
        """
        pass

    def stripNum(self):
        """
        Return the name of the node with trailing numbers stripped off.
        
        If no trailing numbers are found the name will be returned unchanged.
        """
        pass


class AttributeName(NameParser):
    def __call__(self, *args, **kwargs):
        """
        # Added the __call__ so to generate a more appropriate exception when a class method is not found
        """
        pass

    def __getitem__(self, item): pass

    def __init__(self, attrName): pass

    def add(self, **kwargs): pass

    def addAttr(self, **kwargs): pass

    def array(self):
        """
        Returns the array (multi) AttributeName of the current element
            >>> n = AttributeName('lambert1.groupNodes[0]')
            >>> n.array()
            AttributeName(u'lambert1.groupNodes')
        """
        pass

    def exists(self): pass

    def getParent(self, generations='1'):
        """
        Returns the parent attribute
        
        Modifications:
            - added optional generations flag, which gives the number of levels up that you wish to go for the parent;
              ie:
                  >>> AttributeName("Cube1.multiComp[3].child.otherchild").getParent(2)
                  AttributeName(u'Cube1.multiComp[3]')
        
              Negative values will traverse from the top, not counting the initial node name:
        
                  >>> AttributeName("Cube1.multiComp[3].child.otherchild").getParent(-2)
                  AttributeName(u'Cube1.multiComp[3].child')
        
              A value of 0 will return the same node.
              The default value is 1.
        
              Since the original command returned None if there is no parent, to sync with this behavior, None will
              be returned if generations is out of bounds (no IndexError will be thrown).
        """
        pass

    def item(self, asSlice='False', asString='False'): pass

    def lastPlugAttr(self):
        """
        >>> NameParser('foo:bar.spangle.banner').lastPlugAttr()
        u'banner'
        """
        pass

    def node(self):
        """
        plugNode
        
        >>> NameParser('foo:bar.spangle.banner').plugNode()
        DependNodeName(u'foo:bar')
        """
        pass

    def nodeName(self):
        """
        basename
        """
        pass

    def plugAttr(self):
        """
        plugAttr
        
        >>> NameParser('foo:bar.spangle.banner').plugAttr()
        u'spangle.banner'
        """
        pass

    def plugNode(self):
        """
        plugNode
        
        >>> NameParser('foo:bar.spangle.banner').plugNode()
        DependNodeName(u'foo:bar')
        """
        pass

    def set(self, *args, **kwargs): pass

    def setAttr(self, *args, **kwargs): pass

    attrItemReg = None


class DagNodeName(DependNodeName):
    def firstParent(self):
        """
        firstParentOf
        """
        pass

    def getParent(self, generations='1'):
        """
        Returns the parent node
        
        Modifications:
            - added optional generations flag, which gives the number of levels up that you wish to go for the parent;
              ie:
                  >>> DagNodeName("NS1:TopLevel|Next|ns2:Third|Fourth").getParent(2)
                  DagNodeName(u'NS1:TopLevel|Next')
        
              Negative values will traverse from the top, not counting the initial node name:
        
                  >>> DagNodeName("NS1:TopLevel|Next|ns2:Third|Fourth").getParent(-3)
                  DagNodeName(u'NS1:TopLevel|Next|ns2:Third')
        
              A value of 0 will return the same node.
              The default value is 1.
        
              Since the original command returned None if there is no parent, to sync with this behavior, None will
              be returned if generations is out of bounds (no IndexError will be thrown).
        """
        pass

    def getRoot(self):
        """
        unlike the root command which determines the parent via string formatting, this
        command uses the listRelatives command
        """
        pass

    def nodeName(self):
        """
        basename
        """
        pass

    def root(self):
        """
        rootOf
        """
        pass


def repeatLast(*args, **kwargs):
    """
    Flags:
    - addCommand : ac                (unicode)       []
    
    - addCommandLabel : acl          (unicode)       []
    
    - commandList : cl               (int)           []
    
    - commandNameList : cnl          (int)           []
    
    - historyLimit : hl              (int)           []
    
    - item : i                       (int)           []
    
    - numberOfHistoryItems : nhi     (bool)          []
    
    
    Derived from mel command `maya.cmds.repeatLast`
    """
    pass


def _getParserClass(strObj): pass


def adskAssetListUI(*args, **kwargs):
    """
    Flags:
    - commandSuffix : cms            (unicode)       []
    
    - materialLoaded : mld           (bool)          []
    
    - uiCommand : uiC                (unicode)       []
    
    
    Derived from mel command `maya.cmds.adskAssetListUI`
    """
    pass


def cacheEvaluator(*args, **kwargs):
    """
    Flags:
    - cacheFillMode : cfm            (unicode)       []
    
    - cacheFillOrder : cfo           (unicode)       []
    
    - cacheInvalidate : ci           (timeRange)     []
    
    - cacheName : cn                 (unicode)       []
    
    - cachingPoints : cps            (bool)          []
    
    - creationParameters : cp        (bool)          []
    
    - flushCache : fc                (unicode)       []
    
    - flushCacheRange : fcr          (timeRange, <type 'bool'>) []
    
    - flushCacheSync : fcs           (bool)          []
    
    - flushCacheWait : fcw           (bool)          []
    
    - listCacheNames : lcn           (bool)          []
    
    - listCachedNodes : lcd          (bool)          []
    
    - listValueNames : lvn           (bool)          []
    
    - newAction : na                 (unicode)       []
    
    - newActionParam : nap           (unicode)       []
    
    - newFilter : nf                 (unicode)       []
    
    - newFilterParam : nfp           (unicode)       []
    
    - newRule : nr                   (unicode)       []
    
    - newRuleParam : nrp             (unicode)       []
    
    - pauseInvalidation : pi         (bool)          []
    
    - preventFrameSkip : pfs         (bool)          []
    
    - resetRules : rr                (bool)          []
    
    - resourceUsage : ru             (bool)          []
    
    - resumeInvalidation : ri        (bool)          []
    
    - safeMode : sf                  (bool)          []
    
    - safeModeMessages : sfm         (bool)          []
    
    - safeModeTriggered : sft        (bool)          []
    
    - valueName : vn                 (unicode)       []
    
    - waitForCache : wfc             (float)         []
    
    
    Derived from mel command `maya.cmds.cacheEvaluator`
    """
    pass


def imageWindowEditor(*args, **kwargs):
    """
    Flags:
    - autoResize : ar                (bool)          []
    
    - changeCommand : cc             (unicode, unicode, unicode, unicode) []
    
    - clear : cl                     (int, int, float, float, float) []
    
    - control : ctl                  (bool)          []
    
    - defineTemplate : dt            (unicode)       []
    
    - displayImage : di              (int)           []
    
    - displayStyle : dst             (unicode)       []
    
    - docTag : dtg                   (unicode)       []
    
    - doubleBuffer : dbf             (bool)          []
    
    - drawAxis : da                  (bool)          []
    
    - exists : ex                    (bool)          []
    
    - filter : f                     (unicode)       []
    
    - forceMainConnection : fmc      (unicode)       []
    
    - frameImage : fi                (bool)          []
    
    - frameRegion : fr               (bool)          []
    
    - highlightConnection : hlc      (unicode)       []
    
    - loadImage : li                 (unicode)       []
    
    - lockMainConnection : lck       (bool)          []
    
    - mainListConnection : mlc       (unicode)       []
    
    - marquee : mq                   (float, float, float, float) []
    
    - nbImages : nim                 (bool)          []
    
    - panel : pnl                    (unicode)       []
    
    - parent : p                     (unicode)       []
    
    - realSize : rs                  (bool)          []
    
    - refresh : ref                  (bool)          []
    
    - removeAllImages : ra           (bool)          []
    
    - removeImage : ri               (bool)          []
    
    - saveImage : si                 (bool)          []
    
    - scaleBlue : sb                 (float)         []
    
    - scaleGreen : sg                (float)         []
    
    - scaleRed : sr                  (float)         []
    
    - selectionConnection : slc      (unicode)       []
    
    - showRegion : srg               (int, int)      []
    
    - singleBuffer : sbf             (bool)          []
    
    - stateString : sts              (bool)          []
    
    - toggle : tgl                   (bool)          []
    
    - unParent : up                  (bool)          []
    
    - unlockMainConnection : ulk     (bool)          []
    
    - updateMainConnection : upd     (bool)          []
    
    - useTemplate : ut               (unicode)       []
    
    - writeImage : wi                (unicode)       []
    
    
    Derived from mel command `maya.cmds.imageWindowEditor`
    """
    pass


def selectKeyframe(*args, **kwargs):
    """
    Flags:
    - animation : an                 (unicode)       []
    
    - attribute : at                 (unicode)       []
    
    - controlPoints : cp             (bool)          []
    
    - float : f                      (floatRange)    []
    
    - hierarchy : hi                 (unicode)       []
    
    - includeUpperBound : iub        (bool)          []
    
    - index : index                  (indexRange)    []
    
    - selectionWindow : sel          (float, float, float, float) []
    
    - shape : s                      (bool)          []
    
    - time : t                       (timeRange)     []
    
    
    Derived from mel command `maya.cmds.selectKeyframe`
    """
    pass


def flagTest(*args, **kwargs):
    """
    Flags:
    - floatRange : fr                (floatRange)    []
    
    - indexRange : ir                (indexRange)    []
    
    - multiUse : mu                  (float, int, unicode) []
    
    - noReport : nr                  (bool)          []
    
    - optionalQueryArgsFlag : oqa    (float, int, unicode) []
    
    - pythonOptionalQueryArgsFlag : poq (float, int, unicode) []
    
    - pythonQueryArgsFlag : pq       (float, int, unicode) []
    
    - queryArgsFlag : qa             (float, int, unicode) []
    
    - simpleFlag : s                 (bool)          []
    
    - stringArrayFlag : saf          (string[...])   []
    
    - stringFlag : sf                (unicode)       []
    
    - timeRange : tr                 (timeRange)     []
    
    - tripleFloat : tf               (float, float, float) []
    
    
    Derived from mel command `maya.cmds.flagTest`
    """
    pass
