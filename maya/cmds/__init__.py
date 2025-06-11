from time import sleep
import re
import platform
from typing import Union
from pathlib import Path
import weakref
import maya.mmc_hierarchy as _hierarchy
from .custom_cmds import *
from maya.api import OpenMaya as om
from maya import ACTIVE_SELECTION
from mmc_output import node_types_to_shapes


def _register_node_from_name(node_name:str) -> om.MObject:
    mobject = _hierarchy.NodePool.from_name(node_name)

    if mobject:
        return mobject

    # Object could have been given with path and not have this one registered. Try with just name
    if "|" in node_name:
        mobject = _hierarchy.NodePool.from_name(node_name.split("|")[-1])
        if mobject:
            return mobject

    # Else, assume in scene. Not created through this api
    sl_ls = om.MSelectionList()
    sl_ls.add(node_name)
    mobject = sl_ls.getDependNode(0)
    _hierarchy.register(mobject)
    return mobject


def _attr_name_to_mobject_and_plug(attr_name:str) -> tuple["om.MObject", "om.MPlug"]:
    node_name, attr_name = attr_name.split(".")
    mobject = _register_node_from_name(node_name)
    mfn_dep_node = om.MFnDependencyNode(mobject)
    plug = mfn_dep_node.findPlug(attr_name, False)
    return mobject, plug


def aaf2fcp(deleteFile=bool(), df=bool(), dstPath=str(), dst=str(), getFileName=int(), gfn=int(), progress=int(),
            pr=int(), srcFile=str(), src=str(), terminate=int(), t=int(), waitCompletion=int(), wc=int(), *args,
            **kwargs):
    pass


def about(apiVersion=bool(), api=bool(), application=bool(), a=bool(), batch=bool(), b=bool(), buildDirectory=bool(),
          bd=bool(), buildVariant=bool(), bv=bool(), codeset=bool(), cs=bool(), compositingManager=bool(), cm=bool(),
          connected=bool(), cnt=bool(), ctime=bool(), cti=bool(), currentDate=bool(), cd=bool(), currentTime=bool(),
          ct=bool(), customVersion=bool(), cv=bool(), customVersionClient=bool(), cvc=bool(), customVersionMajor=bool(),
          cvm=bool(), customVersionMinor=bool(), cvn=bool(), customVersionString=bool(), cvs=bool(),
          cutIdentifier=bool(), c=bool(), date=bool(), d=bool(), environmentFile=bool(), env=bool(), evalVersion=bool(),
          ev=bool(), file=bool(), f=bool(), fontInfo=bool(), foi=bool(), helpDataDirectory=bool(), hdd=bool(),
          installedVersion=bool(), iv=bool(), ioVersion=bool(), io=bool(), irix=bool(), ir=bool(), is64=bool(),
          x64=bool(), languageResources=bool(), lr=bool(), linux=bool(), li=bool(), linux64=bool(), l64=bool(),
          liveUpdate=bool(), lu=bool(), localizedResourceLocation=bool(), lrl=bool(), ltVersion=bool(), lt=bool(),
          macOS=bool(), mac=bool(), macOSppc=bool(), ppc=bool(), macOSx86=bool(), x86=bool(), majorVersion=bool(),
          mjv=bool(), minorVersion=bool(), mnv=bool(), ntOS=bool(), nt=bool(), operatingSystem=bool(), os=bool(),
          operatingSystemVersion=bool(), osv=bool(), patchVersion=bool(), pv=bool(), preferences=bool(), pd=bool(),
          product=bool(), p=bool(), qtVersion=bool(), qt=bool(), tablet=bool(), tab=bool(), tabletMode=bool(),
          tm=bool(), uiLanguage=bool(), uil=bool(), uiLanguageForStartup=bool(), uis=bool(),
          uiLanguageIsLocalized=bool(), uii=bool(), uiLocaleLanguage=bool(), ull=bool(), version=bool(), v=bool(),
          win64=bool(), w64=bool(), windowManager=bool(), wm=bool(), windows=bool(), win=bool(), *args, **kwargs):
    if v or version:
        _DEFAULT_MAYA_LOCATIONS = {
            'Windows': r'C:/Program Files/Autodesk/Maya{}',
            'Darwin': r'/Applications/Autodesk/maya{}/Maya.app/Contents',
            'Linux': r'/usr/autodesk/maya{}',
        }
        p = Path(_DEFAULT_MAYA_LOCATIONS[str(platform.system())])
        
        def find_largest_versioned_folder(parent_directory):
            largest_version = -1
            largest_folder = None
            
            # Regular expression to match folder names ending with numbers (e.g., maya2022)
            pattern = re.compile(r'^(.*?)(\d+)$')
            
            # Iterate through the child folders
            for elem in Path(parent_directory).iterdir():
                if not elem.is_dir():
                    continue
                match = pattern.match(elem.name)
                if not match:
                    continue
                version_number = int(match.group(2))  # Extract the trailing number
                if version_number > largest_version:
                    largest_version = version_number
                    largest_folder = elem.name
            return largest_folder

        maya_version = find_largest_versioned_folder(
            next((str(x) for x in p.parents if str(x).lower().endswith("autodesk")))
        )
        return maya_version[4:] if maya_version else None


def addAttr(attributeType=str(), at=str(), binaryTag=str(), bt=str(), cachedInternally=bool(), ci=bool(),
            category=str(), ct=str(), dataType=str(), dt=str(), defaultValue=float(), dv=float(),
            disconnectBehaviour=int(), dcb=int(), enumName=str(), en=str(), exists=bool(), ex=bool(), fromPlugin=bool(),
            fp=bool(), hasMaxValue=bool(), hxv=bool(), hasMinValue=bool(), hnv=bool(), hasSoftMaxValue=bool(),
            hsx=bool(), hasSoftMinValue=bool(), hsn=bool(), hidden=bool(), h=bool(), indexMatters=bool(), im=bool(),
            internalSet=bool(), keyable=bool(), k=bool(), longName=str(), ln=str(), maxValue=float(), max=float(),
            minValue=float(), min=float(), multi=bool(), m=bool(), niceName=str(), nn=str(), numberOfChildren=int(),
            nc=int(), parent=str(), p=str(), proxy=str(), pxy=str(), readable=bool(), r=bool(), shortName=str(),
            sn=str(), softMaxValue=float(), smx=float(), softMinValue=float(), smn=float(), storable=bool(), s=bool(),
            usedAsColor=bool(), uac=bool(), usedAsFilename=bool(), uaf=bool(), usedAsProxy=bool(), uap=bool(),
            worldSpace=bool(), ws=bool(), writable=bool(), w=bool(), *args, **kwargs):
    import cmdx
    if args:
        node_name = args[0]
    else:
        node_name = ls(selection=True)[0]
    cmdx.add_attr(node_name,
                  longName or ln,
                  attributeType or at,
                  shortName=sn or shortName,
                  defaultValue=dv or defaultValue
                  )


def addDynamic(*args, **kwargs):
    pass


def addExtension(attributeType=str(), at=str(), binaryTag=str(), bt=str(), cachedInternally=bool(), ci=bool(),
                 category=str(), ct=str(), dataType=str(), dt=str(), defaultValue=float(), dv=float(),
                 disconnectBehaviour=int(), dcb=int(), enumName=str(), en=str(), exists=bool(), ex=bool(),
                 fromPlugin=bool(), fp=bool(), hasMaxValue=bool(), hxv=bool(), hasMinValue=bool(), hnv=bool(),
                 hasSoftMaxValue=bool(), hsx=bool(), hasSoftMinValue=bool(), hsn=bool(), hidden=bool(), h=bool(),
                 indexMatters=bool(), im=bool(), internalSet=bool(), keyable=bool(), k=bool(), longName=str(), ln=str(),
                 maxValue=float(), max=float(), minValue=float(), min=float(), multi=bool(), m=bool(), niceName=str(),
                 nn=str(), nodeType=str(), nt=str(), numberOfChildren=int(), nc=int(), parent=str(), p=str(),
                 proxy=str(), pxy=str(), readable=bool(), r=bool(), shortName=str(), sn=str(), softMaxValue=float(),
                 smx=float(), softMinValue=float(), smn=float(), storable=bool(), s=bool(), usedAsColor=bool(),
                 uac=bool(), usedAsFilename=bool(), uaf=bool(), usedAsProxy=bool(), uap=bool(), worldSpace=bool(),
                 ws=bool(), writable=bool(), w=bool(), *args, **kwargs):
    pass


def addMetadata(channelName=str(), cn=str(), channelType=str(), cht=str(), indexType=str(), idt=str(), scene=bool(),
                scn=bool(), streamName=str(), stn=str(), structure=str(), str=str(), *args, **kwargs):
    pass


def addPP(attribute=str(), atr=str(), *args, **kwargs):
    pass


def affectedNet(type=str(), t=str(), *args, **kwargs):
    pass


def affects(by=bool(), type=str(), t=str(), *args, **kwargs):
    pass


def aimConstraint(aimVector=list, aim=list, layer=str(), l=str(), maintainOffset=bool(), mo=bool(), name=str(), n=str(),
                  offset=list, o=list, remove=bool(), rm=bool(), skip=str(), sk=str(), targetList=bool(), tl=bool(),
                  upVector=list, u=list, weight=float(), w=float(), weightAliasList=bool(), wal=bool(),
                  worldUpObject=str(), wuo=str(), worldUpType=str(), wut=str(), worldUpVector=list, wu=list, *args,
                  **kwargs):
    pass


def air(attenuation=float(), att=float(), directionX=float(), dx=float(), directionY=float(), dy=float(),
        directionZ=float(), dz=float(), enableSpread=bool(), es=bool(), fanSetup=bool(), fs=bool(),
        inheritRotation=bool(), iro=bool(), inheritVelocity=float(), iv=float(), magnitude=float(), m=float(),
        maxDistance=float(), mxd=float(), name=str(), n=str(), perVertex=bool(), pv=bool(), position=list, pos=list,
        speed=float(), s=float(), spread=float(), sp=float(), torusSectionRadius=float(), tsr=float(),
        velocityComponentOnly=bool(), vco=bool(), volumeExclusion=bool(), vex=bool(), volumeOffset=list, vof=list,
        volumeShape=str(), vsh=str(), volumeSweep=float(), vsw=float(), wakeSetup=bool(), wks=bool(), windSetup=bool(),
        wns=bool(), *args, **kwargs):
    pass


def aliasAttr(remove=bool(), rm=bool(), *args, **kwargs):
    pass


def align(alignToLead=bool(), atl=bool(), coordinateSystem=str(), cs=str(), xAxis=str(), x=str(), yAxis=str(), y=str(),
          zAxis=str(), z=str(), *args, **kwargs):
    pass


def alignCtx(align=bool(), a=bool(), anchorFirstObject=bool(), afo=bool(), distribute=bool(), d=bool(), exists=bool(),
             ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(),
             i3=str(), name=str(), n=str(), showAlignTouch=bool(), sat=bool(), *args, **kwargs):
    pass


def alignCurve(attach=bool(), at=bool(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
               curvatureContinuity=bool(), cc=bool(), curvatureScale1=float(), cs1=float(), curvatureScale2=float(),
               cs2=float(), joinParameter=float(), jnp=float(), keepMultipleKnots=bool(), kmk=bool(), name=str(),
               n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), positionalContinuity=bool(), pc=bool(),
               positionalContinuityType=int(), pct=int(), replaceOriginal=bool(), rpo=bool(), reverse1=bool(),
               rv1=bool(), reverse2=bool(), rv2=bool(), tangentContinuity=bool(), tc=bool(),
               tangentContinuityType=int(), tct=int(), tangentScale1=float(), ts1=float(), tangentScale2=float(),
               ts2=float(), *args, **kwargs):
    pass


def alignSurface(attach=bool(), at=bool(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                 curvatureContinuity=bool(), cc=bool(), curvatureScale1=float(), cs1=float(), curvatureScale2=float(),
                 cs2=float(), directionU=bool(), du=bool(), joinParameter=float(), jnp=float(),
                 keepMultipleKnots=bool(), kmk=bool(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(),
                 o=bool(), positionalContinuity=bool(), pc=bool(), positionalContinuityType=int(), pct=int(),
                 replaceOriginal=bool(), rpo=bool(), reverse1=bool(), rv1=bool(), reverse2=bool(), rv2=bool(),
                 swap1=bool(), sw1=bool(), swap2=bool(), sw2=bool(), tangentContinuity=bool(), tc=bool(),
                 tangentContinuityType=int(), tct=int(), tangentScale1=float(), ts1=float(), tangentScale2=float(),
                 ts2=float(), twist=bool(), tw=bool(), *args, **kwargs):
    pass


def allNodeTypes(includeAbstract=bool(), ia=bool(), *args, **kwargs):
    pass


def ambientLight(ambientShade=float(), discRadius=float(), drs=float(), exclusive=bool(), exc=bool(), intensity=float(),
                 i=float(), name=str(), n=str(), position=list, pos=list, rgb=list, rotation=list, rot=list,
                 shadowColor=list, sc=list, shadowDither=float(), sd=float(), shadowSamples=int(), sh=int(),
                 softShadow=bool(), ss=bool(), useRayTraceShadows=bool(), rs=bool(), *args, **kwargs):
    pass


def angleBetween(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), euler=bool(), er=bool(),
                 nodeState=int(), nds=int(), vector1=list, v1=list, vector1X=float(), v1x=float(), vector1Y=float(),
                 v1y=float(), vector1Z=float(), v1z=float(), vector2=list, v2=list, vector2X=float(), v2x=float(),
                 vector2Y=float(), v2y=float(), vector2Z=float(), v2z=float(), *args, **kwargs):
    pass


def animCurveEditor(areCurvesSelected=bool(), acs=bool(), autoFit=str(), af=str(), autoFitTime=str(), aft=str(),
                    classicMode=bool(), cm=bool(), clipTime=str(), ct=str(), constrainDrag=int(), cd=int(),
                    control=bool(), ctl=bool(), curvesShown=bool(), cs=bool(), curvesShownForceUpdate=bool(),
                    csf=bool(), defineTemplate=str(), dt=str(), denormalizeCurvesCommand=str(), dcc=str(),
                    displayActiveKeyTangents=str(), dat=str(), displayActiveKeys=str(), dak=str(),
                    displayInfinities=str(), di=str(), displayKeys=str(), dk=str(), displayNormalized=bool(), dn=bool(),
                    displayTangents=str(), dtn=str(), displayValues=str(), dv=str(), docTag=str(), dtg=str(),
                    exists=bool(), ex=bool(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(),
                    highlightAffectedCurves=bool(), hac=bool(), highlightConnection=str(), hlc=str(),
                    keyMinScale=float(), kms=float(), keyScale=float(), ksc=float(), keyingTime=str(), kt=str(),
                    lockMainConnection=bool(), lck=bool(), lockPlayRangeShades=str(), lpr=str(), lookAt=str(), la=str(),
                    mainListConnection=str(), mlc=str(), menu=str(), m=str(), normalizeCurvesCommand=str(), ncc=str(),
                    outliner=str(), o=str(), panel=str(), pnl=str(), parent=str(), p=str(),
                    preSelectionHighlight=bool(), psh=bool(), renormalizeCurves=bool(), rnc=bool(),
                    resultSamples=float(), rs=float(), resultScreenSamples=int(), rss=int(), resultUpdate=str(),
                    ru=str(), selectionConnection=str(), slc=str(), showActiveCurveNames=bool(), acn=bool(),
                    showBufferCurves=str(), sb=str(), showCurveNames=bool(), scn=bool(), showPlayRangeShades=str(),
                    spr=str(), showResults=str(), sr=str(), showUpstreamCurves=bool(), suc=bool(), simpleKeyView=bool(),
                    skv=bool(), smoothness=str(), s=str(), snapTime=str(), st=str(), snapValue=str(), sv=str(),
                    stackedCurves=bool(), sc=bool(), stackedCurvesMax=float(), scx=float(), stackedCurvesMin=float(),
                    scm=float(), stackedCurvesSpace=float(), scs=float(), stateString=bool(), sts=bool(),
                    timelinePositionTop=bool(), tlp=bool(), unParent=bool(), up=bool(), unlockMainConnection=bool(),
                    ulk=bool(), updateMainConnection=bool(), upd=bool(), useTemplate=str(), ut=str(),
                    valueLinesToggle=str(), vlt=str(), *args, **kwargs):
    pass


def animDisplay(modelUpdate=str(), upd=str(), refAnimCurvesEditable=bool(), rae=bool(), timeCode=str(), tc=str(),
                timeCodeOffset=str(), tco=str(), *args, **kwargs):
    pass


def animLayer(addRelatedKG=bool(), akg=bool(), addSelectedObjects=bool(), aso=bool(), affectedLayers=bool(), afl=bool(),
              animCurves=bool(), anc=bool(), attribute=str(), at=str(), baseAnimCurves=bool(), bac=bool(),
              bestAnimLayer=bool(), blr=bool(), bestLayer=bool(), bl=bool(), blendNodes=bool(), bld=bool(),
              children=str(), c=str(), collapse=bool(), col=bool(), copy=str(), cp=str(), copyAnimation=str(), ca=str(),
              copyNoAnimation=str(), cna=str(), excludeBoolean=bool(), ebl=bool(), excludeDynamic=bool(), edn=bool(),
              excludeEnum=bool(), een=bool(), excludeRotate=bool(), ert=bool(), excludeScale=bool(), esc=bool(),
              excludeTranslate=bool(), etr=bool(), excludeVisibility=bool(), evs=bool(), exists=bool(), ex=bool(),
              extractAnimation=str(), ea=str(), findCurveForPlug=str(), fcv=str(), forceUIRebuild=bool(), fur=bool(),
              forceUIRefresh=bool(), uir=bool(), layeredPlug=str(), lp=str(), lock=bool(), l=bool(), maxLayers=bool(),
              ml=bool(), moveLayerAfter=str(), mva=str(), moveLayerBefore=str(), mvb=str(), mute=bool(), m=bool(),
              override=bool(), o=bool(), parent=str(), p=str(), passthrough=bool(), pth=bool(), preferred=bool(),
              prf=bool(), removeAllAttributes=bool(), raa=bool(), removeAttribute=str(), ra=str(), root=str(), r=str(),
              selected=bool(), sel=bool(), solo=bool(), s=bool(), weight=float(), w=float(),
              writeBlendnodeDestinations=bool(), wbd=bool(), *args, **kwargs):
    pass


def animView(endTime=float(), et=float(), maxValue=float(), max=float(), minValue=float(), min=float(), nextView=bool(),
             nv=bool(), previousView=bool(), pv=bool(), startTime=float(), st=float(), *args, **kwargs):
    pass


def annotate(point=list, p=list, text=str(), tx=str(), *args, **kwargs):
    pass


def appHome(instrument=str(), i=str(), setTab=str(), t=str(), toggleVisibility=bool(), tv=bool(),
            updateRecentFiles=bool(), urf=bool(), visible=bool(), v=bool(), *args, **kwargs):
    pass


def applyAttrPattern(nodeType=str(), nt=str(), patternName=str(), pn=str(), *args, **kwargs):
    pass


def applyMetadata(format=str(), fmt=str(), scene=bool(), scn=bool(), value=str(), v=str(), *args, **kwargs):
    pass


def applyTake(channel=str(), c=str(), device=str(), d=str(), filter=str(), f=str(), preview=bool(), p=bool(),
              recurseChannel=bool(), rc=bool(), reset=bool(), r=bool(), specifyChannel=bool(), sc=bool(),
              startTime=float(), st=float(), *args, **kwargs):
    pass


def arclen(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), nodeState=int(), nds=int(), *args,
           **kwargs):
    pass


def arcLenDimContext(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                     i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def arcLengthDimension(*args, **kwargs):
    pass


def arrayMapper(destAttr=str(), da=str(), inputU=str(), iu=str(), inputV=str(), iv=str(), mapTo=str(), mt=str(),
                target=str(), t=str(), type=str(), ty=str(), *args, **kwargs):
    pass


def art3dPaintCtx(accopacity=bool(), aco=bool(), afterStrokeCmd=str(), asc=str(), alphablendmode=str(), abm=str(),
                  assigntxt=bool(), ast=bool(), attrnames=str(), atn=str(), beforeStrokeCmd=str(), bsc=str(),
                  brushalignment=bool(), bra=bool(), brushdepth=float(), bd=float(), brushfeedback=bool(), brf=bool(),
                  brushtype=str(), brt=str(), clear=bool(), clr=bool(), commonattr=str(), cat=str(), dragSlider=str(),
                  dsl=str(), dynclonemode=bool(), dcm=bool(), exists=bool(), ex=bool(), expandfilename=bool(),
                  eef=bool(), extendFillColor=bool(), efc=bool(), fileformat=str(), eff=str(),
                  filetxtaspectratio=float(), far=float(), filetxtsizex=int(), ftx=int(), filetxtsizey=int(), fty=int(),
                  floodOpacity=float(), fop=float(), floodall=bool(), fal=bool(), floodselect=bool(), fsl=bool(),
                  history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                  keepaspectratio=bool(), kar=bool(), lastRecorderCmd=str(), lrc=str(), lastStampName=str(), lsn=str(),
                  lowerradius=float(), lr=float(), makeStroke=int(), mst=int(), mappressure=str(), mp=str(), name=str(),
                  n=str(), opacity=float(), op=float(), outline=bool(), o=bool(), outwhilepaint=bool(), owp=bool(),
                  paintmode=str(), pm=str(), paintoperationtype=str(), pot=str(), painttxtattr=str(), pta=str(),
                  painttxtattrname=str(), ptn=str(), pfxScale=float(), psc=float(), pfxWidth=float(), pwd=float(),
                  pickColor=bool(), pcm=bool(), pickValue=bool(), pv=bool(), playbackCursor=list, plc=list,
                  playbackPressure=float(), plp=float(), preserveclonesource=bool(), pcs=bool(), pressureMapping1=int(),
                  pm1=int(), pressureMapping2=int(), pm2=int(), pressureMapping3=int(), pm3=int(), pressureMax1=float(),
                  px1=float(), pressureMax2=float(), px2=float(), pressureMax3=float(), px3=float(),
                  pressureMin1=float(), ps1=float(), pressureMin2=float(), ps2=float(), pressureMin3=float(),
                  ps3=float(), profileShapeFile=str(), psf=str(), projective=bool(), prm=bool(), radius=float(),
                  r=float(), record=bool(), rec=bool(), reflection=bool(), rn=bool(), reflectionaboutorigin=bool(),
                  rno=bool(), reflectionaxis=str(), ra=str(), reloadtexfile=bool(), rtf=bool(), resizeratio=float(),
                  rr=float(), resizetxt=bool(), rft=bool(), rgbcolor=list, rgb=list, rgbflood=list, fc=list,
                  saveTextureOnStroke=bool(), sts=bool(), saveonstroke=bool(), sos=bool(), savetexture=bool(),
                  stx=bool(), screenRadius=float(), scR=float(), selectclonesource=bool(), scs=bool(),
                  shadernames=str(), hnm=str(), shapeattr=bool(), spa=bool(), shapenames=str(), shn=str(),
                  showactive=bool(), sa=bool(), soloAsDiffuse=bool(), sod=bool(), stampDepth=float(), stD=float(),
                  stampProfile=str(), stP=str(), stampSpacing=float(), stS=float(), strokesmooth=str(), ssm=str(),
                  surfaceConformedBrushVertices=bool(), scv=bool(), tablet=bool(), tab=bool(), tangentOutline=bool(),
                  to=bool(), textureFilenames=bool(), tfn=bool(), updateEraseTex=bool(), uet=bool(), usepressure=bool(),
                  up=bool(), worldRadius=float(), wlR=float(), *args, **kwargs):
    pass


def artAttrCtx(accopacity=bool(), aco=bool(), activeListChangedProc=str(), alp=str(), afterStrokeCmd=str(), asc=str(),
               alphaclamp=str(), alc=str(), alphaclamplower=float(), acl=float(), alphaclampupper=float(), acu=float(),
               attrSelected=str(), asl=str(), beforeStrokeCmd=str(), bsc=str(), brushalignment=bool(), bra=bool(),
               brushfeedback=bool(), brf=bool(), clamp=str(), cl=str(), clamplower=float(), cll=float(),
               clampupper=float(), clu=float(), clear=bool(), clr=bool(), colorAlphaValue=float(), cl1=float(),
               colorRGBAValue=list, cl4=list, colorRGBValue=list, cl3=list, colorRamp=str(), cr=str(),
               colorfeedback=bool(), cf=bool(), colorfeedbackOverride=bool(), cfo=bool(), colorrangelower=float(),
               crl=float(), colorrangeupper=float(), cru=float(), dataTypeIndex=int(), dti=int(),
               disablelighting=bool(), dl=bool(), dragSlider=str(), dsl=str(), duringStrokeCmd=str(), dsk=str(),
               dynclonemode=bool(), dcm=bool(), exists=bool(), ex=bool(), expandfilename=bool(), eef=bool(),
               exportaspectratio=float(), ear=float(), exportfilemode=str(), efm=str(), exportfilesave=str(), esf=str(),
               exportfilesizex=int(), fsx=int(), exportfilesizey=int(), fsy=int(), exportfiletype=str(), eft=str(),
               filterNodes=bool(), fon=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
               i2=str(), image3=str(), i3=str(), importfileload=str(), ifl=str(), importfilemode=str(), ifm=str(),
               importreassign=bool(), irm=bool(), interactiveUpdate=bool(), iu=bool(), lastRecorderCmd=str(), lrc=str(),
               lastStampName=str(), lsn=str(), lowerradius=float(), lr=float(), makeStroke=int(), mst=int(),
               mappressure=str(), mp=str(), maxvalue=float(), mxv=float(), minvalue=float(), miv=float(), name=str(),
               n=str(), objattrArray=str(), oaa=str(), opacity=float(), op=float(), outline=bool(), o=bool(),
               outwhilepaint=bool(), owp=bool(), paintNodeArray=str(), pna=str(), paintattrselected=str(), pas=str(),
               paintmode=str(), pm=str(), paintoperationtype=str(), pot=str(), pickColor=bool(), pcm=bool(),
               pickValue=bool(), pv=bool(), playbackCursor=list, plc=list, playbackPressure=float(), plp=float(),
               preserveclonesource=bool(), pcs=bool(), profileShapeFile=str(), psf=str(), projective=bool(), prm=bool(),
               radius=float(), r=float(), rampMaxColor=list, rxc=list, rampMinColor=list, rmc=list, record=bool(),
               rec=bool(), reflection=bool(), rn=bool(), reflectionaboutorigin=bool(), rno=bool(), reflectionaxis=str(),
               ra=str(), screenRadius=float(), scR=float(), selectclonesource=bool(), scs=bool(),
               selectedattroper=str(), sao=str(), showactive=bool(), sa=bool(), stampDepth=float(), stD=float(),
               stampProfile=str(), stP=str(), stampSpacing=float(), stS=float(), strokesmooth=str(), ssm=str(),
               surfaceConformedBrushVertices=bool(), scv=bool(), tablet=bool(), tab=bool(), tangentOutline=bool(),
               to=bool(), toolOffProc=str(), tfp=str(), toolOnProc=str(), top=str(), useColorRamp=bool(), ucr=bool(),
               useMaxMinColor=bool(), umc=bool(), usepressure=bool(), up=bool(), value=float(), val=float(),
               whichTool=str(), wst=str(), worldRadius=float(), wlR=float(), *args, **kwargs):
    pass


def artAttrPaintVertexCtx(accopacity=bool(), aco=bool(), activeListChangedProc=str(), alp=str(), afterStrokeCmd=str(),
                          asc=str(), alphaclamp=str(), alc=str(), alphaclamplower=float(), acl=float(),
                          alphaclampupper=float(), acu=float(), attrSelected=str(), asl=str(), beforeStrokeCmd=str(),
                          bsc=str(), brushalignment=bool(), bra=bool(), brushfeedback=bool(), brf=bool(), clamp=str(),
                          cl=str(), clamplower=float(), cll=float(), clampupper=float(), clu=float(), clear=bool(),
                          clr=bool(), colorAlphaValue=float(), cl1=float(), colorRGBAValue=list, cl4=list,
                          colorRGBValue=list, cl3=list, colorRamp=str(), cr=str(), colorfeedback=bool(), cf=bool(),
                          colorfeedbackOverride=bool(), cfo=bool(), colorrangelower=float(), crl=float(),
                          colorrangeupper=float(), cru=float(), dataTypeIndex=int(), dti=int(), disablelighting=bool(),
                          dl=bool(), dragSlider=str(), dsl=str(), duringStrokeCmd=str(), dsk=str(), dynclonemode=bool(),
                          dcm=bool(), exists=bool(), ex=bool(), expandfilename=bool(), eef=bool(),
                          exportaspectratio=float(), ear=float(), exportfilemode=str(), efm=str(), exportfilesave=str(),
                          esf=str(), exportfilesizex=int(), fsx=int(), exportfilesizey=int(), fsy=int(),
                          exportfiletype=str(), eft=str(), filterNodes=bool(), fon=bool(), history=bool(), ch=bool(),
                          image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), importfileload=str(),
                          ifl=str(), importfilemode=str(), ifm=str(), importreassign=bool(), irm=bool(),
                          interactiveUpdate=bool(), iu=bool(), lastRecorderCmd=str(), lrc=str(), lastStampName=str(),
                          lsn=str(), lowerradius=float(), lr=float(), makeStroke=int(), mst=int(), mappressure=str(),
                          mp=str(), maxvalue=float(), mxv=float(), minvalue=float(), miv=float(), name=str(), n=str(),
                          objattrArray=str(), oaa=str(), opacity=float(), op=float(), outline=bool(), o=bool(),
                          outwhilepaint=bool(), owp=bool(), paintComponent=int(), pc=int(), paintNodeArray=str(),
                          pna=str(), paintNumChannels=int(), pnc=int(), paintRGBA=bool(), pc4=bool(),
                          paintVertexFace=bool(), pvf=bool(), paintattrselected=str(), pas=str(), paintmode=str(),
                          pm=str(), paintoperationtype=str(), pot=str(), pickColor=bool(), pcm=bool(), pickValue=bool(),
                          pv=bool(), playbackCursor=list, plc=list, playbackPressure=float(), plp=float(),
                          preserveclonesource=bool(), pcs=bool(), profileShapeFile=str(), psf=str(), projective=bool(),
                          prm=bool(), radius=float(), r=float(), rampMaxColor=list, rxc=list, rampMinColor=list,
                          rmc=list, record=bool(), rec=bool(), reflection=bool(), rn=bool(),
                          reflectionaboutorigin=bool(), rno=bool(), reflectionaxis=str(), ra=str(),
                          screenRadius=float(), scR=float(), selectclonesource=bool(), scs=bool(),
                          selectedattroper=str(), sao=str(), showactive=bool(), sa=bool(), stampDepth=float(),
                          stD=float(), stampProfile=str(), stP=str(), stampSpacing=float(), stS=float(),
                          strokesmooth=str(), ssm=str(), surfaceConformedBrushVertices=bool(), scv=bool(),
                          tablet=bool(), tab=bool(), tangentOutline=bool(), to=bool(), toolOffProc=str(), tfp=str(),
                          toolOnProc=str(), top=str(), useColorRamp=bool(), ucr=bool(), useMaxMinColor=bool(),
                          umc=bool(), usepressure=bool(), up=bool(), value=float(), val=float(),
                          vertexColorRange=bool(), vcr=bool(), vertexColorRangeLower=float(), vcl=float(),
                          vertexColorRangeUpper=float(), vcu=float(), whichTool=str(), wst=str(), worldRadius=float(),
                          wlR=float(), *args, **kwargs):
    pass


def artAttrSkinPaintCtx(accopacity=bool(), aco=bool(), activeListChangedProc=str(), alp=str(), afterStrokeCmd=str(),
                        asc=str(), alphaclamp=str(), alc=str(), alphaclamplower=float(), acl=float(),
                        alphaclampupper=float(), acu=float(), attrSelected=str(), asl=str(), beforeStrokeCmd=str(),
                        bsc=str(), brushalignment=bool(), bra=bool(), brushfeedback=bool(), brf=bool(), clamp=str(),
                        cl=str(), clamplower=float(), cll=float(), clampupper=float(), clu=float(), clear=bool(),
                        clr=bool(), colorAlphaValue=float(), cl1=float(), colorRGBAValue=list, cl4=list,
                        colorRGBValue=list, cl3=list, colorRamp=str(), cr=str(), colorfeedback=bool(), cf=bool(),
                        colorfeedbackOverride=bool(), cfo=bool(), colorrangelower=float(), crl=float(),
                        colorrangeupper=float(), cru=float(), dataTypeIndex=int(), dti=int(), disablelighting=bool(),
                        dl=bool(), dragSlider=str(), dsl=str(), duringStrokeCmd=str(), dsk=str(), dynclonemode=bool(),
                        dcm=bool(), exists=bool(), ex=bool(), expandfilename=bool(), eef=bool(),
                        exportaspectratio=float(), ear=float(), exportfilemode=str(), efm=str(), exportfilesave=str(),
                        esf=str(), exportfilesizex=int(), fsx=int(), exportfilesizey=int(), fsy=int(),
                        exportfiletype=str(), eft=str(), filterNodes=bool(), fon=bool(), history=bool(), ch=bool(),
                        image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), importfileload=str(),
                        ifl=str(), importfilemode=str(), ifm=str(), importreassign=bool(), irm=bool(), influence=str(),
                        inf=str(), interactiveUpdate=bool(), iu=bool(), lastRecorderCmd=str(), lrc=str(),
                        lastStampName=str(), lsn=str(), lowerradius=float(), lr=float(), makeStroke=int(), mst=int(),
                        mappressure=str(), mp=str(), maxvalue=float(), mxv=float(), minvalue=float(), miv=float(),
                        name=str(), n=str(), objattrArray=str(), oaa=str(), opacity=float(), op=float(), outline=bool(),
                        o=bool(), outwhilepaint=bool(), owp=bool(), paintNodeArray=str(), pna=str(),
                        paintSelectMode=int(), psm=int(), paintattrselected=str(), pas=str(), paintmode=str(), pm=str(),
                        paintoperationtype=str(), pot=str(), pickColor=bool(), pcm=bool(), pickValue=bool(), pv=bool(),
                        playbackCursor=list, plc=list, playbackPressure=float(), plp=float(),
                        preserveclonesource=bool(), pcs=bool(), profileShapeFile=str(), psf=str(), projective=bool(),
                        prm=bool(), radius=float(), r=float(), rampMaxColor=list, rxc=list, rampMinColor=list, rmc=list,
                        record=bool(), rec=bool(), reflection=bool(), rn=bool(), reflectionaboutorigin=bool(),
                        rno=bool(), reflectionaxis=str(), ra=str(), screenRadius=float(), scR=float(),
                        selectclonesource=bool(), scs=bool(), selectedattroper=str(), sao=str(), showactive=bool(),
                        sa=bool(), skinPaintMode=int(), spm=int(), stampDepth=float(), stD=float(), stampProfile=str(),
                        stP=str(), stampSpacing=float(), stS=float(), strokesmooth=str(), ssm=str(),
                        surfaceConformedBrushVertices=bool(), scv=bool(), tablet=bool(), tab=bool(),
                        tangentOutline=bool(), to=bool(), toolOffProc=str(), tfp=str(), toolOnProc=str(), top=str(),
                        useColorRamp=bool(), ucr=bool(), useMaxMinColor=bool(), umc=bool(), usepressure=bool(),
                        up=bool(), value=float(), val=float(), whichTool=str(), wst=str(), worldRadius=float(),
                        wlR=float(), xrayJoints=bool(), xry=bool(), *args, **kwargs):
    pass


def artAttrTool(add=str(), exists=str(), ex=str(), remove=str(), rm=str(), *args, **kwargs):
    pass


def artBuildPaintMenu(*args, **kwargs):
    pass


def artFluidAttrCtx(accopacity=bool(), aco=bool(), activeListChangedProc=str(), alp=str(), afterStrokeCmd=str(),
                    asc=str(), alphaclamp=str(), alc=str(), alphaclamplower=float(), acl=float(),
                    alphaclampupper=float(), acu=float(), attrSelected=str(), asl=str(), autoSave=str(),
                    beforeStrokeCmd=str(), bsc=str(), brushalignment=bool(), bra=bool(), brushfeedback=bool(),
                    brf=bool(), clamp=str(), cl=str(), clamplower=float(), cll=float(), clampupper=float(), clu=float(),
                    clear=bool(), clr=bool(), colorAlphaValue=float(), cl1=float(), colorRGBAValue=list, cl4=list,
                    colorRGBValue=list, cl3=list, colorRamp=str(), cr=str(), colorfeedback=bool(), cf=bool(),
                    colorfeedbackOverride=bool(), cfo=bool(), colorrangelower=float(), crl=float(),
                    colorrangeupper=float(), cru=float(), currentPaintableFluid=str(), cpf=str(), dataTypeIndex=int(),
                    dti=int(), delaySelectionChanged=bool(), dsc=bool(), disablelighting=bool(), dl=bool(),
                    displayAsRender=bool(), dar=bool(), displayVelocity=bool(), dv=bool(), doAutoSave=bool(),
                    das=bool(), dragSlider=str(), dsl=str(), duringStrokeCmd=str(), dsk=str(), dynclonemode=bool(),
                    dcm=bool(), exists=bool(), ex=bool(), expandfilename=bool(), eef=bool(), exportaspectratio=float(),
                    ear=float(), exportfilemode=str(), efm=str(), exportfilesave=str(), esf=str(),
                    exportfilesizex=int(), fsx=int(), exportfilesizey=int(), fsy=int(), exportfiletype=str(), eft=str(),
                    filterNodes=bool(), fon=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                    i2=str(), image3=str(), i3=str(), importfileload=str(), ifl=str(), importfilemode=str(), ifm=str(),
                    importreassign=bool(), irm=bool(), interactiveUpdate=bool(), iu=bool(), lastRecorderCmd=str(),
                    lrc=str(), lastStampName=str(), lsn=str(), lowerradius=float(), lr=float(), makeStroke=int(),
                    mst=int(), mappressure=str(), mp=str(), maxvalue=float(), mxv=float(), minvalue=float(),
                    miv=float(), name=str(), n=str(), objattrArray=str(), oaa=str(), opacity=float(), op=float(),
                    outline=bool(), o=bool(), outwhilepaint=bool(), owp=bool(), paintNodeArray=str(), pna=str(),
                    paintattrselected=str(), pas=str(), paintmode=str(), pm=str(), paintoperationtype=str(), pot=str(),
                    pickColor=bool(), pcm=bool(), pickValue=bool(), pv=bool(), playbackCursor=list, plc=list,
                    playbackPressure=float(), plp=float(), preserveclonesource=bool(), pcs=bool(),
                    profileShapeFile=str(), psf=str(), projective=bool(), prm=bool(), property=str(), p=str(),
                    radius=float(), r=float(), rampMaxColor=list, rxc=list, rampMinColor=list, rmc=list, record=bool(),
                    rec=bool(), reflection=bool(), rn=bool(), reflectionaboutorigin=bool(), rno=bool(),
                    reflectionaxis=str(), ra=str(), rgbValue=list, rgb=list, screenRadius=float(), scR=float(),
                    selectclonesource=bool(), scs=bool(), selectedattroper=str(), sao=str(), showactive=bool(),
                    sa=bool(), stampDepth=float(), stD=float(), stampProfile=str(), stP=str(), stampSpacing=float(),
                    stS=float(), strokesmooth=str(), ssm=str(), surfaceConformedBrushVertices=bool(), scv=bool(),
                    tablet=bool(), tab=bool(), tangentOutline=bool(), to=bool(), toolOffProc=str(), tfp=str(),
                    toolOnProc=str(), top=str(), useColorRamp=bool(), ucr=bool(), useMaxMinColor=bool(), umc=bool(),
                    useStrokeDirection=bool(), usd=bool(), usepressure=bool(), up=bool(), value=float(), val=float(),
                    velocity=list, v=list, whichTool=str(), wst=str(), worldRadius=float(), wlR=float(), *args,
                    **kwargs):
    pass


def artPuttyCtx(accopacity=bool(), aco=bool(), activeListChangedProc=str(), alp=str(), afterStrokeCmd=str(), asc=str(),
                alphaclamp=str(), alc=str(), alphaclamplower=float(), acl=float(), alphaclampupper=float(), acu=float(),
                attrSelected=str(), asl=str(), autosmooth=bool(), asm=bool(), beforeStrokeCmd=str(), bsc=str(),
                brushStrength=float(), bs=float(), brushalignment=bool(), bra=bool(), brushfeedback=bool(), brf=bool(),
                clamp=str(), cl=str(), clamplower=float(), cll=float(), clampupper=float(), clu=float(), clear=bool(),
                clr=bool(), collapsecvtol=float(), clc=float(), colorAlphaValue=float(), cl1=float(),
                colorRGBAValue=list, cl4=list, colorRGBValue=list, cl3=list, colorRamp=str(), cr=str(),
                colorfeedback=bool(), cf=bool(), colorfeedbackOverride=bool(), cfo=bool(), colorrangelower=float(),
                crl=float(), colorrangeupper=float(), cru=float(), dataTypeIndex=int(), dti=int(),
                disablelighting=bool(), dl=bool(), dispdecr=bool(), dde=bool(), dispincr=bool(), din=bool(),
                dragSlider=str(), dsl=str(), duringStrokeCmd=str(), dsk=str(), dynclonemode=bool(), dcm=bool(),
                erasesrfupd=bool(), eut=bool(), exists=bool(), ex=bool(), expandfilename=bool(), eef=bool(),
                exportaspectratio=float(), ear=float(), exportfilemode=str(), efm=str(), exportfilesave=str(),
                esf=str(), exportfilesizex=int(), fsx=int(), exportfilesizey=int(), fsy=int(), exportfiletype=str(),
                eft=str(), filterNodes=bool(), fon=bool(), history=bool(), ch=bool(), image1=str(), i1=str(),
                image2=str(), i2=str(), image3=str(), i3=str(), importfileload=str(), ifl=str(), importfilemode=str(),
                ifm=str(), importreassign=bool(), irm=bool(), interactiveUpdate=bool(), iu=bool(),
                invertrefvector=bool(), irv=bool(), lastRecorderCmd=str(), lrc=str(), lastStampName=str(), lsn=str(),
                lowerradius=float(), lr=float(), makeStroke=int(), mst=int(), mappressure=str(), mp=str(),
                maxdisp=float(), md=float(), maxvalue=float(), mxv=float(), minvalue=float(), miv=float(),
                mouldtypehead=str(), mth=str(), mouldtypemouse=str(), mtm=str(), mouldtypetail=str(), mtt=str(),
                name=str(), n=str(), objattrArray=str(), oaa=str(), opacity=float(), op=float(), outline=bool(),
                o=bool(), outwhilepaint=bool(), owp=bool(), paintNodeArray=str(), pna=str(), paintattrselected=str(),
                pas=str(), paintmode=str(), pm=str(), paintoperationtype=str(), pot=str(), pickColor=bool(), pcm=bool(),
                pickValue=bool(), pv=bool(), playbackCursor=list, plc=list, playbackPressure=float(), plp=float(),
                polecv=bool(), pcv=bool(), preserveclonesource=bool(), pcs=bool(), profileShapeFile=str(), psf=str(),
                projective=bool(), prm=bool(), radius=float(), r=float(), rampMaxColor=list, rxc=list,
                rampMinColor=list, rmc=list, record=bool(), rec=bool(), reflection=bool(), rn=bool(),
                reflectionaboutorigin=bool(), rno=bool(), reflectionaxis=str(), ra=str(), refsurface=bool(), rs=bool(),
                refvector=str(), rv=str(), refvectoru=float(), rvu=float(), refvectorv=float(), rvv=float(),
                screenRadius=float(), scR=float(), selectclonesource=bool(), scs=bool(), selectedattroper=str(),
                sao=str(), showactive=bool(), sa=bool(), smoothiters=int(), si=int(), stampDepth=float(), stD=float(),
                stampProfile=str(), stP=str(), stampSpacing=float(), stS=float(), stitchcorner=bool(), stc=bool(),
                stitchedgeflood=bool(), sef=bool(), stitchtype=str(), stt=str(), strokesmooth=str(), ssm=str(),
                surfaceConformedBrushVertices=bool(), scv=bool(), tablet=bool(), tab=bool(), tangentOutline=bool(),
                to=bool(), toolOffProc=str(), tfp=str(), toolOnProc=str(), top=str(), updateerasesrf=bool(), ues=bool(),
                updaterefsrf=bool(), urs=bool(), useColorRamp=bool(), ucr=bool(), useMaxMinColor=bool(), umc=bool(),
                usepressure=bool(), up=bool(), value=float(), val=float(), whichTool=str(), wst=str(),
                worldRadius=float(), wlR=float(), *args, **kwargs):
    pass


def artSelectCtx(accopacity=bool(), aco=bool(), addselection=bool(), ads=bool(), afterStrokeCmd=str(), asc=str(),
                 beforeStrokeCmd=str(), bsc=str(), brushalignment=bool(), bra=bool(), brushfeedback=bool(), brf=bool(),
                 clear=bool(), clr=bool(), dragSlider=str(), dsl=str(), dynclonemode=bool(), dcm=bool(), exists=bool(),
                 ex=bool(), expandfilename=bool(), eef=bool(), exportaspectratio=float(), ear=float(),
                 exportfilemode=str(), efm=str(), exportfilesave=str(), esf=str(), exportfilesizex=int(), fsx=int(),
                 exportfilesizey=int(), fsy=int(), exportfiletype=str(), eft=str(), history=bool(), ch=bool(),
                 image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), importfileload=str(),
                 ifl=str(), importfilemode=str(), ifm=str(), importreassign=bool(), irm=bool(), importthreshold=float(),
                 ift=float(), lastRecorderCmd=str(), lrc=str(), lastStampName=str(), lsn=str(), lowerradius=float(),
                 lr=float(), makeStroke=int(), mst=int(), mappressure=str(), mp=str(), name=str(), n=str(),
                 opacity=float(), op=float(), outline=bool(), o=bool(), outwhilepaint=bool(), owp=bool(),
                 paintmode=str(), pm=str(), paintoperationtype=str(), pot=str(), pickColor=bool(), pcm=bool(),
                 pickValue=bool(), pv=bool(), playbackCursor=list, plc=list, playbackPressure=float(), plp=float(),
                 preserveclonesource=bool(), pcs=bool(), profileShapeFile=str(), psf=str(), projective=bool(),
                 prm=bool(), radius=float(), r=float(), record=bool(), rec=bool(), reflection=bool(), rn=bool(),
                 reflectionaboutorigin=bool(), rno=bool(), reflectionaxis=str(), ra=str(), screenRadius=float(),
                 scR=float(), selectall=bool(), sal=bool(), selectclonesource=bool(), scs=bool(), selectop=str(),
                 sop=str(), showactive=bool(), sa=bool(), stampDepth=float(), stD=float(), stampProfile=str(),
                 stP=str(), stampSpacing=float(), stS=float(), strokesmooth=str(), ssm=str(),
                 surfaceConformedBrushVertices=bool(), scv=bool(), tablet=bool(), tab=bool(), tangentOutline=bool(),
                 to=bool(), toggleall=bool(), tal=bool(), unselectall=bool(), ual=bool(), usepressure=bool(), up=bool(),
                 worldRadius=float(), wlR=float(), *args, **kwargs):
    pass


def artSetPaintCtx(accopacity=bool(), aco=bool(), afterStrokeCmd=str(), asc=str(), beforeStrokeCmd=str(), bsc=str(),
                   brushalignment=bool(), bra=bool(), brushfeedback=bool(), brf=bool(), clear=bool(), clr=bool(),
                   dragSlider=str(), dsl=str(), dynclonemode=bool(), dcm=bool(), exists=bool(), ex=bool(),
                   expandfilename=bool(), eef=bool(), exportaspectratio=float(), ear=float(), exportfilemode=str(),
                   efm=str(), exportfilesave=str(), esf=str(), exportfilesizex=int(), fsx=int(), exportfilesizey=int(),
                   fsy=int(), exportfiletype=str(), eft=str(), history=bool(), ch=bool(), image1=str(), i1=str(),
                   image2=str(), i2=str(), image3=str(), i3=str(), importfileload=str(), ifl=str(),
                   importfilemode=str(), ifm=str(), importreassign=bool(), irm=bool(), lastRecorderCmd=str(), lrc=str(),
                   lastStampName=str(), lsn=str(), lowerradius=float(), lr=float(), makeStroke=int(), mst=int(),
                   mappressure=str(), mp=str(), name=str(), n=str(), objectsetnames=str(), osn=str(), opacity=float(),
                   op=float(), outline=bool(), o=bool(), outwhilepaint=bool(), owp=bool(), paintmode=str(), pm=str(),
                   paintoperationtype=str(), pot=str(), pickColor=bool(), pcm=bool(), pickValue=bool(), pv=bool(),
                   playbackCursor=list, plc=list, playbackPressure=float(), plp=float(), preserveclonesource=bool(),
                   pcs=bool(), profileShapeFile=str(), psf=str(), projective=bool(), prm=bool(), radius=float(),
                   r=float(), record=bool(), rec=bool(), reflection=bool(), rn=bool(), reflectionaboutorigin=bool(),
                   rno=bool(), reflectionaxis=str(), ra=str(), screenRadius=float(), scR=float(),
                   selectclonesource=bool(), scs=bool(), setcolorfeedback=bool(), scf=bool(), setdisplaycvs=bool(),
                   dcv=bool(), setopertype=str(), sot=str(), settomodify=str(), stm=str(), showactive=bool(), sa=bool(),
                   stampDepth=float(), stD=float(), stampProfile=str(), stP=str(), stampSpacing=float(), stS=float(),
                   strokesmooth=str(), ssm=str(), surfaceConformedBrushVertices=bool(), scv=bool(), tablet=bool(),
                   tab=bool(), tangentOutline=bool(), to=bool(), usepressure=bool(), up=bool(), worldRadius=float(),
                   wlR=float(), *args, **kwargs):
    pass


def artUserPaintCtx(accopacity=bool(), aco=bool(), activeListChangedProc=str(), alp=str(), afterStrokeCmd=str(),
                    asc=str(), alphaclamp=str(), alc=str(), alphaclamplower=float(), acl=float(),
                    alphaclampupper=float(), acu=float(), attrSelected=str(), asl=str(), beforeStrokeCmd=str(),
                    bsc=str(), brushalignment=bool(), bra=bool(), brushfeedback=bool(), brf=bool(), chunkCommand=str(),
                    cc=str(), clamp=str(), cl=str(), clamplower=float(), cll=float(), clampupper=float(), clu=float(),
                    clear=bool(), clr=bool(), colorAlphaValue=float(), cl1=float(), colorRGBAValue=list, cl4=list,
                    colorRGBValue=list, cl3=list, colorRamp=str(), cr=str(), colorfeedback=bool(), cf=bool(),
                    colorfeedbackOverride=bool(), cfo=bool(), colorrangelower=float(), crl=float(),
                    colorrangeupper=float(), cru=float(), dataTypeIndex=int(), dti=int(), disablelighting=bool(),
                    dl=bool(), dragSlider=str(), dsl=str(), duringStrokeCmd=str(), dsk=str(), dynclonemode=bool(),
                    dcm=bool(), exists=bool(), ex=bool(), expandfilename=bool(), eef=bool(), exportaspectratio=float(),
                    ear=float(), exportfilemode=str(), efm=str(), exportfilesave=str(), esf=str(),
                    exportfilesizex=int(), fsx=int(), exportfilesizey=int(), fsy=int(), exportfiletype=str(), eft=str(),
                    filterNodes=bool(), fon=bool(), finalizeCmd=str(), fc=str(), fullpaths=bool(), fp=bool(),
                    getArrayAttrCommand=str(), gac=str(), getSurfaceCommand=str(), gsc=str(), getValueCommand=str(),
                    gvc=str(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(),
                    i3=str(), importfileload=str(), ifl=str(), importfilemode=str(), ifm=str(), importreassign=bool(),
                    irm=bool(), initializeCmd=str(), ic=str(), interactiveUpdate=bool(), iu=bool(),
                    lastRecorderCmd=str(), lrc=str(), lastStampName=str(), lsn=str(), lowerradius=float(), lr=float(),
                    makeStroke=int(), mst=int(), mappressure=str(), mp=str(), maxvalue=float(), mxv=float(),
                    minvalue=float(), miv=float(), name=str(), n=str(), objattrArray=str(), oaa=str(), opacity=float(),
                    op=float(), outline=bool(), o=bool(), outwhilepaint=bool(), owp=bool(), paintNodeArray=str(),
                    pna=str(), paintattrselected=str(), pas=str(), paintmode=str(), pm=str(), paintoperationtype=str(),
                    pot=str(), pickColor=bool(), pcm=bool(), pickValue=bool(), pv=bool(), playbackCursor=list, plc=list,
                    playbackPressure=float(), plp=float(), preserveclonesource=bool(), pcs=bool(),
                    profileShapeFile=str(), psf=str(), projective=bool(), prm=bool(), radius=float(), r=float(),
                    rampMaxColor=list, rxc=list, rampMinColor=list, rmc=list, record=bool(), rec=bool(),
                    reflection=bool(), rn=bool(), reflectionaboutorigin=bool(), rno=bool(), reflectionaxis=str(),
                    ra=str(), screenRadius=float(), scR=float(), selectclonesource=bool(), scs=bool(),
                    selectedattroper=str(), sao=str(), setArrayValueCommand=str(), sac=str(), setValueCommand=str(),
                    svc=str(), showactive=bool(), sa=bool(), stampDepth=float(), stD=float(), stampProfile=str(),
                    stP=str(), stampSpacing=float(), stS=float(), strokesmooth=str(), ssm=str(),
                    surfaceConformedBrushVertices=bool(), scv=bool(), tablet=bool(), tab=bool(), tangentOutline=bool(),
                    to=bool(), toolCleanupCmd=str(), tcc=str(), toolOffProc=str(), tfp=str(), toolOnProc=str(),
                    top=str(), toolSetupCmd=str(), tsc=str(), useColorRamp=bool(), ucr=bool(), useMaxMinColor=bool(),
                    umc=bool(), usepressure=bool(), up=bool(), value=float(), val=float(), whichTool=str(), wst=str(),
                    worldRadius=float(), wlR=float(), *args, **kwargs):
    pass


def arubaNurbsToPoly(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), localSpace=bool(), ls=bool(),
                     name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), worldSpace=bool(),
                     ws=bool(), *args, **kwargs):
    pass


def assembly(active=str(), a=str(), activeLabel=str(), al=str(), canCreate=str(), cc=str(), createOptionBoxProc=str(),
             cob=str(), createRepresentation=str(), cr=str(), defaultType=str(), dt=str(), deleteRepresentation=str(),
             dr=str(), deregister=str(), d=str(), input=str(), isAType=str(), isa=str(), isTrackingMemberEdits=str(),
             ite=str(), label=str(), lbl=str(), listRepTypes=bool(), lrt=bool(), listRepTypesProc=str(), lrp=str(),
             listRepresentations=bool(), lr=bool(), listTypes=bool(), lt=bool(), name=str(), n=str(), newRepLabel=str(),
             nrl=str(), postCreateUIProc=str(), aoc=str(), proc=str(), prc=str(), renameRepresentation=str(), rnr=str(),
             repLabel=str(), rl=str(), repName=str(), rnm=str(), repNamespace=str(), rns=str(),
             repPostCreateUIProc=str(), poc=str(), repPreCreateUIProc=str(), pec=str(), repType=str(), rt=str(),
             repTypeLabel=str(), rtl=str(), repTypeLabelProc=str(), rtp=str(), type=str(), typ=str(), *args, **kwargs):
    pass


def assignCommand(addDivider=str(), ad=str(), altModifier=bool(), alt=bool(), annotation=str(), ann=str(),
                  command=str(), c=str(), commandModifier=bool(), cmd=bool(), ctrlModifier=bool(), ctl=bool(),
                  data1=str(), da1=str(), data2=str(), da2=str(), data3=str(), da3=str(), delete=int(), d=int(),
                  dividerString=str(), ds=str(), enableCommandRepeat=bool(), ecr=bool(), factorySettings=bool(),
                  fs=bool(), index=int(), i=int(), keyArray=bool(), ka=bool(), keyString=str(), k=str(), keyUp=bool(),
                  kup=bool(), name=bool(), n=bool(), numDividersPreceding=int(), ndp=int(), numElements=bool(),
                  num=bool(), optionModifier=bool(), opt=bool(), sortByKey=bool(), sbk=bool(),
                  sourceUserCommands=bool(), suc=bool(), *args, **kwargs):
    pass


def assignInputDevice(clutch=str(), c=str(), continuous=bool(), ct=bool(), device=str(), d=str(), immediate=bool(),
                      im=bool(), multiple=bool(), m=bool(), *args, **kwargs):
    pass


def assignViewportFactories(materialFactory=str(), mf=str(), nodeType=str(), nt=str(), textureFactory=str(), tf=str(),
                            *args, **kwargs):
    pass


def attachCurve(blendBias=float(), bb=float(), blendKnotInsertion=bool(), bki=bool(), caching=bool(), cch=bool(),
                constructionHistory=bool(), ch=bool(), keepMultipleKnots=bool(), kmk=bool(), method=int(), m=int(),
                name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), parameter=float(), p=float(),
                replaceOriginal=bool(), rpo=bool(), reverse1=bool(), rv1=bool(), reverse2=bool(), rv2=bool(), *args,
                **kwargs):
    pass


def attachDeviceAttr(attribute=str(), at=str(), axis=str(), ax=str(), camera=bool(), cam=bool(), cameraRotate=bool(),
                     cr=bool(), cameraTranslate=bool(), ct=bool(), clutch=str(), c=str(), device=str(), d=str(),
                     selection=bool(), sl=bool(), *args, **kwargs):
    pass


def attachSurface(blendBias=float(), bb=float(), blendKnotInsertion=bool(), bki=bool(), caching=bool(), cch=bool(),
                  constructionHistory=bool(), ch=bool(), directionU=bool(), du=bool(), keepMultipleKnots=bool(),
                  kmk=bool(), method=int(), m=int(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(),
                  o=bool(), parameter=float(), p=float(), replaceOriginal=bool(), rpo=bool(), reverse1=bool(),
                  rv1=bool(), reverse2=bool(), rv2=bool(), swap1=bool(), sw1=bool(), swap2=bool(), sw2=bool(),
                  twist=bool(), tw=bool(), *args, **kwargs):
    pass


def attrColorSliderGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                       ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                       adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), attrNavDecision=list,
                       attribute=str(), at=str(), backgroundColor=list, bgc=list, columnAlign=list, cal=list,
                       columnAlign2=list, cl2=list, columnAlign3=list, cl3=list, columnAlign4=list, cl4=list,
                       columnAlign5=list, cl5=list, columnAlign6=list, cl6=list, columnAttach=list, cat=list,
                       columnAttach2=list, ct2=list, columnAttach3=list, ct3=list, columnAttach4=list, ct4=list,
                       columnAttach5=list, ct5=list, columnAttach6=list, ct6=list, columnOffset2=list, co2=list,
                       columnOffset3=list, co3=list, columnOffset4=list, co4=list, columnOffset5=list, co5=list,
                       columnOffset6=list, co6=list, columnWidth=list, cw=list, columnWidth1=int(), cw1=int(),
                       columnWidth2=list, cw2=list, columnWidth3=list, cw3=list, columnWidth4=list, cw4=list,
                       columnWidth5=list, cw5=list, columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(),
                       docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
                       enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                       ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                       highlightColor=list, hlc=list, hsvValue=list, hsv=list, isObscured=bool(), io=bool(),
                       label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                       numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                       preventOverride=bool(), po=bool(), rgbValue=list, rgb=list, rowAttach=list, rat=list,
                       showButton=bool(), sb=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
                       visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                       **kwargs):
    pass


def attrControlGrp(annotation=str(), ann=str(), attribute=str(), a=str(), changeCommand=str(), cc=str(), enable=bool(),
                   en=bool(), exists=bool(), ex=bool(), handlesAttribute=str(), ha=str(), hideMapButton=bool(),
                   hmb=bool(), label=str(), l=str(), preventOverride=bool(), po=bool(), *args, **kwargs):
    pass


def attrEnumOptionMenu(annotation=str(), ann=str(), attribute=str(), at=str(), backgroundColor=list, bgc=list,
                       changeCommand=str(), cc=str(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                       dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                       enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), enumeratedItem=list,
                       ei=list, exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                       highlightColor=list, hlc=list, isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(),
                       m=bool(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(),
                       p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
                       statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                       visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def attrEnumOptionMenuGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(),
                          adjustableColumn3=int(), ad3=int(), adjustableColumn4=int(), ad4=int(),
                          adjustableColumn5=int(), ad5=int(), adjustableColumn6=int(), ad6=int(), annotation=str(),
                          ann=str(), attribute=str(), at=str(), backgroundColor=list, bgc=list, columnAlign=list,
                          cal=list, columnAlign2=list, cl2=list, columnAlign3=list, cl3=list, columnAlign4=list,
                          cl4=list, columnAlign5=list, cl5=list, columnAlign6=list, cl6=list, columnAttach=list,
                          cat=list, columnAttach2=list, ct2=list, columnAttach3=list, ct3=list, columnAttach4=list,
                          ct4=list, columnAttach5=list, ct5=list, columnAttach6=list, ct6=list, columnOffset2=list,
                          co2=list, columnOffset3=list, co3=list, columnOffset4=list, co4=list, columnOffset5=list,
                          co5=list, columnOffset6=list, co6=list, columnWidth=list, cw=list, columnWidth1=int(),
                          cw1=int(), columnWidth2=list, cw2=list, columnWidth3=list, cw3=list, columnWidth4=list,
                          cw4=list, columnWidth5=list, cw5=list, columnWidth6=list, cw6=list, defineTemplate=str(),
                          dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(),
                          dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                          enableKeyboardFocus=bool(), ekf=bool(), enumeratedItem=list, ei=list, exists=bool(),
                          ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list,
                          hlc=list, isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(), m=bool(),
                          noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                          popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rowAttach=list,
                          rat=list, statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(),
                          vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def attrFieldGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                 ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                 adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), attribute=str(), at=str(),
                 backgroundColor=list, bgc=list, changeCommand=str(), cc=str(), columnAlign=list, cal=list,
                 columnAlign2=list, cl2=list, columnAlign3=list, cl3=list, columnAlign4=list, cl4=list,
                 columnAlign5=list, cl5=list, columnAlign6=list, cl6=list, columnAttach=list, cat=list,
                 columnAttach2=list, ct2=list, columnAttach3=list, ct3=list, columnAttach4=list, ct4=list,
                 columnAttach5=list, ct5=list, columnAttach6=list, ct6=list, columnOffset2=list, co2=list,
                 columnOffset3=list, co3=list, columnOffset4=list, co4=list, columnOffset5=list, co5=list,
                 columnOffset6=list, co6=list, columnWidth=list, cw=list, columnWidth1=int(), cw1=int(),
                 columnWidth2=list, cw2=list, columnWidth3=list, cw3=list, columnWidth4=list, cw4=list,
                 columnWidth5=list, cw5=list, columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(),
                 dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                 enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
                 extraButton=bool(), eb=bool(), extraButtonCommand=str(), ebc=str(), extraButtonIcon=str(), ebi=str(),
                 extraLabel=str(), el=str(), forceAddMapButton=bool(), fmb=bool(), fullPathName=bool(), fpn=bool(),
                 height=int(), h=int(), hideMapButton=bool(), hmb=bool(), highlightColor=list, hlc=list,
                 isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(), m=bool(), maxValue=float(),
                 max=float(), minValue=float(), min=float(), noBackground=bool(), nbg=bool(), numberOfFields=int(),
                 nf=int(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(),
                 pma=bool(), precision=int(), pre=int(), preventOverride=bool(), po=bool(), rowAttach=list, rat=list,
                 statusBarMessage=str(), sbm=str(), step=float(), s=float(), useTemplate=str(), ut=str(),
                 visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                 **kwargs):
    pass


def attrFieldSliderGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                       ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                       adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), attribute=str(), at=str(),
                       backgroundColor=list, bgc=list, changeCommand=str(), cc=str(), columnAlign=list, cal=list,
                       columnAlign2=list, cl2=list, columnAlign3=list, cl3=list, columnAlign4=list, cl4=list,
                       columnAlign5=list, cl5=list, columnAlign6=list, cl6=list, columnAttach=list, cat=list,
                       columnAttach2=list, ct2=list, columnAttach3=list, ct3=list, columnAttach4=list, ct4=list,
                       columnAttach5=list, ct5=list, columnAttach6=list, ct6=list, columnOffset2=list, co2=list,
                       columnOffset3=list, co3=list, columnOffset4=list, co4=list, columnOffset5=list, co5=list,
                       columnOffset6=list, co6=list, columnWidth=list, cw=list, columnWidth1=int(), cw1=int(),
                       columnWidth2=list, cw2=list, columnWidth3=list, cw3=list, columnWidth4=list, cw4=list,
                       columnWidth5=list, cw5=list, columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(),
                       docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
                       enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                       ekf=bool(), exists=bool(), ex=bool(), extraButton=bool(), eb=bool(), extraButtonCommand=str(),
                       ebc=str(), extraButtonIcon=str(), ebi=str(), fieldMaxValue=float(), fmx=float(),
                       fieldMinValue=float(), fmn=float(), fieldStep=float(), fs=float(), forceAddMapButton=bool(),
                       fmb=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), hideMapButton=bool(),
                       hmb=bool(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(), label=str(), l=str(),
                       manage=bool(), m=bool(), maxValue=float(), max=float(), minValue=float(), min=float(),
                       noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                       popupMenuArray=bool(), pma=bool(), precision=int(), pre=int(), preventOverride=bool(), po=bool(),
                       rowAttach=list, rat=list, sliderMaxValue=float(), smx=float(), sliderMinValue=float(),
                       smn=float(), sliderStep=float(), ss=float(), statusBarMessage=str(), sbm=str(), step=float(),
                       s=float(), useTemplate=str(), ut=str(), vertical=bool(), vr=bool(), visible=bool(), vis=bool(),
                       visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def attributeInfo(allAttributes=bool(), all=bool(), bool=bool(), b=bool(), enumerated=bool(), e=bool(), hidden=bool(),
                  h=bool(), inherited=bool(), internal=bool(), i=bool(), leaf=bool(), l=bool(), logicalAnd=bool(),
                  multi=bool(), m=bool(), short=bool(), s=bool(), type=str(), t=str(), userInterface=bool(), ui=bool(),
                  writable=bool(), w=bool(), *args, **kwargs):
    pass


def attributeMenu(beginMenu=bool(), beg=bool(), editor=str(), edt=str(), finishMenu=bool(), fsh=bool(), inputs=bool(),
                  inp=bool(), plug=str(), p=str(), regPulldownMenuCommand=str(), rpm=str(),
                  unregPulldownMenuCommand=int(), upm=int(), *args, **kwargs):
    pass


def attributeName(attr_name, leaf=bool(), lf=bool(), long: bool=None, l: bool=None, nice: bool=None, n: bool=None,
                  short: bool=None, s: bool=None):
    if not attr_name:
        raise RuntimeError("attr_name is required")
    
    if sum([long or 0, l or 0, nice or 0, n or 0, short or 0, s or 0]) > 1:
        raise ValueError("Only one of long, nice, or short can be True")
    
    use_long = any((long or l, not (short or s)))
    
    _, plug = _attr_name_to_mobject_and_plug(attr_name)
    plug_name = plug.partialName(
        useLongNames=use_long,
        includeNodeName=False,
    )
    if nice:
        return re.sub(
            r"((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))",
            r" \1", plug_name
        ).title().replace("  ", " ").replace("_", " ")
    return plug_name


def attributeQuery(affectsAppearance=bool(), aa=bool(), affectsWorldspace=bool(), aws=bool(), attributeType=bool(),
                   at=bool(), cachedInternally=bool(), ci=bool(), categories=bool(), ct=bool(), channelBox=bool(),
                   ch=bool(), connectable=bool(), c=bool(), enum=bool(), e=bool(), exists=bool(), ex=bool(),
                   hidden=bool(), h=bool(), indeterminant=bool(), idt=bool(), indexMatters=bool(), im=bool(),
                   internal=bool(), i=bool(), internalGet=bool(), ig=bool(), internalSet=bool(), keyable=bool(),
                   k=bool(), listChildren=bool(), lc=bool(), listDefault=bool(), ld=bool(), listEnum=bool(), le=bool(),
                   listParent=bool(), lp=bool(), listSiblings=bool(), ls=bool(), localizedListEnum=bool(), lz=bool(),
                   longName=bool(), ln=bool(), maxExists=bool(), mxe=bool(), maximum=bool(), max=bool(), message=bool(),
                   msg=bool(), minExists=bool(), mne=bool(), minimum=bool(), min=bool(), multi=bool(), m=bool(),
                   niceName=bool(), nn=bool(), node=str(), n=str(), numberOfChildren=bool(), nc=bool(), range=bool(),
                   r=bool(), rangeExists=bool(), re=bool(), readable=bool(), rd=bool(), renderSource=bool(), rs=bool(),
                   shortName=bool(), sn=bool(), softMax=bool(), smx=bool(), softMaxExists=bool(), sxe=bool(),
                   softMin=bool(), smn=bool(), softMinExists=bool(), sme=bool(), softRange=bool(), s=bool(),
                   softRangeExists=bool(), se=bool(), storable=bool(), st=bool(), type=str(), typ=str(),
                   typeExact=str(), tex=str(), usedAsColor=bool(), uac=bool(), usedAsFilename=bool(), uaf=bool(),
                   usesMultiBuilder=bool(), umb=bool(), worldspace=bool(), ws=bool(), writable=bool(), w=bool(), *args,
                   **kwargs):
    pass


def attrNavigationControlGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(),
                             adjustableColumn3=int(), ad3=int(), adjustableColumn4=int(), ad4=int(),
                             adjustableColumn5=int(), ad5=int(), adjustableColumn6=int(), ad6=int(), annotation=str(),
                             ann=str(), attrNavDecision=list, attribute=str(), at=str(), backgroundColor=list, bgc=list,
                             columnAlign=list, cal=list, columnAlign2=list, cl2=list, columnAlign3=list, cl3=list,
                             columnAlign4=list, cl4=list, columnAlign5=list, cl5=list, columnAlign6=list, cl6=list,
                             columnAttach=list, cat=list, columnAttach2=list, ct2=list, columnAttach3=list, ct3=list,
                             columnAttach4=list, ct4=list, columnAttach5=list, ct5=list, columnAttach6=list, ct6=list,
                             columnOffset2=list, co2=list, columnOffset3=list, co3=list, columnOffset4=list, co4=list,
                             columnOffset5=list, co5=list, columnOffset6=list, co6=list, columnWidth=list, cw=list,
                             columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list, columnWidth3=list, cw3=list,
                             columnWidth4=list, cw4=list, columnWidth5=list, cw5=list, columnWidth6=list, cw6=list,
                             connectAttrToDropped=str(), cad=str(), connectNodeToDropped=str(), cnd=str(),
                             connectToExisting=str(), ce=str(), createNew=str(), cn=str(), defaultTraversal=str(),
                             dtv=str(), defineTemplate=str(), dt=str(), delete=str(), disconnect=str(), d=str(),
                             docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
                             enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                             ekf=bool(), exists=bool(), ex=bool(), extraButton=bool(), eb=bool(),
                             extraButtonCommand=str(), ebc=str(), extraButtonIcon=str(), ebi=str(), fullPathName=bool(),
                             fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, ignore=str(), i=str(),
                             ignoreNotSupported=bool(), ins=bool(), isObscured=bool(), io=bool(), label=str(), l=str(),
                             manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), noIgnorableMenu=bool(),
                             nim=bool(), noKeyableMenu=bool(), nkm=bool(), numberOfPopupMenus=bool(), npm=bool(),
                             parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(),
                             po=bool(), relatedNodes=str(), ren=str(), rowAttach=list, rat=list, statusBarMessage=str(),
                             sbm=str(), unignore=str(), u=str(), useTemplate=str(), ut=str(), visible=bool(),
                             vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def audioTrack(insertTrack=int(), it=int(), lock=bool(), l=bool(), mute=bool(), m=bool(), numTracks=int(), nt=int(),
               removeEmptyTracks=bool(), ret=bool(), removeTrack=int(), rt=int(), solo=bool(), so=bool(),
               swapTracks=list, st=list, title=str(), t=str(), track=int(), tr=int(), *args, **kwargs):
    pass


def autoKeyframe(addAttr=str(), aa=str(), characterOption=str(), co=str(), listAttr=bool(), lsa=bool(), noReset=bool(),
                 nr=bool(), state=bool(), st=bool(), *args, **kwargs):
    pass


def autoPlace(useMouse=bool(), um=bool(), *args, **kwargs):
    pass


def autoSave(destination=int(), dst=int(), destinationFolder=bool(), df=bool(), enable=bool(), en=bool(), folder=str(),
             fol=str(), interval=float(), int=float(), limitBackups=bool(), lim=bool(), maxBackups=int(), max=int(),
             perform=bool(), p=bool(), prompt=bool(), prm=bool(), *args, **kwargs):
    pass


def backgroundEvaluationManager(interrupt=bool(), i=bool(), mode=str(), m=str(), pause=bool(), p=bool(), resume=bool(),
                                r=bool(), *args, **kwargs):
    pass


def bakeClip(blend=list, b=list, clipIndex=int(), ci=int(), keepOriginals=bool(), k=bool(), name=str(), n=str(), *args,
             **kwargs):
    pass


def bakeDeformer(colorizeSkeleton=bool(), cs=bool(), customRangeOfMotion=tuple(), rom=tuple(), dstMeshName=str(),
                 dm=str(), dstSkeletonName=str(), ds=str(), hierarchy=bool(), hi=bool(), influences=list, i=list,
                 maxInfluences=int(), mi=int(), pruneWeights=float(), pw=float(), smoothWeights=int(), sw=int(),
                 srcMeshName=str(), sm=str(), srcSkeletonName=str(), ss=str(), *args, **kwargs):
    pass


def bakePartialHistory(allShapes=bool(), all=bool(), postSmooth=bool(), nps=bool(), preCache=bool(), pc=bool(),
                       preDeformers=bool(), pre=bool(), prePostDeformers=bool(), ppt=bool(), *args, **kwargs):
    pass


def bakeResults(animation=str(), an=str(), attribute=str(), at=str(), bakeOnOverrideLayer=bool(), bol=bool(),
                controlPoints=bool(), cp=bool(), destinationLayer=str(), dl=str(), disableImplicitControl=bool(),
                dic=bool(), float=tuple(), f=tuple(), hierarchy=str(), hi=str(), includeUpperBound=bool(), iub=bool(),
                index=int(), minimizeRotation=bool(), mr=bool(), oversamplingRate=int(), osr=int(),
                preserveOutsideKeys=bool(), pok=bool(), removeBakedAnimFromLayer=bool(), rba=bool(),
                removeBakedAttributeFromLayer=bool(), ral=bool(), resolveWithoutLayer=str(), rwl=str(),
                sampleBy=float(), sb=float(), shape=bool(), s=bool(), simulation=bool(), sm=bool(), smart=list, sr=list,
                sparseAnimCurveBake=bool(), sac=bool(), time=tuple(), t=tuple(), *args, **kwargs):
    pass


def bakeSimulation(animation=str(), an=str(), attribute=str(), at=str(), bakeOnOverrideLayer=bool(), bol=bool(),
                   controlPoints=bool(), cp=bool(), destinationLayer=str(), dl=str(), disableImplicitControl=bool(),
                   dic=bool(), float=tuple(), f=tuple(), hierarchy=str(), hi=str(), includeUpperBound=bool(),
                   iub=bool(), index=int(), minimizeRotation=bool(), mr=bool(), preserveOutsideKeys=bool(), pok=bool(),
                   removeBakedAnimFromLayer=bool(), rba=bool(), removeBakedAttributeFromLayer=bool(), ral=bool(),
                   resolveWithoutLayer=str(), rwl=str(), sampleBy=float(), sb=float(), shape=bool(), s=bool(),
                   simulation=bool(), sm=bool(), smart=list, sr=list, sparseAnimCurveBake=bool(), sac=bool(),
                   time=tuple(), t=tuple(), *args, **kwargs):
    pass


def baseTemplate(exists=bool(), ex=bool(), fileName=str(), fn=str(), force=bool(), f=bool(), load=bool(), l=bool(),
                 matchFile=str(), mf=str(), silent=bool(), si=bool(), unload=bool(), u=bool(), viewList=str(), vl=str(),
                 *args, **kwargs):
    pass


def baseView(itemInfo=str(), ii=str(), itemList=bool(), il=bool(), viewDescription=bool(), vd=bool(), viewLabel=bool(),
             vb=bool(), viewList=bool(), vl=bool(), viewName=str(), vn=str(), *args, **kwargs):
    pass


def batchRender(filename=str(), f=str(), melCommand=str(), mc=str(), numProcs=int(), n=int(), preRenderCommand=str(),
                prc=str(), remoteRenderMachine=str(), rm=str(), renderCommandOptions=str(), rco=str(), showImage=bool(),
                si=bool(), status=str(), st=str(), useRemoteRender=bool(), um=bool(), useStandalone=bool(), us=bool(),
                verbosity=int(), v=int(), *args, **kwargs):
    pass


def bevel(bevelShapeType=int(), bst=int(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
          cornerType=int(), ct=int(), depth=float(), d=float(), extrudeDepth=float(), ed=float(), joinSurfaces=bool(),
          js=bool(), name=str(), n=str(), nodeState=int(), nds=int(), numberOfSides=int(), ns=int(), object=bool(),
          o=bool(), polygon=int(), po=int(), range=bool(), rn=bool(), tolerance=float(), tol=float(), width=float(),
          w=float(), *args, **kwargs):
    pass


def bevelPlus(bevelInside=bool(), bin=bool(), capSides=int(), cap=int(), constructionHistory=bool(), ch=bool(),
              innerStyle=int(), joinSurfaces=bool(), js=bool(), name=str(), n=str(), normalsOutwards=bool(), no=bool(),
              numberOfSides=int(), ns=int(), outerStyle=int(), os=int(), polygon=int(), po=int(), range=bool(),
              rn=bool(), *args, **kwargs):
    pass


def bezierAnchorPreset(preset=int(), p=int(), *args, **kwargs):
    pass


def bezierAnchorState(even=bool(), ev=bool(), smooth=bool(), sm=bool(), *args, **kwargs):
    pass


def bezierCurveToNurbs(*args, **kwargs):
    pass


def bezierInfo(anchorFromCV=int(), afc=int(), cvFromAnchor=int(), cfa=int(), isAnchorSelected=bool(), ias=bool(),
               isTangentSelected=bool(), its=bool(), onlyAnchorsSelected=bool(), oas=bool(),
               onlyTangentsSelected=bool(), ots=bool(), *args, **kwargs):
    pass


def bindSkin(byClosestPoint=bool(), bcp=bool(), byPartition=bool(), bp=bool(), colorJoints=bool(), cj=bool(),
             delete=bool(), d=bool(), doNotDescend=bool(), dnd=bool(), enable=bool(), en=bool(), name=str(), n=str(),
             partition=str(), p=str(), toAll=bool(), ta=bool(), toSelectedBones=bool(), tsb=bool(), toSkeleton=bool(),
             ts=bool(), unbind=bool(), ub=bool(), unbindKeepHistory=bool(), ubk=bool(), unlock=bool(), ul=bool(), *args,
             **kwargs):
    pass


def binMembership(addToBin=str(), add=str(), exists=str(), ex=str(), inheritBinsFromNodes=str(), ibn=str(),
                  isValidBinName=str(), ivn=str(), listBins=bool(), lb=bool(), makeExclusive=str(), mke=str(),
                  notifyChanged=bool(), nfc=bool(), removeFromBin=str(), rm=str(), *args, **kwargs):
    pass


def blend2(autoAnchor=bool(), aa=bool(), autoNormal=bool(), an=bool(), caching=bool(), cch=bool(),
           constructionHistory=bool(), ch=bool(), crvsInFirstRail=int(), cfr=int(), flipLeftNormal=bool(), fln=bool(),
           flipRightNormal=bool(), frn=bool(), leftAnchor=float(), la=float(), leftEnd=float(), le=float(),
           leftStart=float(), ls=float(), multipleKnots=bool(), mk=bool(), name=str(), n=str(), nodeState=int(),
           nds=int(), object=bool(), o=bool(), polygon=int(), po=int(), positionTolerance=float(), pt=float(),
           reverseLeft=bool(), rvl=bool(), reverseRight=bool(), rvr=bool(), rightAnchor=float(), ra=float(),
           rightEnd=float(), re=float(), rightStart=float(), rs=float(), tangentTolerance=float(), tt=float(), *args,
           **kwargs):
    pass


def blendShape(after=bool(), af=bool(), afterReference=bool(), ar=bool(), automatic=bool(), at=bool(), before=bool(),
               bf=bool(), copyDelta=list, cd=list, copyInBetweenDelta=list, cid=list, deformerTools=bool(), dt=bool(),
               envelope=float(), en=float(), exclusive=str(), ex=str(), export=str(), ep=str(), exportTarget=list,
               et=list, flipTarget=list, ft=list, frontOfChain=bool(), foc=bool(), geometry=str(), g=str(),
               geometryIndices=bool(), gi=bool(), ignoreSelected=bool(), inBetween=bool(), ib=bool(),
               inBetweenIndex=int(), ibi=int(), inBetweenType=str(), ibt=str(), includeHiddenSelections=bool(),
               ihs=bool(), ip=str(), mergeSource=int(), mgs=int(), mergeTarget=int(), mgt=int(), mirrorDirection=int(),
               md=int(), mirrorTarget=list, mt=list, name=str(), n=str(), normalizationGroups=bool(), ng=bool(),
               origin=str(), o=str(), parallel=bool(), par=bool(), prune=bool(), pr=bool(), remove=bool(), rm=bool(),
               resetTargetDelta=list, rtd=list, split=bool(), sp=bool(), suppressDialog=bool(), sd=bool(),
               symmetryAxis=str(), sa=str(), symmetryEdge=str(), se=str(), symmetrySpace=int(), ss=int(),
               tangentSpace=bool(), ts=bool(), target=list, t=list, topologyCheck=bool(), tc=bool(), transform=str(),
               tr=str(), useComponentTags=bool(), uct=bool(), weight=list, w=list, weightCount=int(), wc=int(), *args,
               **kwargs):
    pass


def blendShapeEditor(control=bool(), ctl=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), exists=bool(),
                     ex=bool(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(), highlightConnection=str(),
                     hlc=str(), lockMainConnection=bool(), lck=bool(), mainListConnection=str(), mlc=str(), panel=str(),
                     pnl=str(), parent=str(), p=str(), selectionConnection=str(), slc=str(), stateString=bool(),
                     sts=bool(), targetControlList=bool(), tcl=bool(), targetList=bool(), tl=bool(), unParent=bool(),
                     up=bool(), unlockMainConnection=bool(), ulk=bool(), updateMainConnection=bool(), upd=bool(),
                     useTemplate=str(), ut=str(), verticalSliders=bool(), vs=bool(), *args, **kwargs):
    pass


def blendShapePanel(blendShapeEditor=bool(), be=bool(), control=bool(), ctl=bool(), copy=str(), cp=str(),
                    createString=bool(), cs=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                    editString=bool(), es=bool(), exists=bool(), ex=bool(), init=bool(), isUnique=bool(), iu=bool(),
                    label=str(), l=str(), menuBarRepeatLast=bool(), mrl=bool(), menuBarVisible=bool(), mbv=bool(),
                    needsInit=bool(), ni=bool(), parent=str(), p=str(), popupMenuProcedure=str(), pmp=str(),
                    replacePanel=str(), rp=str(), tearOff=bool(), to=bool(), tearOffCopy=str(), toc=str(),
                    tearOffRestore=bool(), tor=bool(), unParent=bool(), up=bool(), useTemplate=str(), ut=str(), *args,
                    **kwargs):
    pass


def blendTwoAttr(attribute=str(), at=str(), attribute0=str(), at0=str(), attribute1=str(), at1=str(), blender=str(),
                 bl=str(), controlPoints=bool(), cp=bool(), driver=int(), d=int(), name=str(), n=str(), shape=bool(),
                 s=bool(), time=tuple(), t=tuple(), *args, **kwargs):
    pass


def blindDataType(dataType=str(), dt=str(), longDataName=str(), ldn=str(), longNames=bool(), ln=bool(), query=bool(),
                  q=bool(), shortDataName=str(), sdn=str(), shortNames=bool(), sn=bool(), typeId=int(), id=int(),
                  typeNames=bool(), tn=bool(), *args, **kwargs):
    pass


def boneLattice(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(), bicep=float(),
                bi=float(), deformerTools=bool(), dt=bool(), exclusive=str(), ex=str(), frontOfChain=bool(), foc=bool(),
                geometry=str(), g=str(), geometryIndices=bool(), gi=bool(), ignoreSelected=bool(),
                includeHiddenSelections=bool(), ihs=bool(), joint=str(), j=str(), lengthIn=float(), li=float(),
                lengthOut=float(), lo=float(), name=str(), n=str(), parallel=bool(), par=bool(), prune=bool(),
                pr=bool(), remove=bool(), rm=bool(), split=bool(), sp=bool(), transform=str(), t=str(), tricep=float(),
                tr=float(), useComponentTags=bool(), uct=bool(), widthLeft=float(), wl=float(), widthRight=float(),
                wr=float(), *args, **kwargs):
    pass


def boundary(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), endPoint=bool(), ep=bool(),
             endPointTolerance=float(), ept=float(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(),
             o=bool(), order=bool(), polygon=int(), po=int(), range=bool(), rn=bool(), *args, **kwargs):
    pass


def boxDollyCtx(alternateContext=bool(), ac=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
                i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), toolName=str(), tn=str(),
                *args, **kwargs):
    pass


def boxZoomCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
               image3=str(), i3=str(), name=str(), n=str(), zoomScale=float(), zs=float(), *args, **kwargs):
    pass


def bufferCurve(animation=str(), an=str(), attribute=str(), at=str(), controlPoints=bool(), cp=bool(), exists=bool(),
                ex=bool(), float=tuple(), f=tuple(), hierarchy=str(), hi=str(), includeUpperBound=bool(), iub=bool(),
                index=int(), overwrite=bool(), ov=bool(), shape=bool(), s=bool(), swap=bool(), sw=bool(), time=tuple(),
                t=tuple(), useReferencedCurve=bool(), urc=bool(), *args, **kwargs):
    pass


def buildBookmarkMenu(editor=str(), ed=str(), type=str(), typ=str(), *args, **kwargs):
    pass


def buildKeyframeMenu(*args, **kwargs):
    pass


def button(actOnPress=bool(), aop=bool(), actionIsSubstitute=bool(), ais=bool(), align=str(), al=str(),
           annotation=str(), ann=str(), backgroundColor=list, bgc=list, command=str(), c=str(), defineTemplate=str(),
           dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
           enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(),
           exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list,
           hlc=list, isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(),
           nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
           preventOverride=bool(), po=bool(), recomputeSize=bool(), rs=bool(), statusBarMessage=str(), sbm=str(),
           useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(),
           w=int(), *args, **kwargs):
    pass


def buttonManip(icon=str(), i=str(), *args, **kwargs):
    pass


def cacheEvaluator(cacheFillMode=str(), cfm=str(), cacheFillOrder=str(), cfo=str(), cacheInvalidate=tuple(), ci=tuple(),
                   cacheName=str(), cn=str(), cachedFrames=bool(), cfs=bool(), cachingPoints=bool(), cps=bool(),
                   creationParameters=bool(), cp=bool(), delegateEvaluation=bool(), de=bool(),
                   dynamicsAsyncRefresh=bool(), dar=bool(), dynamicsSupportActive=bool(), dsa=bool(),
                   dynamicsSupportEnabled=bool(), dse=bool(), flushCache=str(), fc=str(), flushCacheRange=list,
                   fcr=list, flushCacheSync=bool(), fcs=bool(), flushCacheWait=bool(), fcw=bool(),
                   hybridCacheMode=str(), hcm=str(), layeredEvaluationActive=bool(), lea=bool(),
                   layeredEvaluationCachingPoints=bool(), lec=bool(), layeredEvaluationEnabled=bool(), lee=bool(),
                   listCacheNames=bool(), lcn=bool(), listCachedNodes=bool(), lcd=bool(), listValueNames=bool(),
                   lvn=bool(), newAction=str(), na=str(), newActionParam=str(), nap=str(), newFilter=str(), nf=str(),
                   newFilterParam=str(), nfp=str(), newRule=str(), nr=str(), newRuleParam=str(), nrp=str(),
                   pauseInvalidation=bool(), pi=bool(), preventFrameSkip=bool(), pfs=bool(), resetRules=bool(),
                   rr=bool(), resourceUsage=bool(), ru=bool(), resumeInvalidation=bool(), ri=bool(), safeMode=bool(),
                   sf=bool(), safeModeMessages=bool(), sfm=bool(), safeModeTriggered=bool(), sft=bool(),
                   valueName=str(), vn=str(), waitForCache=float(), wfc=float(), *args, **kwargs):
    pass


def cacheFile(appendFrame=bool(), apf=bool(), attachFile=bool(), af=bool(), cacheFileNode=str(), cfn=str(),
              cacheFormat=str(), cf=str(), cacheInfo=str(), ci=str(), cacheableAttrs=str(), cat=str(),
              cacheableNode=str(), cnd=str(), channelIndex=bool(), chi=bool(), channelName=str(), cnm=str(),
              convertPc2=bool(), pc2=bool(), createCacheNode=bool(), ccn=bool(), creationChannelName=str(), cch=str(),
              dataSize=bool(), dsz=bool(), deleteCachedFrame=bool(), dcf=bool(), descriptionFileName=bool(), dfn=bool(),
              directory=str(), dir=str(), doubleToFloat=bool(), dtf=bool(), endTime=float(), et=float(), fileName=str(),
              f=str(), format=str(), fm=str(), geometry=bool(), gm=bool(), inAttr=str(), ia=str(), inTangent=str(),
              it=str(), interpEndTime=float(), iet=float(), interpStartTime=float(), ist=float(), noBackup=bool(),
              nb=bool(), outAttr=str(), oa=str(), outTangent=str(), ot=str(), pc2File=str(), pcf=str(),
              pointCount=bool(), pc=bool(), points=str(), pts=str(), pointsAndNormals=str(), pan=str(), prefix=bool(),
              p=bool(), refresh=bool(), r=bool(), replaceCachedFrame=bool(), rcf=bool(),
              replaceWithoutSimulating=bool(), rws=bool(), runupFrames=int(), rf=int(), sampleMultiplier=int(),
              spm=int(), simulationRate=float(), smr=float(), singleCache=bool(), sch=bool(), startTime=float(),
              st=float(), staticCache=bool(), sc=bool(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def cacheFileCombine(cacheIndex=bool(), ci=bool(), channelName=str(), cnm=str(), connectCache=str(), cc=str(),
                     keepWeights=bool(), kw=bool(), layerNode=bool(), ln=bool(), nextAvailable=bool(), na=bool(),
                     object=str(), obj=str(), objectIndex=int(), oi=int(), *args, **kwargs):
    pass


def cacheFileMerge(endTime=float(), et=float(), geometry=bool(), g=bool(), startTime=float(), st=float(), *args,
                   **kwargs):
    pass


def cacheFileTrack(insertTrack=int(), it=int(), lock=bool(), l=bool(), mute=bool(), m=bool(), removeEmptyTracks=bool(),
                   ret=bool(), removeTrack=int(), rt=int(), solo=bool(), so=bool(), track=int(), t=int(), *args,
                   **kwargs):
    pass


def callbacks(addCallback=str(), ac=str(), clearAllCallbacks=bool(), cac=bool(), clearCallbacks=bool(), cc=bool(),
              describeHooks=bool(), dh=bool(), dumpCallbacks=bool(), dc=bool(), executeCallbacks=bool(), ec=bool(),
              hook=str(), h=str(), listCallbacks=bool(), lc=bool(), owner=str(), o=str(), removeCallback=str(),
              rc=str(), *args, **kwargs):
    pass


def camera(aspectRatio=float(), ar=float(), cameraScale=float(), cs=float(), centerOfInterest=float(), coi=float(),
           clippingPlanes=bool(), cp=bool(), depthOfField=bool(), dof=bool(), displayFieldChart=bool(), dfc=bool(),
           displayFilmGate=bool(), dfg=bool(), displayFilmOrigin=bool(), dfo=bool(), displayFilmPivot=bool(),
           dfp=bool(), displayGateMask=bool(), dgm=bool(), displayResolution=bool(), dr=bool(),
           displaySafeAction=bool(), dsa=bool(), displaySafeTitle=bool(), dst=bool(), fStop=float(), fs=float(),
           farClipPlane=float(), fcp=float(), farFocusDistance=float(), ffd=float(), filmFit=str(), ff=str(),
           filmFitOffset=float(), ffo=float(), filmRollOrder=str(), fro=str(), filmRollValue=float(), frv=float(),
           filmTranslateH=float(), fth=float(), filmTranslateV=float(), ftv=float(), focalLength=float(), fl=float(),
           focusDistance=float(), fd=float(), homeCommand=str(), hc=str(), horizontalFieldOfView=float(), hfv=float(),
           horizontalFilmAperture=float(), hfa=float(), horizontalFilmOffset=float(), hfo=float(),
           horizontalPan=float(), hpn=float(), horizontalRollPivot=float(), hrp=float(), horizontalShake=float(),
           hs=float(), journalCommand=bool(), jc=bool(), lensSqueezeRatio=float(), lsr=float(), lockTransform=bool(),
           lt=bool(), motionBlur=bool(), mb=bool(), name=str(), n=str(), nearClipPlane=float(), ncp=float(),
           nearFocusDistance=float(), nfd=float(), orthographic=bool(), o=bool(), orthographicWidth=float(), ow=float(),
           overscan=float(), ovr=float(), panZoomEnabled=bool(), pze=bool(), position=list, p=list, postScale=float(),
           pts=float(), preScale=float(), prs=float(), renderPanZoom=bool(), rpz=bool(), rotation=list, rot=list,
           shakeEnabled=bool(), se=bool(), shakeOverscan=float(), so=float(), shakeOverscanEnabled=bool(), soe=bool(),
           shutterAngle=float(), sa=float(), startupCamera=bool(), sc=bool(), stereoHorizontalImageTranslate=float(),
           hit=float(), stereoHorizontalImageTranslateEnabled=bool(), she=bool(), verticalFieldOfView=float(),
           vfv=float(), verticalFilmAperture=float(), vfa=float(), verticalFilmOffset=float(), vfo=float(),
           verticalLock=bool(), vl=bool(), verticalPan=float(), vpn=float(), verticalRollPivot=float(), vrp=float(),
           verticalShake=float(), vs=float(), worldCenterOfInterest=list, wci=list, worldUp=list, wup=list,
           zoom=float(), zom=float(), *args, **kwargs):
    pass


def cameraSet(active=bool(), a=bool(), appendTo=bool(), atl=bool(), camera=str(), cam=str(), clearDepth=bool(),
              cd=bool(), deleteAll=bool(), da=bool(), deleteLayer=bool(), d=bool(), insertAt=bool(), ins=bool(),
              layer=int(), l=int(), name=str(), n=str(), numLayers=bool(), nl=bool(), objectSet=str(), os=str(),
              order=int(), o=int(), *args, **kwargs):
    pass


def cameraView(addBookmark=bool(), ab=bool(), animate=bool(), an=bool(), bookmarkType=int(), typ=int(), camera=str(),
               c=str(), name=str(), n=str(), removeBookmark=bool(), rb=bool(), setCamera=bool(), sc=bool(),
               setView=bool(), sv=bool(), *args, **kwargs):
    pass


def canCreateCaddyManip(*args, **kwargs):
    pass


def canCreateManip(*args, **kwargs):
    pass


def canvas(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(), docTag=str(),
           dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
           enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
           fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, hsvValue=list,
           hsv=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
           numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
           pressCommand=str(), pc=str(), preventOverride=bool(), po=bool(), rgbValue=list, rgb=list,
           statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
           visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def changeSubdivComponentDisplayLevel(level=int(), l=int(), relative=bool(), r=bool(), *args, **kwargs):
    pass


def changeSubdivRegion(action=int(), a=int(), level=int(), l=int(), *args, **kwargs):
    pass


def channelBox(annotation=str(), ann=str(), attrBgColor=list, bc=list, attrColor=list, ac=list, attrFilter=str(),
               af=str(), attrRegex=str(), ar=str(), attributeEditorMode=bool(), aem=bool(), backgroundColor=list,
               bgc=list, containerAtTop=bool(), cat=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
               dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
               enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), enableLabelSelection=bool(),
               els=bool(), execute=list, exe=list, exists=bool(), ex=bool(), fieldWidth=int(), fw=int(),
               fixedAttrList=list, fal=list, fullPathName=bool(), fpn=bool(), height=int(), h=int(),
               highlightColor=list, hlc=list, historyObjectList=bool(), hol=bool(), hyperbolic=bool(), hyp=bool(),
               inputs=bool(), isObscured=bool(), io=bool(), labelWidth=int(), lw=int(), longNames=bool(), ln=bool(),
               mainListConnection=str(), mlc=str(), mainObjectList=bool(), mol=bool(), manage=bool(), m=bool(),
               maxHeight=int(), mh=int(), maxWidth=int(), mw=int(), niceNames=bool(), nn=bool(), noBackground=bool(),
               nbg=bool(), nodeRegex=str(), nr=str(), numberOfPopupMenus=bool(), npm=bool(), outputObjectList=bool(),
               ool=bool(), outputs=bool(), out=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
               precision=int(), pre=int(), preventOverride=bool(), po=bool(), select=str(), s=str(),
               selectedHistoryAttributes=bool(), sha=bool(), selectedMainAttributes=bool(), sma=bool(),
               selectedOutputAttributes=bool(), soa=bool(), selectedShapeAttributes=bool(), ssa=bool(),
               shapeObjectList=bool(), sol=bool(), shapes=bool(), shp=bool(), showNamespace=bool(), sn=bool(),
               showTransforms=bool(), st=bool(), speed=float(), spd=float(), statusBarMessage=str(), sbm=str(),
               takeFocus=bool(), tf=bool(), update=bool(), u=bool(), useManips=str(), mnp=str(), useTemplate=str(),
               ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
               **kwargs):
    pass


def character(addElement=str(), add=str(), addOffsetObject=str(), aoo=str(), anyMember=str(), am=str(),
              characterPlug=bool(), cp=bool(), clear=str(), cl=str(), empty=bool(), em=bool(), excludeDynamic=bool(),
              ed=bool(), excludeRotate=bool(), er=bool(), excludeScale=bool(), es=bool(), excludeTranslate=bool(),
              et=bool(), excludeVisibility=bool(), ev=bool(), flatten=str(), fl=str(), forceElement=str(), fe=str(),
              include=str(), intersection=str(), int=str(), isIntersecting=str(), ii=str(), isMember=str(), im=str(),
              library=bool(), lib=bool(), memberIndex=int(), mi=int(), name=str(), n=str(), noWarnings=bool(),
              nw=bool(), nodesOnly=bool(), no=bool(), offsetNode=bool(), ofs=bool(), remove=str(), rm=str(),
              removeOffsetObject=str(), roo=str(), root=str(), rt=str(), scheduler=bool(), sc=bool(), split=str(),
              sp=str(), subtract=str(), sub=str(), text=str(), t=str(), union=str(), un=str(), userAlias=str(),
              ua=str(), *args, **kwargs):
    pass


def characterize(activatePivot=bool(), apv=bool(), addAuxEffector=bool(), aae=bool(), addFloorContactPlane=bool(),
                 afp=bool(), addMissingEffectors=bool(), ame=bool(), attributeFromHIKProperty=str(), ahk=str(),
                 attributeFromHIKPropertyMode=str(), mhk=str(), autoActivateBodyPart=bool(), aab=bool(),
                 changePivotPlacement=bool(), cpp=bool(), effectors=str(), ef=str(), fkSkeleton=str(), fk=str(),
                 name=str(), nm=str(), pinHandFeet=bool(), phf=bool(), placeNewPivot=bool(), pnp=bool(), posture=str(),
                 pos=str(), sourceSkeleton=str(), sk=str(), stancePose=str(), sp=str(), type=str(), typ=str(), *args,
                 **kwargs):
    pass


def characterMap(mapAttr=list, ma=list, mapMethod=str(), mm=str(), mapNode=list, mn=list, mapping=str(), m=str(),
                 proposedMapping=bool(), pm=bool(), unmapAttr=list, ua=list, unmapNode=list, umn=list, *args, **kwargs):
    pass


def checkBox(align=str(), al=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(),
             cc=str(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
             dropCallback=str(), dpc=str(), editable=bool(), ed=bool(), enable=bool(), en=bool(),
             enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
             fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(),
             io=bool(), label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
             numberOfPopupMenus=bool(), npm=bool(), offCommand=str(), ofc=str(), onCommand=str(), onc=str(),
             parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
             recomputeSize=bool(), rs=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
             value=bool(), v=bool(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(),
             w=int(), *args, **kwargs):
    pass


def checkBoxGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                changeCommand=str(), cc=str(), changeCommand1=str(), cc1=str(), changeCommand2=str(), cc2=str(),
                changeCommand3=str(), cc3=str(), changeCommand4=str(), cc4=str(), columnAlign=list, cal=list,
                columnAlign2=list, cl2=list, columnAlign3=list, cl3=list, columnAlign4=list, cl4=list,
                columnAlign5=list, cl5=list, columnAlign6=list, cl6=list, columnAttach=list, cat=list,
                columnAttach2=list, ct2=list, columnAttach3=list, ct3=list, columnAttach4=list, ct4=list,
                columnAttach5=list, ct5=list, columnAttach6=list, ct6=list, columnOffset2=list, co2=list,
                columnOffset3=list, co3=list, columnOffset4=list, co4=list, columnOffset5=list, co5=list,
                columnOffset6=list, co6=list, columnWidth=list, cw=list, columnWidth1=int(), cw1=int(),
                columnWidth2=list, cw2=list, columnWidth3=list, cw3=list, columnWidth4=list, cw4=list,
                columnWidth5=list, cw5=list, columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(),
                dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), editable=bool(), ed=bool(),
                enable=bool(), en=bool(), enable1=bool(), en1=bool(), enable2=bool(), en2=bool(), enable3=bool(),
                en3=bool(), enable4=bool(), en4=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                highlightColor=list, hlc=list, isObscured=bool(), io=bool(), label=str(), l=str(), label1=str(),
                l1=str(), label2=str(), l2=str(), label3=str(), l3=str(), label4=str(), l4=str(), labelArray2=list,
                la2=list, labelArray3=list, la3=list, labelArray4=list, la4=list, manage=bool(), m=bool(),
                noBackground=bool(), nbg=bool(), numberOfCheckBoxes=int(), ncb=int(), numberOfPopupMenus=bool(),
                npm=bool(), offCommand=str(), ofc=str(), offCommand1=str(), of1=str(), offCommand2=str(), of2=str(),
                offCommand3=str(), of3=str(), offCommand4=str(), of4=str(), onCommand=str(), onc=str(),
                onCommand1=str(), on1=str(), onCommand2=str(), on2=str(), onCommand3=str(), on3=str(), onCommand4=str(),
                on4=str(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
                rowAttach=list, rat=list, statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), value1=bool(),
                v1=bool(), value2=bool(), v2=bool(), value3=bool(), v3=bool(), value4=bool(), v4=bool(),
                valueArray2=list, va2=list, valueArray3=list, va3=list, valueArray4=list, va4=list, vertical=bool(),
                vr=bool(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
                *args, **kwargs):
    pass


def checkDefaultRenderGlobals(*args, **kwargs):
    pass


def choice(attribute=str(), at=str(), controlPoints=bool(), cp=bool(), index=int(), name=str(), n=str(), selector=str(),
           sl=str(), shape=bool(), s=bool(), sourceAttribute=str(), sa=str(), time=float(), t=float(), *args, **kwargs):
    pass


def circle(caching=bool(), cch=bool(), center=list, c=list, centerX=float(), cx=float(), centerY=float(), cy=float(),
           centerZ=float(), cz=float(), constructionHistory=bool(), ch=bool(), degree=int(), d=int(), first=list,
           fp=list, firstPointX=float(), fpx=float(), firstPointY=float(), fpy=float(), firstPointZ=float(),
           fpz=float(), fixCenter=bool(), fc=bool(), name=str(), n=str(), nodeState=int(), nds=int(), normal=list,
           nr=list, normalX=float(), nrx=float(), normalY=float(), nry=float(), normalZ=float(), nrz=float(),
           object=bool(), o=bool(), radius=float(), r=float(), sections=int(), s=int(), sweep=float(), sw=float(),
           tolerance=float(), tol=float(), useTolerance=bool(), ut=bool(), *args, **kwargs):
    pass


def circularFillet(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), curveOnSurface=bool(), cos=bool(),
                   name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), positionTolerance=float(),
                   pt=float(), primaryRadius=float(), pr=float(), secondaryRadius=float(), sr=float(),
                   tangentTolerance=float(), tt=float(), *args, **kwargs):
    pass


def clearCache(allNodes=bool(), all=bool(), computed=bool(), c=bool(), dirty=bool(), d=bool(), *args, **kwargs):
    pass


def clip(absolute=bool(), abs=bool(), absoluteRotations=bool(), abr=bool(), active=str(), a=str(), addTrack=bool(),
         at=bool(), allAbsolute=bool(), aa=bool(), allClips=bool(), ac=bool(), allRelative=bool(), ar=bool(),
         allSourceClips=bool(), asc=bool(), animCurveRange=bool(), acr=bool(), character=bool(), ch=bool(),
         constraint=bool(), cn=bool(), copy=bool(), c=bool(), defaultAbsolute=bool(), da=bool(), duplicate=bool(),
         d=bool(), endTime=float(), end=float(), expression=bool(), ex=bool(), ignoreSubcharacters=bool(),
         isolate=bool(), i=bool(), leaveOriginal=bool(), lo=bool(), mapMethod=str(), mm=str(), name=str(), n=str(),
         newName=str(), nn=str(), paste=bool(), p=bool(), pasteInstance=bool(), pi=bool(), remove=bool(), rm=bool(),
         removeTrack=bool(), rt=bool(), rotationOffset=list, rof=list, rotationsAbsolute=bool(), ra=bool(),
         scheduleClip=bool(), sc=bool(), sourceClipName=bool(), scn=bool(), split=float(), sp=float(),
         startTime=float(), s=float(), translationOffset=list, tof=list, useChannel=str(), uc=str(), *args, **kwargs):
    pass


def clipEditor(allTrackHeights=int(), th=int(), autoFit=str(), af=str(), autoFitTime=str(), aft=str(),
               clipDropCmd=str(), cd=str(), clipStyle=int(), cs=int(), control=bool(), ctl=bool(), defineTemplate=str(),
               dt=str(), deleteCmd=str(), dc=str(), deselectAll=bool(), da=bool(), displayActiveKeyTangents=str(),
               dat=str(), displayActiveKeys=str(), dak=str(), displayInfinities=str(), di=str(), displayKeys=str(),
               dk=str(), displayTangents=str(), dtn=str(), displayValues=str(), dv=str(), docTag=str(), dtg=str(),
               exists=bool(), ex=bool(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(), frameAll=bool(),
               fa=bool(), frameRange=list, fr=list, highlightConnection=str(), hlc=str(), highlightedBlend=list,
               hb=list, highlightedClip=list, hc=list, initialized=bool(), it=bool(), listAllCharacters=bool(),
               lac=bool(), listCurrentCharacters=bool(), lc=bool(), lockMainConnection=bool(), lck=bool(), lookAt=str(),
               la=str(), mainListConnection=str(), mlc=str(), manageSequencer=bool(), ms=bool(), menuContext=str(),
               mc=str(), panel=str(), pnl=str(), parent=str(), p=str(), selectBlend=list, sb=list, selectClip=list,
               sc=list, selectionConnection=str(), slc=str(), snapTime=str(), st=str(), snapValue=str(), sv=str(),
               stateString=bool(), sts=bool(), unParent=bool(), up=bool(), unlockMainConnection=bool(), ulk=bool(),
               updateMainConnection=bool(), upd=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def clipEditorCurrentTimeCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                             i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def clipMatching(clipDst=list, cd=list, clipSrc=list, cs=list, matchRotation=int(), mr=int(), matchTranslation=int(),
                 mt=int(), *args, **kwargs):
    pass


def clipSchedule(allAbsolute=bool(), aa=bool(), allRelative=bool(), ar=bool(), blend=list, b=list, blendNode=list,
                 bn=list, blendUsingNode=str(), bun=str(), character=bool(), ch=bool(), clipIndex=int(), ci=int(),
                 cycle=float(), c=float(), defaultAbsolute=bool(), da=bool(), enable=bool(), en=bool(), group=bool(),
                 grp=bool(), groupIndex=int(), gri=int(), groupName=str(), gn=str(), hold=float(), ph=float(),
                 insertTrack=int(), it=int(), instance=str(), listCurves=bool(), lc=bool(), listPairs=bool(), lp=bool(),
                 lock=bool(), l=bool(), mute=bool(), m=bool(), name=str(), n=str(), postCycle=float(), poc=float(),
                 preCycle=float(), prc=float(), remove=bool(), rm=bool(), removeBlend=list, rb=list,
                 removeEmptyTracks=bool(), ret=bool(), removeTrack=int(), rt=int(), rotationsAbsolute=bool(), ra=bool(),
                 scale=float(), sc=float(), shift=int(), sh=int(), shiftIndex=int(), shi=int(), solo=bool(), so=bool(),
                 sourceClipName=bool(), scn=bool(), sourceEnd=float(), se=float(), sourceStart=float(), ss=float(),
                 start=float(), s=float(), track=int(), t=int(), weight=float(), w=float(), weightStyle=int(), ws=int(),
                 *args, **kwargs):
    pass


def clipSchedulerOutliner(annotation=str(), ann=str(), backgroundColor=list, bgc=list, clipScheduler=str(), cs=str(),
                          defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                          dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                          enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(),
                          fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(),
                          io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                          numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(),
                          pma=bool(), preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(),
                          useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(),
                          vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def closeCurve(blendBias=float(), bb=float(), blendKnotInsertion=bool(), bki=bool(), caching=bool(), cch=bool(),
               constructionHistory=bool(), ch=bool(), curveOnSurface=bool(), cos=bool(), name=str(), n=str(),
               nodeState=int(), nds=int(), object=bool(), o=bool(), parameter=float(), p=float(), preserveShape=int(),
               ps=int(), replaceOriginal=bool(), rpo=bool(), *args, **kwargs):
    pass


def closeSurface(blendBias=float(), bb=float(), blendKnotInsertion=bool(), bki=bool(), caching=bool(), cch=bool(),
                 constructionHistory=bool(), ch=bool(), direction=int(), d=int(), name=str(), n=str(), nodeState=int(),
                 nds=int(), object=bool(), o=bool(), parameter=float(), p=float(), preserveShape=int(), ps=int(),
                 replaceOriginal=bool(), rpo=bool(), *args, **kwargs):
    pass


def cluster(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(), bindState=bool(),
            bs=bool(), deformerTools=bool(), dt=bool(), envelope=float(), en=float(), exclusive=str(), ex=str(),
            frontOfChain=bool(), foc=bool(), geometry=str(), g=str(), geometryIndices=bool(), gi=bool(),
            ignoreSelected=bool(), includeHiddenSelections=bool(), ihs=bool(), name=str(), n=str(), parallel=bool(),
            par=bool(), prune=bool(), pr=bool(), relative=bool(), rel=bool(), remove=bool(), rm=bool(),
            resetGeometry=bool(), rg=bool(), split=bool(), sp=bool(), useComponentTags=bool(), uct=bool(),
            weightedNode=list, wn=list, *args, **kwargs):
    pass


def cmdFileOutput(close=int(), c=int(), closeAll=bool(), ca=bool(), open=str(), o=str(), status=int(), s=int(), *args,
                  **kwargs):
    pass


def cmdScrollFieldExecuter(annotation=str(), ann=str(), appendText=str(), at=str(), autoCloseBraces=bool(), acb=bool(),
                           backgroundColor=list, bgc=list, clear=bool(), clr=bool(), commandCompletion=bool(),
                           cco=bool(), copySelection=bool(), cp=bool(), currentLine=int(), cl=int(),
                           cutSelection=bool(), ct=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                           dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                           enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), execute=bool(),
                           exc=bool(), executeAll=bool(), exa=bool(), exists=bool(), ex=bool(),
                           fileChangedCommand=str(), fcc=str(), filename=bool(), fn=bool(), filterKeyPress=str(),
                           fkp=str(), fullPathName=bool(), fpn=bool(), hasFocus=bool(), hf=bool(), hasSelection=bool(),
                           hsl=bool(), height=int(), h=int(), highlightColor=list, hlc=list, insertText=str(), it=str(),
                           isObscured=bool(), io=bool(), load=bool(), ld=bool(), loadContents=str(), ldc=str(),
                           loadFile=str(), ldf=str(), manage=bool(), m=bool(), modificationChangedCommand=str(),
                           mcc=str(), modified=bool(), mod=bool(), noBackground=bool(), nbg=bool(), numberOfLines=int(),
                           nl=int(), numberOfPopupMenus=bool(), npm=bool(), objectPathCompletion=bool(), opc=bool(),
                           parent=str(), p=str(), pasteSelection=bool(), pst=bool(), popupMenuArray=bool(), pma=bool(),
                           preventOverride=bool(), po=bool(), redo=bool(), rd=bool(), removeStoredContents=str(),
                           rsc=str(), replaceAll=list, rpa=list, saveFile=str(), svf=str(), saveSelection=str(),
                           sv=str(), saveSelectionToShelf=bool(), svs=bool(), searchAndSelect=bool(), sas=bool(),
                           searchDown=bool(), sd=bool(), searchMatchCase=bool(), smc=bool(), searchString=str(),
                           ss=str(), searchWraps=bool(), sw=bool(), select=list, sl=list, selectAll=bool(), sla=bool(),
                           selectedText=bool(), slt=bool(), showLineNumbers=bool(), sln=bool(),
                           showTabsAndSpaces=bool(), sts=bool(), showTooltipHelp=bool(), sth=bool(), source=bool(),
                           src=bool(), sourceType=str(), st=str(), spacesPerTab=int(), spt=int(),
                           statusBarMessage=str(), sbm=str(), storeContents=str(), stc=str(), tabsForIndent=bool(),
                           tfi=bool(), text=str(), t=str(), textLength=bool(), tl=bool(), undo=bool(), ud=bool(),
                           useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(),
                           vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def cmdScrollFieldReporter(annotation=str(), ann=str(), backgroundColor=list, bgc=list, clear=bool(), clr=bool(),
                           copySelection=bool(), cp=bool(), cutSelection=bool(), ct=bool(), defineTemplate=str(),
                           dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(),
                           dpc=str(), echoAllCommands=bool(), eac=bool(), enable=bool(), en=bool(),
                           enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                           ex=bool(), filterSourceType=str(), fst=str(), fullPathName=bool(), fpn=bool(),
                           hasFocus=bool(), hf=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                           isObscured=bool(), io=bool(), lineNumbers=bool(), ln=bool(), manage=bool(), m=bool(),
                           noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(),
                           p=str(), pasteSelection=bool(), pst=bool(), popupMenuArray=bool(), pma=bool(),
                           preventOverride=bool(), po=bool(), receiveFocusCommand=str(), rfc=str(), saveSelection=str(),
                           sv=str(), saveSelectionToShelf=bool(), svs=bool(), select=list, sl=list, selectAll=bool(),
                           sla=bool(), stackTrace=bool(), st=bool(), statusBarMessage=str(), sbm=str(),
                           suppressErrors=bool(), se=bool(), suppressInfo=bool(), si=bool(), suppressResults=bool(),
                           sr=bool(), suppressStackTrace=bool(), sst=bool(), suppressWarnings=bool(), sw=bool(),
                           text=str(), t=str(), textLength=bool(), tl=bool(), useTemplate=str(), ut=str(),
                           visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
                           *args, **kwargs):
    pass


def cmdShell(annotation=str(), ann=str(), backgroundColor=list, bgc=list, clear=bool(), cl=bool(), command=str(),
             c=str(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
             dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
             enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(),
             height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(), manage=bool(),
             m=bool(), noBackground=bool(), nbg=bool(), numberOfHistoryLines=int(), nhl=int(),
             numberOfPopupMenus=bool(), npm=bool(), numberOfSavedLines=int(), nsl=int(), parent=str(), p=str(),
             popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), prompt=str(), pr=str(),
             statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
             visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def coarsenSubdivSelectionList(*args, **kwargs):
    pass


def collision(friction=float(), f=float(), name=str(), n=str(), offset=float(), o=float(), resilience=float(),
              r=float(), *args, **kwargs):
    pass


def color(rgbColor=list, rgb=list, userDefined=int(), ud=int(), *args, **kwargs):
    pass


def colorAtPoint(coordU=float(), u=float(), coordV=float(), v=float(), maxU=float(), xu=float(), maxV=float(),
                 xv=float(), minU=float(), mu=float(), minV=float(), mv=float(), output=str(), o=str(), samplesU=int(),
                 su=int(), samplesV=int(), sv=int(), *args, **kwargs):
    pass


def colorEditor(alpha=float(), a=float(), hsvValue=list, hsv=list, mini=bool(), m=bool(), parent=str(), p=str(),
                position=list, pos=list, result=bool(), r=bool(), rgbValue=list, rgb=list, *args, **kwargs):
    pass


def colorIndex(hueSaturationValue=bool(), hsv=bool(), resetToFactory=bool(), rf=bool(), resetToSaved=bool(), rs=bool(),
               *args, **kwargs):
    pass


def colorIndexSliderGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                        ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                        adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                        changeCommand=str(), cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list,
                        columnAlign3=list, cl3=list, columnAlign4=list, cl4=list, columnAlign5=list, cl5=list,
                        columnAlign6=list, cl6=list, columnAttach=list, cat=list, columnAttach2=list, ct2=list,
                        columnAttach3=list, ct3=list, columnAttach4=list, ct4=list, columnAttach5=list, ct5=list,
                        columnAttach6=list, ct6=list, columnOffset2=list, co2=list, columnOffset3=list, co3=list,
                        columnOffset4=list, co4=list, columnOffset5=list, co5=list, columnOffset6=list, co6=list,
                        columnWidth=list, cw=list, columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list,
                        columnWidth3=list, cw3=list, columnWidth4=list, cw4=list, columnWidth5=list, cw5=list,
                        columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                        dragCallback=str(), dgc=str(), dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(),
                        enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                        ekf=bool(), exists=bool(), ex=bool(), extraLabel=str(), el=str(), forceDragRefresh=bool(),
                        fdr=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list,
                        hlc=list, invisible=int(), inv=int(), isObscured=bool(), io=bool(), label=str(), l=str(),
                        manage=bool(), m=bool(), maxValue=int(), max=int(), minValue=int(), min=int(),
                        noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                        popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rowAttach=list, rat=list,
                        statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), value=int(), v=int(),
                        visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                        **kwargs):
    pass


def colorInputWidgetGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                        ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                        adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                        changeCommand=str(), cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list,
                        columnAlign3=list, cl3=list, columnAlign4=list, cl4=list, columnAlign5=list, cl5=list,
                        columnAlign6=list, cl6=list, columnAttach=list, cat=list, columnAttach2=list, ct2=list,
                        columnAttach3=list, ct3=list, columnAttach4=list, ct4=list, columnAttach5=list, ct5=list,
                        columnAttach6=list, ct6=list, columnOffset2=list, co2=list, columnOffset3=list, co3=list,
                        columnOffset4=list, co4=list, columnOffset5=list, co5=list, columnOffset6=list, co6=list,
                        columnWidth=list, cw=list, columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list,
                        columnWidth3=list, cw3=list, columnWidth4=list, cw4=list, columnWidth5=list, cw5=list,
                        columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                        dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                        enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                        ex=bool(), forceDragRefresh=bool(), fdr=bool(), fullPathName=bool(), fpn=bool(), height=int(),
                        h=int(), highlightColor=list, hlc=list, hsvValue=list, hsv=list, isObscured=bool(), io=bool(),
                        label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                        numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                        preventOverride=bool(), po=bool(), rgbValue=list, rgb=list, rowAttach=list, rat=list,
                        statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                        visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def colorManagementCatalog(addTransform=str(), adt=str(), editUserTransformPath=str(), eut=str(),
                           listSupportedExtensions=bool(), lse=bool(), listTransformConnections=bool(), ltc=bool(),
                           path=str(), pth=str(), queryUserTransformPath=bool(), qut=bool(), removeTransform=str(),
                           rmt=str(), transformConnection=str(), tcn=str(), type=str(), typ=str(), *args, **kwargs):
    pass


def colorManagementConvert(toDisplaySpace=list, tds=list, *args, **kwargs):
    pass


def colorManagementFileRules(addRule=str(), add=str(), colorSpace=str(), cs=str(), colorSpaceDescription=str(),
                             csd=str(), colorSpaceFamilies=str(), csf=str(), colorSpaceNames=bool(), csn=bool(),
                             down=str(), dwn=str(), enabled=bool(), ena=bool(), evaluate=str(), ev=str(),
                             extension=str(), ext=str(), listRules=bool(), lsr=bool(), load=bool(), ld=bool(),
                             moveUp=str(), up=str(), pattern=str(), pat=str(), remove=str(), rm=str(),
                             restoreDefaults=bool(), rde=bool(), save=bool(), sav=bool(), *args, **kwargs):
    pass


def colorManagementPrefs(cmConfigFileEnabled=bool(), cfe=bool(), cmEnabled=bool(), cme=bool(),
                         colorManageAllNodes=bool(), cma=bool(), colorManagePots=bool(), cmp=bool(),
                         colorManagedNodes=bool(), cmn=bool(), colorManagementSDKVersion=str(), cmv=str(),
                         configFilePath=str(), cfp=str(), configFileVersion=str(), cfv=str(),
                         defaultInputSpaceName=str(), din=str(), displayName=str(), dn=str(), displayNames=bool(),
                         dns=bool(), equalsToPolicyFile=str(), etp=str(), exportPolicy=str(), epy=str(),
                         inhibitEvents=bool(), ie=bool(), inputSpaceDescription=str(), isd=str(),
                         inputSpaceFamilies=str(), isf=str(), inputSpaceNames=bool(), iss=bool(), loadPolicy=str(),
                         lpy=str(), loadedDefaultInputSpaceName=str(), ldn=str(), loadedDisplayName=str(), ld=str(),
                         loadedOutputTransformName=str(), lon=str(), loadedRenderingSpaceName=str(), lrn=str(),
                         loadedViewName=str(), lv=str(), loadedViewTransformName=str(), lvn=str(),
                         missingColorSpaceNodes=bool(), mcn=bool(), ocioRulesEnabled=bool(), ore=bool(),
                         ociov2Enabled=bool(), oci=bool(), outputTarget=str(), ott=str(), outputTransformEnabled=bool(),
                         ote=bool(), outputTransformName=str(), otn=str(), outputTransformNames=bool(), ots=bool(),
                         outputTransformUseColorConversion=bool(), otc=bool(), outputUseViewTransform=bool(),
                         ovt=bool(), policyFileName=str(), pfn=str(), popupOnError=bool(), poe=bool(), refresh=bool(),
                         rfr=bool(), renderingSpaceName=str(), rsn=str(), renderingSpaceNames=bool(), rss=bool(),
                         restoreDefaults=bool(), rde=bool(), viewName=str(), vn=str(), viewNames=bool(), vns=bool(),
                         viewTransformName=str(), vtn=str(), viewTransformNames=bool(), vts=bool(), *args, **kwargs):
    pass


def colorSliderButtonGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                         ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                         adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list,
                         bgc=list, buttonCommand=str(), bc=str(), buttonLabel=str(), bl=str(), changeCommand=str(),
                         cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list, columnAlign3=list, cl3=list,
                         columnAlign4=list, cl4=list, columnAlign5=list, cl5=list, columnAlign6=list, cl6=list,
                         columnAttach=list, cat=list, columnAttach2=list, ct2=list, columnAttach3=list, ct3=list,
                         columnAttach4=list, ct4=list, columnAttach5=list, ct5=list, columnAttach6=list, ct6=list,
                         columnOffset2=list, co2=list, columnOffset3=list, co3=list, columnOffset4=list, co4=list,
                         columnOffset5=list, co5=list, columnOffset6=list, co6=list, columnWidth=list, cw=list,
                         columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list, columnWidth3=list, cw3=list,
                         columnWidth4=list, cw4=list, columnWidth5=list, cw5=list, columnWidth6=list, cw6=list,
                         defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                         dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                         enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                         ex=bool(), forceDragRefresh=bool(), fdr=bool(), fullPathName=bool(), fpn=bool(), height=int(),
                         h=int(), highlightColor=list, hlc=list, hsvValue=list, hsv=list, image=str(), i=str(),
                         isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(), m=bool(),
                         noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                         popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rgbValue=list, rgb=list,
                         rowAttach=list, rat=list, statusBarMessage=str(), sbm=str(), symbolButtonCommand=str(),
                         sbc=str(), symbolButtonDisplay=bool(), sbd=bool(), useTemplate=str(), ut=str(), visible=bool(),
                         vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def colorSliderGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                   ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                   adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                   changeCommand=str(), cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list,
                   columnAlign3=list, cl3=list, columnAlign4=list, cl4=list, columnAlign5=list, cl5=list,
                   columnAlign6=list, cl6=list, columnAttach=list, cat=list, columnAttach2=list, ct2=list,
                   columnAttach3=list, ct3=list, columnAttach4=list, ct4=list, columnAttach5=list, ct5=list,
                   columnAttach6=list, ct6=list, columnOffset2=list, co2=list, columnOffset3=list, co3=list,
                   columnOffset4=list, co4=list, columnOffset5=list, co5=list, columnOffset6=list, co6=list,
                   columnWidth=list, cw=list, columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list,
                   columnWidth3=list, cw3=list, columnWidth4=list, cw4=list, columnWidth5=list, cw5=list,
                   columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                   dragCallback=str(), dgc=str(), dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(),
                   enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                   ekf=bool(), exists=bool(), ex=bool(), forceDragRefresh=bool(), fdr=bool(), fullPathName=bool(),
                   fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, hsvValue=list, hsv=list,
                   isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(),
                   nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(),
                   pma=bool(), preventOverride=bool(), po=bool(), rgbValue=list, rgb=list, rowAttach=list, rat=list,
                   statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                   visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def columnLayout(adjustableColumn=bool(), adj=bool(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                 childArray=bool(), ca=bool(), columnAlign=str(), cal=str(), columnAttach=list, cat=list,
                 columnOffset=list, co=list, columnWidth=int(), cw=int(), defineTemplate=str(), dt=str(), docTag=str(),
                 dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                 enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
                 fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                 isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                 numberOfChildren=bool(), nch=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                 popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rowSpacing=int(), rs=int(),
                 statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                 visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def combinationShape(addDriver=bool(), add=bool(), allDrivers=bool(), ald=bool(), blendShape=str(), bs=str(),
                     combinationTargetIndex=int(), cti=int(), combinationTargetName=str(), ctn=str(),
                     combineMethod=int(), cm=int(), driverTargetIndex=int(), dti=int(), driverTargetName=str(),
                     dtn=str(), exist=bool(), ex=bool(), removeDriver=bool(), rmd=bool(), *args, **kwargs):
    pass


def commandEcho(addFilter=list, af=list, filter=list, f=list, lineNumbers=bool(), ln=bool(), state=bool(), st=bool(),
                *args, **kwargs):
    pass


def commandLine(annotation=str(), ann=str(), backgroundColor=list, bgc=list, command=str(), c=str(),
                defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                enableKeyboardFocus=bool(), ekf=bool(), enterCommand=str(), ec=str(), exists=bool(), ex=bool(),
                fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, holdFocus=bool(),
                hf=bool(), inputAnnotation=str(), ian=str(), isObscured=bool(), io=bool(), manage=bool(), m=bool(),
                noBackground=bool(), nbg=bool(), numberOfHistoryLines=int(), nhl=int(), numberOfPopupMenus=bool(),
                npm=bool(), outputAnnotation=str(), oan=str(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                preventOverride=bool(), po=bool(), sourceType=str(), st=str(), statusBarMessage=str(), sbm=str(),
                useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                width=int(), w=int(), *args, **kwargs):
    pass


def commandLogging(historySize=int(), hs=int(), logCommands=bool(), lc=bool(), logFile=str(), lf=str(),
                   recordCommands=bool(), rc=bool(), resetLogFile=bool(), rl=bool(), *args, **kwargs):
    pass


def commandPort(bufferSize=int(), bs=int(), close=bool(), cl=bool(), echoOutput=bool(), eo=bool(), listPorts=bool(),
                lp=bool(), name=str(), n=str(), noreturn=bool(), nr=bool(), pickleOutput=bool(), po=bool(),
                prefix=str(), pre=str(), returnNumCommands=bool(), rnc=bool(), securityWarning=bool(), sw=bool(),
                sourceType=str(), stp=str(), *args, **kwargs):
    pass


def componentBox(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(),
                 docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
                 en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), execute=list,
                 exe=list, exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                 highlightColor=list, hlc=list, isObscured=bool(), io=bool(), labelWidth=int(), lw=int(), manage=bool(),
                 m=bool(), maxHeight=int(), mh=int(), maxWidth=int(), mw=int(), noBackground=bool(), nbg=bool(),
                 numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                 precision=int(), pre=int(), preventOverride=bool(), po=bool(), rowHeight=int(), rh=int(),
                 selectedAttr=bool(), sla=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
                 visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                 **kwargs):
    pass


def componentEditor(control=bool(), ctl=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), exists=bool(),
                    ex=bool(), filter=str(), f=str(), floatField=str(), ff=str(), floatSlider=str(), fs=str(),
                    forceMainConnection=str(), fmc=str(), hidePathName=bool(), hpn=bool(), hideZeroColumns=bool(),
                    hzc=bool(), highlightConnection=str(), hlc=str(), justifyHeaders=int(), jh=int(), lockInput=bool(),
                    li=bool(), lockMainConnection=bool(), lck=bool(), mainListConnection=str(), mlc=str(), newTab=list,
                    nt=list, operationCount=bool(), oc=bool(), operationLabels=bool(), ol=bool(), operationType=int(),
                    ot=int(), panel=str(), pnl=str(), parent=str(), p=str(), precision=int(), pre=int(),
                    removeTab=str(), rt=str(), selected=bool(), sl=bool(), selectionConnection=str(), slc=str(),
                    setOperationLabel=list, sol=list, showNamespaces=bool(), sn=bool(), showObjects=bool(), so=bool(),
                    showSelected=bool(), ss=bool(), sortAlpha=bool(), sa=bool(), stateString=bool(), sts=bool(),
                    unParent=bool(), up=bool(), unlockMainConnection=bool(), ulk=bool(), updateMainConnection=bool(),
                    upd=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def condition(delete=bool(), dependency=str(), d=str(), initialize=bool(), i=bool(), script=str(), s=str(),
              state=bool(), st=bool(), *args, **kwargs):
    pass


def cone(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), degree=int(), d=int(),
         endSweep=float(), esw=float(), heightRatio=float(), hr=float(), name=str(), n=str(), nodeState=int(),
         nds=int(), object=bool(), o=bool(), pivot=list, p=list, polygon=int(), po=int(), radius=float(), r=float(),
         sections=int(), s=int(), spans=int(), nsp=int(), startSweep=float(), ssw=float(), tolerance=float(),
         tol=float(), useOldInitBehaviour=bool(), oib=bool(), useTolerance=bool(), ut=bool(), *args, **kwargs):
    pass


def confirmDialog(annotation=str(), ann=str(), backgroundColor=list, bgc=list, button=str(), b=str(),
                  cancelButton=str(), cb=str(), defaultButton=str(), db=str(), dismissString=str(), ds=str(),
                  icon=str(), icn=str(), message=str(), m=str(), messageAlign=str(), ma=str(), parent=str(), p=str(),
                  title=str(), t=str(), *args, **kwargs):
    pass


def connectAttr(source_attr: str, destination_attr: str, force=bool(), f=bool(), lock=bool(), l=bool(), nextAvailable=bool(),
                na=bool(), referenceDest=str(), rd=str(), *args, **kwargs):
    mod = om.MDGModifier()
    as_objects = [
        _attr_name_to_mobject_and_plug(source_attr),
        _attr_name_to_mobject_and_plug(destination_attr)
    ]
    mod.connect(*as_objects[0], *as_objects[1])
    mod.doIt()


def connectControl(fileName=bool(), fi=bool(), index=int(), preventContextualMenu=bool(), pcm=bool(),
                   preventOverride=bool(), po=bool(), *args, **kwargs):
    pass


def connectDynamic(addScriptHandler=str(), ash=str(), collisions=str(), c=str(), delete=bool(), d=bool(),
                   emitters=str(), em=str(), fields=str(), f=str(), removeScriptHandler=int(), rsh=int(), *args,
                   **kwargs):
    pass


def connectionInfo(destinationFromSource=bool(), dfs=bool(), getExactDestination=bool(), ged=bool(),
                   getExactSource=bool(), ges=bool(), getLockedAncestor=bool(), gla=bool(), isDestination=bool(),
                   id=bool(), isExactDestination=bool(), ied=bool(), isExactSource=bool(), ies=bool(), isLocked=bool(),
                   il=bool(), isSource=bool(), sourceFromDestination=bool(), sfd=bool(), *args, **kwargs):
    pass


def connectJoint(connectMode=bool(), cm=bool(), parentMode=bool(), pm=bool(), *args, **kwargs):
    pass


def constrain(barrier=bool(), br=bool(), damping=float(), d=float(), directionalHinge=bool(), dhi=bool(), hinge=bool(),
              hi=bool(), interpenetrate=bool(), i=bool(), nail=bool(), na=bool(), name=str(), n=str(), orientation=list,
              o=list, pinConstraint=bool(), pin=bool(), position=list, p=list, restLength=float(), rl=float(),
              spring=bool(), s=bool(), stiffness=float(), st=float(), *args, **kwargs):
    pass


def constructionHistory(toggle=bool(), tgl=bool(), *args, **kwargs):
    pass


def container(addNode=list, an=list, asset=list, a=list, assetMember=str(), am=str(), bindAttr=list, ba=list,
              connectionList=bool(), cl=bool(), current=bool(), c=bool(), fileName=list, fn=list, findContainer=list,
              fc=list, force=bool(), f=bool(), includeHierarchyAbove=bool(), iha=bool(), includeHierarchyBelow=bool(),
              ihb=bool(), includeNetwork=bool(), inc=bool(), includeNetworkDetails=str(), ind=str(),
              includeShaders=bool(), isd=bool(), includeShapes=bool(), ish=bool(), includeTransform=bool(), it=bool(),
              isContainer=bool(), isc=bool(), name=str(), n=str(), nodeList=bool(), nl=bool(), nodeNamePrefix=bool(),
              nnp=bool(), parentContainer=bool(), par=bool(), preview=bool(), p=bool(), publishAndBind=list, pb=list,
              publishAsChild=list, pac=list, publishAsParent=list, pap=list, publishAsRoot=list, pro=list,
              publishAttr=str(), pa=str(), publishConnections=bool(), pc=bool(), publishName=str(), pn=str(),
              removeContainer=bool(), rc=bool(), removeNode=list, rn=list, type=str(), typ=str(),
              unbindAndUnpublish=str(), ubp=str(), unbindAttr=list, ua=list, unbindChild=str(), unc=str(),
              unbindParent=str(), unp=str(), unpublishChild=str(), upc=str(), unpublishName=str(), un=str(),
              unpublishParent=str(), upp=str(), unsortedOrder=bool(), uso=bool(), *args, **kwargs):
    pass


def containerBind(allNames=bool(), all=bool(), bindingSet=str(), bs=str(), bindingSetConditions=bool(), bsc=bool(),
                  bindingSetList=bool(), bsl=bool(), force=bool(), f=bool(), preview=bool(), p=bool(), *args, **kwargs):
    pass


def containerProxy(fromTemplate=str(), ft=str(), type=str(), typ=str(), *args, **kwargs):
    pass


def containerPublish(bindNode=list, bn=list, bindTemplateStandins=bool(), bts=bool(), inConnections=bool(), ic=bool(),
                     mergeShared=bool(), ms=bool(), outConnections=bool(), oc=bool(), publishNode=list, pn=list,
                     unbindNode=str(), ubn=str(), unpublishNode=str(), upn=str(), *args, **kwargs):
    pass


def containerTemplate(addBindingSet=str(), abs=str(), addNames=bool(), an=bool(), addView=str(), av=str(),
                      allKeyable=bool(), ak=bool(), attribute=str(), at=str(), attributeList=str(), al=str(),
                      baseName=str(), bn=str(), bindingSetList=str(), bsl=str(), childAnchor=bool(), can=bool(),
                      delete=bool(), d=bool(), exists=bool(), ex=bool(), expandCompounds=bool(), ec=bool(),
                      fileName=str(), fn=str(), force=bool(), f=bool(), fromContainer=str(), fc=str(),
                      fromSelection=bool(), fs=bool(), layoutMode=int(), lm=int(), load=bool(), l=bool(),
                      matchFile=str(), mf=str(), matchName=str(), mn=str(), parentAnchor=bool(), pan=bool(),
                      publishedNodeList=str(), pnl=str(), removeBindingSet=str(), rbs=str(), removeView=str(), rv=str(),
                      rootTransform=bool(), rtn=bool(), save=bool(), s=bool(), searchPath=str(), sp=str(),
                      silent=bool(), si=bool(), templateList=str(), tl=str(), unload=bool(), u=bool(),
                      updateBindingSet=str(), ubs=str(), useHierarchy=bool(), uh=bool(), viewList=str(), vl=str(),
                      *args, **kwargs):
    pass


def containerView(itemInfo=str(), ii=str(), itemList=bool(), il=bool(), viewDescription=bool(), vd=bool(),
                  viewLabel=bool(), vb=bool(), viewList=bool(), vl=bool(), viewName=str(), vn=str(), *args, **kwargs):
    pass


def contentBrowser(addContentPath=str(), acp=str(), context=list, ctx=list, control=bool(), ctl=bool(),
                   defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), exists=bool(), ex=bool(), filter=str(),
                   f=str(), forceMainConnection=str(), fmc=str(), highlightConnection=str(), hlc=str(), location=str(),
                   loc=str(), lockMainConnection=bool(), lck=bool(), mainListConnection=str(), mlc=str(), panel=str(),
                   pnl=str(), parent=str(), p=str(), preview=bool(), pv=bool(), refreshTreeView=bool(), rtv=bool(),
                   removeContentPath=str(), rcp=str(), saveCurrentContext=bool(), scc=bool(), selectionConnection=str(),
                   slc=str(), stateString=bool(), sts=bool(), thumbnailView=bool(), th=bool(), treeView=bool(),
                   tr=bool(), unParent=bool(), up=bool(), unlockMainConnection=bool(), ulk=bool(),
                   updateMainConnection=bool(), upd=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def contextInfo(c=bool(), escapeContext=bool(), esc=bool(), exists=bool(), ex=bool(), image1=bool(), i1=bool(),
                image2=bool(), i2=bool(), image3=bool(), i3=bool(), title=bool(), t=bool(), *args, **kwargs):
    pass


def control(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(), docTag=str(),
            dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
            enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
            fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(),
            io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(),
            parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
            statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
            visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def controller(allControllers=bool(), ac=bool(), children=bool(), cld=bool(), group=bool(), g=bool(), index=int(),
               idx=int(), isController=str(), ic=str(), parent=bool(), p=bool(), pickWalkDown=bool(), pwd=bool(),
               pickWalkLeft=bool(), pwl=bool(), pickWalkRight=bool(), pwr=bool(), pickWalkUp=bool(), pwu=bool(),
               unparent=bool(), unp=bool(), *args, **kwargs):
    pass


def convertIffToPsd(iffFileName=str(), ifn=str(), psdFileName=str(), pfn=str(), xResolution=int(), xr=int(),
                    yResolution=int(), yr=int(), *args, **kwargs):
    pass


def convertSolidTx(alpha=bool(), al=bool(), antiAlias=bool(), aa=bool(), backgroundColor=list, bc=list,
                   backgroundMode=str(), bm=str(), camera=str(), cam=str(), componentRange=bool(), cr=bool(),
                   doubleSided=bool(), ds=bool(), fileFormat=str(), fil=str(), fileImageName=str(), fin=str(),
                   fillTextureSeams=bool(), fts=bool(), force=bool(), f=bool(), fullUvRange=bool(), fur=bool(),
                   name=str(), n=str(), pixelFormat=str(), pf=str(), resolutionX=int(), rx=int(), resolutionY=int(),
                   ry=int(), reuseDepthMap=bool(), rdm=bool(), samplePlane=bool(), sp=bool(), samplePlaneRange=list,
                   spr=list, shadows=bool(), sh=bool(), uvBBoxIntersect=bool(), ubi=bool(), uvRange=list, uvr=list,
                   uvSetName=str(), uv=str(), *args, **kwargs):
    pass


def convertTessellation(allCameras=bool(), acm=bool(), camera=str(), cam=str(), *args, **kwargs):
    pass


def convertUnit(fromUnit=str(), f=str(), toUnit=str(), t=str(), *args, **kwargs):
    pass


def copyAttr(attribute=str(), at=str(), containerParentChild=bool(), cpc=bool(), inConnections=bool(), ic=bool(),
             keepSourceConnections=bool(), ksc=bool(), outConnections=bool(), oc=bool(), renameTargetContainer=bool(),
             rtc=bool(), values=bool(), v=bool(), *args, **kwargs):
    pass


def copyDeformerWeights(destinationDeformer=str(), dd=str(), destinationShape=str(), ds=str(), mirrorInverse=bool(),
                        mi=bool(), mirrorMode=str(), mm=str(), noMirror=bool(), nm=bool(), smooth=bool(), sm=bool(),
                        sourceDeformer=str(), sd=str(), sourceShape=str(), ss=str(), surfaceAssociation=str(), sa=str(),
                        uvSpace=list, uv=list, *args, **kwargs):
    pass


def copyFlexor(*args, **kwargs):
    pass


def copyKey(animLayer=str(), al=str(), animation=str(), an=str(), attribute=str(), at=str(), clipboard=str(), cb=str(),
            controlPoints=bool(), cp=bool(), float=tuple(), f=tuple(), forceIndependentEulerAngles=bool(), fea=bool(),
            hierarchy=str(), hi=str(), includeUpperBound=bool(), iub=bool(), index=int(), option=str(), o=str(),
            shape=bool(), s=bool(), time=tuple(), t=tuple(), *args, **kwargs):
    pass


def copySkinWeights(destinationSkin=str(), ds=str(), influenceAssociation=str(), ia=str(), mirrorInverse=bool(),
                    mi=bool(), mirrorMode=str(), mm=str(), noBlendWeight=bool(), nbw=bool(), noMirror=bool(), nm=bool(),
                    normalize=bool(), nr=bool(), sampleSpace=int(), spa=int(), smooth=bool(), sm=bool(),
                    sourceSkin=str(), ss=str(), surfaceAssociation=str(), sa=str(), uvSpace=list, uv=list, *args,
                    **kwargs):
    pass


def crashInfo(crashFile=bool(), cf=bool(), savedBeforeCrash=bool(), sbc=bool(), *args, **kwargs):
    pass


def createAttrPatterns(patternDefinition=str(), pd=str(), patternFile=str(), pf=str(), patternType=str(), pt=str(),
                       *args, **kwargs):
    pass


def createDisplayLayer(empty=bool(), e=bool(), makeCurrent=bool(), mc=bool(), name=str(), n=str(), noRecurse=bool(),
                       nr=bool(), number=int(), num=int(), *args, **kwargs):
    pass


def createEditor(noCloseOnDelete=bool(), nc=bool(), queueForDelete=bool(), qfd=bool(), *args, **kwargs):
    pass


def createLayeredPsdFile(imageFileName=list, ifn=list, psdFileName=str(), psf=str(), xResolution=int(), xr=int(),
                         yResolution=int(), yr=int(), *args, **kwargs):
    pass


def createNode(node_type: str, name=str(), n=str(), parent=str(), p=str(), shared=bool(), s=bool(),
               skipSelect=bool(), ss=bool(),
               *args, **kwargs):
    if not any((name, n)):
        if shape_type := node_types_to_shapes.NODE_TYPES_TO_SHAPES.get(node_type):
            name = shape_type['child_name']
        else:
            name=f'{node_type}1'
    name = _hierarchy.find_first_available_name(name or n, parent_name=parent if parent != str() else None)

    # try to create as dag node, if it fails it defaults to dependency node
    try:
        if parent:
            parent_mobject = _hierarchy.NodePool.from_name(parent)
            if not parent_mobject:
                # If given a parent, but it doesn't exist yet, create if first
                sl_ls = om.MSelectionList()
                sl_ls.add(parent)
                parent_mobject = om.MFnDagNode().create(node_type, name or n, sl_ls.getDependNode(0))
            mobject = om.MFnDagNode().create(node_type, name or n, parent_mobject)
        else:
            # Assume all nodes are dag nodes. No way to know this unless we create a type map for all nodes...
            mobject = om.MFnDagNode().create(node_type, name or n)

    except RuntimeError:
        mobject = om.MFnDependencyNode(node_type, name or n)

    if len(mobject._children) > 0:
        mobject = mobject._children[0]

    if not skipSelect and not ss:
        ACTIVE_SELECTION.replace_all([mobject, ])
    
    return mobject._name


def createRenderLayer(empty=bool(), e=bool(), g=bool(), makeCurrent=bool(), mc=bool(), name=str(), n=str(),
                      noRecurse=bool(), nr=bool(), number=int(), num=int(), *args, **kwargs):
    pass


def createSubdivRegion(*args, **kwargs):
    pass


def ctxAbort(*args, **kwargs):
    pass


def ctxCompletion(*args, **kwargs):
    pass


def ctxEditMode(buttonDown=bool(), btd=bool(), buttonUp=bool(), btu=bool(), *args, **kwargs):
    pass


def ctxTraverse(down=bool(), d=bool(), left=bool(), l=bool(), right=bool(), r=bool(), up=bool(), *args, **kwargs):
    pass


def currentCtx(*args, **kwargs):
    pass


def currentTime(update=bool(), u=bool(), *args, **kwargs):
    pass


def currentTimeCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                   image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def currentUnit(angle=str(), a=str(), fullName=bool(), f=bool(), linear=str(), l=str(), time=str(), t=str(),
                updateAnimation=bool(), ua=bool(), *args, **kwargs):
    pass


def curve(append=bool(), a=bool(), bezier=bool(), bez=bool(), degree=float(), d=float(), editPoint=list, ep=list,
          knot=float(), k=float(), name=str(), n=str(), objectSpace=bool(), os=bool(), periodic=bool(), per=bool(),
          point=list, p=list, pointWeight=list, pw=list, replace=bool(), r=bool(), worldSpace=bool(), ws=bool(), *args,
          **kwargs):
    pass


def curveAddPtCtx(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                  *args, **kwargs):
    pass


def curveCVCtx(bezier=bool(), bez=bool(), degree=int(), d=int(), exists=bool(), ex=bool(), history=bool(), ch=bool(),
               image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), multEndKnots=bool(), me=bool(),
               name=str(), n=str(), preserveShape=bool(), ps=bool(), rational=bool(), rl=bool(), refit=bool(),
               rf=bool(), symmetry=bool(), sm=bool(), uniform=bool(), un=bool(), *args, **kwargs):
    pass


def curveEditorCtx(direction=int(), dir=int(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
                   i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(),
                   relativeTangentSize=float(), rts=float(), title=str(), t=str(), *args, **kwargs):
    pass


def curveEPCtx(bezier=bool(), bez=bool(), degree=int(), d=int(), exists=bool(), ex=bool(), history=bool(), ch=bool(),
               image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(),
               preserveShape=bool(), ps=bool(), preserveShapeFraction=float(), pf=float(), refit=bool(), rf=bool(),
               uniform=bool(), un=bool(), *args, **kwargs):
    pass


def curveIntersect(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), direction=list, d=list,
                   directionX=float(), dx=float(), directionY=float(), dy=float(), directionZ=float(), dz=float(),
                   nodeState=int(), nds=int(), tolerance=float(), tol=float(), useDirection=bool(), ud=bool(), *args,
                   **kwargs):
    pass


def curveMoveEPCtx(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                   *args, **kwargs):
    pass


def curveOnSurface(append=bool(), a=bool(), degree=float(), d=float(), knot=float(), k=float(), name=str(), n=str(),
                   periodic=bool(), per=bool(), positionUV=list, uv=list, replace=bool(), r=bool(), *args, **kwargs):
    pass


def curveRGBColor(hueSaturationValue=bool(), hsv=bool(), list=bool(), l=bool(), listNames=bool(), ln=bool(),
                  remove=bool(), r=bool(), resetToFactory=bool(), rf=bool(), resetToSaved=bool(), rs=bool(), *args,
                  **kwargs):
    pass


def curveSketchCtx(degree=int(), d=int(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(),
                   image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def cutKey(animation=str(), an=str(), attribute=str(), at=str(), clear=bool(), cl=bool(), controlPoints=bool(),
           cp=bool(), float=tuple(), f=tuple(), hierarchy=str(), hi=str(), includeUpperBound=bool(), iub=bool(),
           index=int(), option=str(), o=str(), selectKey=bool(), sl=bool(), shape=bool(), s=bool(), time=tuple(),
           t=tuple(), *args, **kwargs):
    pass


def cycleCheck(all=bool(), children=bool(), c=bool(), dag=bool(), evaluation=bool(), e=bool(), firstCycleOnly=bool(),
               fco=bool(), firstPlugPerNode=bool(), fpn=bool(), lastPlugPerNode=bool(), lpn=bool(), list=bool(),
               l=bool(), listSeparator=str(), ls=str(), parents=bool(), p=bool(), secondary=bool(), s=bool(),
               timeLimit=float(), tl=float(), *args, **kwargs):
    pass


def cylinder(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), degree=int(),
             d=int(), endSweep=float(), esw=float(), heightRatio=float(), hr=float(), name=str(), n=str(),
             nodeState=int(), nds=int(), object=bool(), o=bool(), pivot=list, p=list, polygon=int(), po=int(),
             radius=float(), r=float(), sections=int(), s=int(), spans=int(), nsp=int(), startSweep=float(),
             ssw=float(), tolerance=float(), tol=float(), useTolerance=bool(), ut=bool(), *args, **kwargs):
    pass


def dagObjectCompare(attribute=bool(), a=bool(), bail=str(), b=str(), connection=bool(), c=bool(), namespace=str(),
                     n=str(), relative=bool(), r=bool(), short=bool(), s=bool(), type=bool(), t=bool(), *args,
                     **kwargs):
    pass


def dagPose(addToPose=bool(), a=bool(), atPose=bool(), ap=bool(), bindPose=bool(), bp=bool(), g=bool(), members=bool(),
            m=bool(), name=str(), n=str(), remove=bool(), rm=bool(), reset=bool(), rs=bool(), restore=bool(), r=bool(),
            save=bool(), s=bool(), selection=bool(), sl=bool(), worldParent=bool(), wp=bool(), *args, **kwargs):
    pass


def dataStructure(asFile=str(), af=str(), asString=str(), dataType=bool(), dt=bool(), format=str(), fmt=str(),
                  listMemberNames=str(), lmn=str(), name=str(), n=str(), remove=bool(), rem=bool(), removeAll=bool(),
                  ral=bool(), *args, **kwargs):
    pass


def date(date=bool(), d=bool(), format=str(), f=str(), shortDate=bool(), sd=bool(), shortTime=bool(), st=bool(),
         time=bool(), t=bool(), *args, **kwargs):
    pass


def dbcount(enabled=bool(), e=bool(), file=str(), f=str(), keyword=str(), k=str(), list=bool(), l=bool(),
            maxdepth=int(), md=int(), quick=bool(), q=bool(), reset=bool(), r=bool(), spreadsheet=bool(), s=bool(),
            *args, **kwargs):
    pass


def dbfootprint(allObjects=bool(), all=bool(), outputFile=str(), of=str(), type=str(), t=str(), *args, **kwargs):
    pass


def dbmessage(file=str(), f=str(), list=bool(), l=bool(), monitor=bool(), m=bool(), type=str(), t=str(), *args,
              **kwargs):
    pass


def dbpeek(allObjects=bool(), all=bool(), argument=str(), a=str(), count=int(), c=int(), evaluationGraph=bool(),
           eg=bool(), operation=str(), op=str(), outputFile=str(), of=str(), *args, **kwargs):
    pass


def dbtrace(filter=str(), f=str(), info=bool(), i=bool(), keyword=str(), k=str(), mark=bool(), m=bool(), off=bool(),
            output=str(), o=str(), timed=bool(), tm=bool(), title=str(), t=str(), verbose=bool(), v=bool(), *args,
            **kwargs):
    pass


def defaultLightListCheckBox(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(),
                             dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(),
                             dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                             enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(),
                             fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(),
                             io=bool(), label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                             numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(),
                             pma=bool(), preventOverride=bool(), po=bool(), shadingGroup=str(), sg=str(),
                             statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                             visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def defaultNavigation(connectToExisting=bool(), ce=bool(), createNew=bool(), cn=bool(), defaultAttribute=bool(),
                      da=bool(), defaultTraversal=bool(), dtv=bool(), defaultWorkingNode=bool(), dwn=bool(),
                      delete=bool(), destination=str(), d=str(), disconnect=bool(), dis=bool(), force=bool(), f=bool(),
                      ignore=bool(), i=bool(), navigatorDecisionString=str(), nds=str(), quiet=bool(), qt=bool(),
                      relatedNodes=bool(), ren=bool(), source=str(), s=str(), unignore=bool(), u=bool(), *args,
                      **kwargs):
    pass


def defineDataServer(device=str(), d=str(), server=str(), s=str(), undefine=bool(), u=bool(), *args, **kwargs):
    pass


def defineVirtualDevice(axis=int(), ax=int(), channel=str(), c=str(), clear=bool(), cl=bool(), create=bool(), cr=bool(),
                        device=str(), d=str(), parent=str(), p=str(), undefine=bool(), u=bool(), usage=str(), use=str(),
                        *args, **kwargs):
    pass


def deformableShape(chain=bool(), ch=bool(), createOriginalGeometry=bool(), cog=bool(), createTweakNode=bool(),
                    ctw=bool(), createUpstreamTagInjectionNode=bool(), cti=bool(), frontOfChain=bool(), foc=bool(),
                    localShapeInAttr=bool(), lsi=bool(), localShapeOutAttr=bool(), lso=bool(), nodeChain=bool(),
                    nch=bool(), originalGeometry=bool(), og=bool(), outputPlugChain=bool(), och=bool(),
                    plugChain=bool(), pch=bool(), tagInjectionList=bool(), til=bool(), tagInjectionNode=bool(),
                    ti=bool(), tweakNode=bool(), tw=bool(), upstreamTagInjectionNode=bool(), uti=bool(),
                    worldShapeOutAttr=bool(), wso=bool(), *args, **kwargs):
    pass


def deformer(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(), deformerTools=bool(),
             dt=bool(), exclusive=str(), ex=str(), frontOfChain=bool(), foc=bool(), geometry=str(), g=str(),
             geometryIndices=bool(), gi=bool(), ignoreSelected=bool(), includeHiddenSelections=bool(), ihs=bool(),
             name=str(), n=str(), parallel=bool(), par=bool(), prune=bool(), pr=bool(), remove=bool(), rm=bool(),
             split=bool(), sp=bool(), type=str(), typ=str(), useComponentTags=bool(), uct=bool(), *args, **kwargs):
    pass


def deformerEvaluator(active=bool(), act=bool(), asNodeName=bool(), nm=bool(), asText=bool(), txt=bool(), chains=bool(),
                      c=bool(), deformerChain=bool(), dch=bool(), deformers=bool(), d=bool(), dumpInfo=bool(),
                      di=bool(), list=bool(), ls=bool(), members=bool(), mbr=bool(), meshes=bool(), m=bool(),
                      message=bool(), msg=bool(), nodeError=bool(), ner=bool(), nodeState=bool(), ns=bool(),
                      verbose=bool(), v=bool(), *args, **kwargs):
    pass


def deformerWeights(attribute=str(), at=str(), defaultValue=float(), dv=float(), deformer=str(), df=str(),
                    export=bool(), ex=bool(), format=str(), fm=str(), ignoreName=bool(), ig=bool(), im=bool(),
                    method=str(), m=str(), path=str(), p=str(), positionTolerance=float(), pt=float(), remap=str(),
                    r=str(), shape=str(), sh=str(), skip=str(), sk=str(), vertexConnections=bool(), vc=bool(),
                    weightPrecision=int(), wp=int(), weightTolerance=float(), wt=float(), worldSpace=bool(), ws=bool(),
                    *args, **kwargs):
    pass


def delete(objects, all=bool(), attribute=str(), at=str(), channels=bool(), c=bool(), constraints=bool(), cn=bool(),
           constructionHistory=bool(), ch=bool(), controlPoints=bool(), cp=bool(), expressions=bool(), e=bool(),
           hierarchy=str(), hi=str(), inputConnectionsAndNodes=bool(), icn=bool(), motionPaths=bool(), mp=bool(),
           shape=bool(), s=bool(), staticChannels=bool(), sc=bool(), timeAnimationCurves=bool(), tac=bool(),
           unitlessAnimationCurves=bool(), uac=bool()):

    if not isinstance(objects, (list, tuple, str)):
        raise ValueError(f'Expected objects to be a list, tuple, or string. Got: {type(objects)}')
    
    if isinstance(objects, str):
        objects = [objects,]
    
    for obj in objects:
        mobject = _hierarchy.NodePool.from_name(obj)
        if not mobject:
            raise ValueError(f'No object matches name: {obj}.')
        om._NODE_REMOVED_SIGNAL.send(mobject)



def deleteAttr(attribute=str(), at=str(), *args, **kwargs):
    pass


def deleteAttrPattern(allPatterns=bool(), all=bool(), patternName=str(), pn=str(), patternType=str(), pt=str(), *args,
                      **kwargs):
    pass


def deleteExtension(attribute=str(), at=str(), forceDelete=bool(), fd=bool(), nodeType=str(), nt=str(), *args,
                    **kwargs):
    pass


def deleteUI(collection=bool(), cl=bool(), control=bool(), ctl=bool(), editor=bool(), ed=bool(), layout=bool(),
             lay=bool(), menu=bool(), m=bool(), menuItem=bool(), mi=bool(), panel=bool(), pnl=bool(),
             panelConfig=bool(), pc=bool(), radioMenuItemCollection=bool(), ric=bool(), toolContext=bool(), tc=bool(),
             uiTemplate=bool(), uit=bool(), window=bool(), wnd=bool(), *args, **kwargs):
    pass


def deltaMush(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(), deformerTools=bool(),
              dt=bool(), envelope=float(), en=float(), exclusive=str(), ex=str(), frontOfChain=bool(), foc=bool(),
              geometry=str(), g=str(), geometryIndices=bool(), gi=bool(), ignoreSelected=bool(),
              includeHiddenSelections=bool(), ihs=bool(), inwardConstraint=float(), iwc=float(), name=str(), n=str(),
              outwardConstraint=float(), owc=float(), parallel=bool(), par=bool(), pinBorderVertices=bool(), pbv=bool(),
              prune=bool(), pr=bool(), remove=bool(), rm=bool(), smoothingIterations=int(), si=int(),
              smoothingStep=float(), ss=float(), split=bool(), sp=bool(), useComponentTags=bool(), uct=bool(), *args,
              **kwargs):
    pass


def detachCurve(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), curveOnSurface=bool(), cos=bool(),
                keep=bool(), k=bool(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(),
                parameter=float(), p=float(), replaceOriginal=bool(), rpo=bool(), *args, **kwargs):
    pass


def detachDeviceAttr(all=bool(), attribute=str(), at=str(), axis=str(), ax=str(), device=str(), d=str(),
                     selection=bool(), sl=bool(), *args, **kwargs):
    pass


def detachSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), direction=int(), d=int(),
                  keep=bool(), k=bool(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(),
                  parameter=float(), p=float(), replaceOriginal=bool(), rpo=bool(), *args, **kwargs):
    pass


def deviceEditor(control=bool(), ctl=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), exists=bool(),
                 ex=bool(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(), highlightConnection=str(),
                 hlc=str(), lockMainConnection=bool(), lck=bool(), mainListConnection=str(), mlc=str(), panel=str(),
                 pnl=str(), parent=str(), p=str(), selectionConnection=str(), slc=str(), stateString=bool(), sts=bool(),
                 takePath=str(), tp=str(), unParent=bool(), up=bool(), unlockMainConnection=bool(), ulk=bool(),
                 updateMainConnection=bool(), upd=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def deviceManager(attachment=bool(), att=bool(), axisCoordChanges=bool(), acc=bool(), axisIndex=int(), axi=int(),
                  axisName=bool(), axn=bool(), axisOffset=bool(), axo=bool(), axisScale=bool(), axs=bool(),
                  deviceIndex=int(), dvi=int(), deviceNameFromIndex=int(), dni=int(), numAxis=bool(), nax=bool(),
                  numDevices=bool(), ndv=bool(), *args, **kwargs):
    pass


def devicePanel(control=bool(), ctl=bool(), copy=str(), cp=str(), createString=bool(), cs=bool(), defineTemplate=str(),
                dt=str(), docTag=str(), dtg=str(), editString=bool(), es=bool(), exists=bool(), ex=bool(), init=bool(),
                isUnique=bool(), iu=bool(), label=str(), l=str(), menuBarRepeatLast=bool(), mrl=bool(),
                menuBarVisible=bool(), mbv=bool(), needsInit=bool(), ni=bool(), parent=str(), p=str(),
                popupMenuProcedure=str(), pmp=str(), replacePanel=str(), rp=str(), tearOff=bool(), to=bool(),
                tearOffCopy=str(), toc=str(), tearOffRestore=bool(), tor=bool(), unParent=bool(), up=bool(),
                useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def dgdirty(allPlugs=bool(), a=bool(), clean=bool(), c=bool(), implicit=bool(), i=bool(), list=str(), l=str(),
            propagation=bool(), p=bool(), showTiming=bool(), st=bool(), verbose=bool(), v=bool(), *args, **kwargs):
    pass


def dgeval(src=bool(), verbose=bool(), v=bool(), *args, **kwargs):
    pass


def dgfilter(attribute=str(), atr=str(), list=bool(), l=bool(), logicalAnd=list, logicalNot=str(), logicalOr=list,
             name=str(), n=str(), node=str(), nd=str(), nodeType=str(), nt=str(), plug=str(), p=str(), *args, **kwargs):
    pass


def dgInfo(allNodes=bool(), all=bool(), connections=bool(), c=bool(), dirty=bool(), d=bool(), nodes=bool(), n=bool(),
           nonDeletable=bool(), nd=bool(), outputFile=str(), of=str(), propagation=bool(), p=bool(), short=bool(),
           s=bool(), size=bool(), sz=bool(), subgraph=bool(), sub=bool(), type=str(), nt=str(), *args, **kwargs):
    pass


def dgmodified(*args, **kwargs):
    pass


def dgtimer(combineType=bool(), ct=bool(), hide=str(), hi=str(), hierarchy=bool(), h=bool(), maxDisplay=int(), m=int(),
            name=str(), n=str(), noHeader=bool(), nh=bool(), outputFile=str(), o=str(), overhead=bool(), oh=bool(),
            rangeLower=float(), rgl=float(), rangeUpper=float(), rgu=float(), reset=bool(), r=bool(), returnCode=str(),
            rc=str(), returnType=str(), rt=str(), show=str(), sh=str(), sortMetric=str(), sm=str(), sortType=str(),
            st=str(), threshold=float(), th=float(), timerOff=bool(), off=bool(), timerOn=bool(), on=bool(),
            trace=bool(), tr=bool(), type=str(), t=str(), uniqueName=bool(), un=bool(), updateHeatMap=int(), uhm=int(),
            *args, **kwargs):
    pass


def dgValidateCurve(allCurves=bool(), a=bool(), verbose=bool(), v=bool(), *args, **kwargs):
    pass


def dimWhen(clear=bool(), c=bool(), false=bool(), f=bool(), true=bool(), t=bool(), *args, **kwargs):
    pass


def directionalLight(decayRate=int(), d=int(), discRadius=float(), drs=float(), exclusive=bool(), exc=bool(),
                     intensity=float(), i=float(), name=str(), n=str(), position=list, pos=list, rgb=list,
                     rotation=list, rot=list, shadowColor=list, sc=list, shadowDither=float(), sd=float(),
                     shadowSamples=int(), sh=int(), softShadow=bool(), ss=bool(), useRayTraceShadows=bool(), rs=bool(),
                     *args, **kwargs):
    pass


def directKeyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                 image3=str(), i3=str(), name=str(), n=str(), option=str(), o=str(), selectedOnly=bool(), so=bool(),
                 *args, **kwargs):
    pass


def dirmap(convertDirectory=str(), cd=str(), enable=bool(), en=bool(), getAllMappings=bool(), gam=bool(),
           getMappedDirectory=str(), gmd=str(), mapDirectory=list, m=list, unmapDirectory=str(), um=str(), *args,
           **kwargs):
    pass


def disable(value=bool(), v=bool(), *args, **kwargs):
    pass


def disableIncorrectNameWarning(*args, **kwargs):
    pass


def disconnectAttr(attr1: str, attr2: str, nextAvailable=bool(), na=bool(), *args, **kwargs):
    mod = om.MDGModifier()

    as_objects = [
        _attr_name_to_mobject_and_plug(attr1),
        _attr_name_to_mobject_and_plug(attr2)
    ]
    mod.connect(*as_objects[0], *as_objects[1])
    mod.disconnect()
    mod.doIt()
    return f'{attr1} {attr2}'


def disconnectJoint(attachHandleMode=bool(), ahm=bool(), deleteHandleMode=bool(), dhm=bool(), *args, **kwargs):
    pass


def diskCache(append=bool(), a=bool(), cacheType=str(), ct=str(), close=str(), c=str(), closeAll=bool(), ca=bool(),
              delete=str(), d=str(), deleteAll=bool(), da=bool(), empty=str(), e=str(), emptyAll=bool(), ea=bool(),
              enabledCachesOnly=bool(), eco=bool(), endTime=float(), et=float(), frameRangeType=str(), frt=str(),
              overSample=bool(), os=bool(), samplingRate=int(), sr=int(), startTime=float(), st=float(), tempDir=bool(),
              tmp=bool(), *args, **kwargs):
    pass


def displacementToPoly(findBboxOnly=bool(), fbb=bool(), *args, **kwargs):
    pass


def displayAffected(*args, **kwargs):
    pass


def displayColor(active=bool(), a=bool(), create=bool(), c=bool(), dormant=bool(), d=bool(), list=bool(), l=bool(),
                 queryIndex=int(), qi=int(), resetToFactory=bool(), rf=bool(), resetToSaved=bool(), rs=bool(), *args,
                 **kwargs):
    pass


def displayCull(backFaceCulling=bool(), bfc=bool(), *args, **kwargs):
    pass


def displayLevelOfDetail(levelOfDetail=bool(), lod=bool(), *args, **kwargs):
    pass


def displayPref(activeObjectPivots=bool(), aop=bool(), displayAffected=bool(), da=bool(), displayGradient=bool(),
                dgr=bool(), ghostFrames=list, gf=list, materialLoadingMode=str(), mld=str(),
                maxHardwareTextureResolution=bool(), mhr=bool(), maxTextureResolution=int(), mtr=int(),
                purgeExistingTextures=bool(), pet=bool(), regionOfEffect=bool(), roe=bool(), shadeTemplates=bool(),
                st=bool(), textureDrawPixel=bool(), tdp=bool(), wireframeOnShadedActive=str(), wsa=str(), *args,
                **kwargs):
    pass


def displayRGBColor(create=bool(), c=bool(), hueSaturationValue=bool(), hsv=bool(), list=bool(), l=bool(),
                    resetToFactory=bool(), rf=bool(), resetToSaved=bool(), rs=bool(), *args, **kwargs):
    pass


def displaySmoothness(all=bool(), boundary=bool(), bn=bool(), defaultCreation=bool(), dc=bool(), divisionsU=int(),
                      du=int(), divisionsV=int(), dv=int(), full=bool(), f=bool(), hull=bool(), hl=bool(),
                      pointsShaded=int(), ps=int(), pointsWire=int(), pw=int(), polygonObject=int(), po=int(),
                      renderTessellation=bool(), rt=bool(), simplifyU=int(), su=int(), simplifyV=int(), sv=int(), *args,
                      **kwargs):
    pass


def displayString(delete=bool(), d=bool(), exists=bool(), ex=bool(), keys=bool(), k=bool(), replace=bool(), r=bool(),
                  value=str(), v=str(), *args, **kwargs):
    pass


def displaySurface(flipNormals=bool(), flp=bool(), twoSidedLighting=bool(), two=bool(), xRay=bool(), x=bool(), *args,
                   **kwargs):
    pass


def distanceDimContext(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                       i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def distanceDimension(endPoint=list, ep=list, startPoint=list, sp=list, *args, **kwargs):
    pass


def doBlur(colorFile=str(), c=str(), length=float(), l=float(), memCapSize=float(), o=float(), sharpness=float(),
           s=float(), smooth=float(), m=float(), smoothColor=bool(), r=bool(), vectorFile=str(), v=str(), *args,
           **kwargs):
    pass


def dockControl(allowedArea=str(), aa=str(), annotation=str(), ann=str(), area=str(), a=str(), backgroundColor=list,
                bgc=list, closeCommand=str(), cc=str(), content=str(), con=str(), defineTemplate=str(), dt=str(),
                docTag=str(), dtg=str(), dockStation=str(), ds=str(), dragCallback=str(), dgc=str(), dropCallback=str(),
                dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                ekf=bool(), enablePopupOption=bool(), epo=bool(), exists=bool(), ex=bool(), fixedHeight=bool(),
                fh=bool(), fixedWidth=bool(), fw=bool(), floatChangeCommand=str(), fcc=str(), floating=bool(),
                fl=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(), m=bool(), moveable=bool(),
                mov=bool(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(),
                p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), r=bool(), retain=bool(),
                ret=bool(), sizeable=bool(), s=bool(), splitLayout=str(), sl=str(), state=str(), st=str(),
                statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def dolly(absolute=bool(), abs=bool(), distance=float(), d=float(), dollyTowardsCenter=bool(), dtc=bool(),
          orthoScale=float(), os=float(), relative=bool(), rel=bool(), *args, **kwargs):
    pass


def dollyCtx(alternateContext=bool(), ac=bool(), boxDollyType=str(), bdt=str(), centerOfInterestDolly=bool(), cd=bool(),
             dollyTowardsCenter=bool(), dtc=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
             i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), localDolly=bool(), ld=bool(), name=str(),
             n=str(), orthoZoom=bool(), oz=bool(), scale=float(), s=float(), toolName=str(), tn=str(), *args, **kwargs):
    pass


def dopeSheetEditor(autoFit=str(), af=str(), autoFitTime=str(), aft=str(), control=bool(), ctl=bool(),
                    defineTemplate=str(), dt=str(), displayActiveKeyTangents=str(), dat=str(), displayActiveKeys=str(),
                    dak=str(), displayInfinities=str(), di=str(), displayKeys=str(), dk=str(), displayTangents=str(),
                    dtn=str(), displayValues=str(), dv=str(), docTag=str(), dtg=str(), exists=bool(), ex=bool(),
                    filter=str(), f=str(), forceMainConnection=str(), fmc=str(), hierarchyBelow=bool(), hb=bool(),
                    highlightConnection=str(), hlc=str(), lockMainConnection=bool(), lck=bool(), lookAt=str(), la=str(),
                    mainListConnection=str(), mlc=str(), outliner=str(), o=str(), panel=str(), pnl=str(), parent=str(),
                    p=str(), selectionConnection=str(), slc=str(), selectionWindow=list, sel=list, showScene=bool(),
                    sc=bool(), showSummary=bool(), ss=bool(), showTicks=bool(), stk=bool(), snapTime=str(), st=str(),
                    snapValue=str(), sv=str(), stateString=bool(), sts=bool(), unParent=bool(), up=bool(),
                    unlockMainConnection=bool(), ulk=bool(), updateMainConnection=bool(), upd=bool(), useTemplate=str(),
                    ut=str(), *args, **kwargs):
    pass


def doubleProfileBirailSurface(blendFactor=float(), bl=float(), caching=bool(), cch=bool(), constructionHistory=bool(),
                               ch=bool(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(),
                               polygon=int(), po=int(), tangentContinuityProfile1=bool(), tp1=bool(),
                               tangentContinuityProfile2=bool(), tp2=bool(), transformMode=int(), tm=int(), *args,
                               **kwargs):
    pass


def drag(attenuation=float(), att=float(), directionX=float(), dx=float(), directionY=float(), dy=float(),
         directionZ=float(), dz=float(), magnitude=float(), m=float(), maxDistance=float(), mxd=float(), name=str(),
         n=str(), perVertex=bool(), pv=bool(), position=list, pos=list, torusSectionRadius=float(), tsr=float(),
         useDirection=bool(), ud=bool(), volumeExclusion=bool(), vex=bool(), volumeOffset=list, vof=list,
         volumeShape=str(), vsh=str(), volumeSweep=float(), vsw=float(), *args, **kwargs):
    pass


def dragAttrContext(connectTo=str(), ct=str(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
                    i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), reset=bool(),
                    r=bool(), *args, **kwargs):
    pass


def draggerContext(anchorPoint=list, ap=list, button=int(), bu=int(), currentStep=int(), cs=int(), cursor=str(),
                   cur=str(), dragCommand=str(), dc=str(), dragPoint=list, dp=list, drawString=str(), ds=str(),
                   exists=bool(), ex=bool(), finalize=str(), fnz=str(), helpString=str(), hs=str(), history=bool(),
                   ch=bool(), holdCommand=str(), hc=str(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(),
                   i3=str(), initialize=str(), inz=str(), modifier=str(), mo=str(), name=str(), n=str(), plane=list,
                   pl=list, prePressCommand=str(), ppc=str(), pressCommand=str(), pc=str(), projection=str(), pr=str(),
                   releaseCommand=str(), rc=str(), snapping=bool(), snp=bool(), space=str(), sp=str(), stepsCount=int(),
                   sc=int(), undoMode=str(), um=str(), *args, **kwargs):
    pass


def dropoffLocator(*args, **kwargs):
    pass


def duplicate(fullPath=bool(), f=bool(), inputConnections=bool(), ic=bool(), instanceLeaf=bool(), ilf=bool(),
              name=str(), n=str(), parentOnly=bool(), po=bool(), renameChildren=bool(), rc=bool(),
              returnRootsOnly=bool(), rr=bool(), smartTransform=bool(), st=bool(), transformsOnly=bool(), to=bool(),
              upstreamNodes=bool(), un=bool(), *args, **kwargs):
    pass


def duplicateCurve(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), local=bool(), l=bool(),
                   maxValue=float(), max=float(), mergeItems=bool(), mi=bool(), minValue=float(), min=float(),
                   name=str(), n=str(), nodeState=int(), nds=int(), range=bool(), rn=bool(), relative=bool(), r=bool(),
                   *args, **kwargs):
    pass


def duplicateSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), faceCountU=int(), fcu=int(),
                     faceCountV=int(), fcv=int(), firstFaceU=int(), ffu=int(), firstFaceV=int(), ffv=int(),
                     local=bool(), l=bool(), mergeItems=bool(), mi=bool(), name=str(), n=str(), nodeState=int(),
                     nds=int(), *args, **kwargs):
    pass


def dynamicLoad(*args, **kwargs):
    pass


def dynCache(*args, **kwargs):
    pass


def dynExport(allObjects=bool(), all=bool(), attribute=str(), atr=str(), format=str(), f=str(), maxFrame=float(),
              mxf=float(), minFrame=float(), mnf=float(), onlyUpdateParticles=bool(), oup=bool(), overSampling=int(),
              os=int(), path=str(), p=str(), *args, **kwargs):
    pass


def dynExpression(creation=bool(), c=bool(), runtime=bool(), r=bool(), runtimeAfterDynamics=bool(), rad=bool(),
                  runtimeBeforeDynamics=bool(), rbd=bool(), string=str(), s=str(), *args, **kwargs):
    pass


def dynGlobals(active=bool(), a=bool(), listAll=bool(), la=bool(), overSampling=int(), os=int(), *args, **kwargs):
    pass


def dynPaintEditor(activeOnly=bool(), ao=bool(), autoSave=bool(), camera=str(), cam=str(), canvasMode=bool(), cm=bool(),
                   canvasUndo=bool(), cu=bool(), changeCommand=list, cc=list, clear=list, cl=list, control=bool(),
                   ctl=bool(), currentCanvasSize=bool(), ccs=bool(), defineTemplate=str(), dt=str(),
                   displayAppearance=str(), dsa=str(), displayFog=bool(), dfg=bool(), displayImage=int(), di=int(),
                   displayLights=str(), dsl=str(), displayStyle=str(), dst=str(), displayTextures=bool(), dtx=bool(),
                   docTag=str(), dtg=str(), doubleBuffer=bool(), dbf=bool(), drawAxis=bool(), da=bool(),
                   drawContext=bool(), drc=bool(), exists=bool(), ex=bool(), fastUpdate=int(), fu=int(), fileName=str(),
                   fil=str(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(), highlightConnection=str(),
                   hlc=str(), iconGrab=bool(), ig=bool(), loadImage=str(), li=str(), lockMainConnection=bool(),
                   lck=bool(), mainListConnection=str(), mlc=str(), menu=str(), mn=str(), nbImages=bool(), nim=bool(),
                   newImage=list, ni=list, paintAll=float(), pa=float(), panel=str(), pnl=str(), parent=str(), p=str(),
                   redrawLast=bool(), rl=bool(), refresh=bool(), ref=bool(), refreshMode=int(), rmd=int(),
                   removeAllImages=bool(), ra=bool(), removeImage=bool(), ri=bool(), rollImage=list, rig=list,
                   saveAlpha=bool(), sa=bool(), saveBumpmap=str(), sbm=str(), saveImage=bool(), si=bool(),
                   scaleBlue=float(), sb=float(), scaleGreen=float(), sg=float(), scaleRed=float(), sr=float(),
                   selectionConnection=str(), slc=str(), singleBuffer=bool(), sbf=bool(), snapShot=bool(), snp=bool(),
                   stateString=bool(), sts=bool(), swap=int(), swp=int(), tileSize=int(), ts=int(), unParent=bool(),
                   up=bool(), undoCache=bool(), uc=bool(), unlockMainConnection=bool(), ulk=bool(),
                   updateMainConnection=bool(), upd=bool(), useTemplate=str(), ut=str(), wrap=list, wr=list,
                   writeImage=str(), wi=str(), zoom=float(), zm=float(), *args, **kwargs):
    pass


def dynParticleCtx(conserve=float(), c=float(), cursorPlacement=bool(), cp=bool(), exists=bool(), ex=bool(),
                   grid=bool(), gr=bool(), gridSpacing=float(), grs=float(), history=bool(), ch=bool(), image1=str(),
                   i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), jitterRadius=float(), jr=float(),
                   lowerLeftX=float(), llx=float(), lowerLeftY=float(), lly=float(), lowerLeftZ=float(), llz=float(),
                   name=str(), n=str(), nucleus=bool(), nc=bool(), numJitters=int(), nj=int(), particleName=str(),
                   pn=str(), sketch=bool(), sk=bool(), sketchInterval=int(), ski=int(), textPlacement=bool(), tp=bool(),
                   upperRightX=float(), urx=float(), upperRightY=float(), ury=float(), upperZ=float(), urz=float(),
                   *args, **kwargs):
    pass


def dynPref(autoCreate=bool(), ac=bool(), echoCollision=bool(), ec=bool(), runupFrom=int(), rf=int(),
            runupToCurrentTime=bool(), rt=bool(), saveOnQuit=bool(), sq=bool(), saveRuntimeState=bool(), sr=bool(),
            *args, **kwargs):
    pass


def editDisplayLayerGlobals(baseId=int(), bi=int(), currentDisplayLayer=str(), cdl=str(), mergeType=int(), mt=int(),
                            useCurrent=bool(), uc=bool(), *args, **kwargs):
    pass


def editDisplayLayerMembers(fullNames=bool(), fn=bool(), noRecurse=bool(), nr=bool(), *args, **kwargs):
    pass


def editMetadata(channelName=str(), cn=str(), channelType=str(), cht=str(), endIndex=str(), eix=str(), index=str(),
                 idx=str(), indexType=str(), idt=str(), memberName=str(), mn=str(), remove=bool(), rem=bool(),
                 scene=bool(), scn=bool(), startIndex=str(), six=str(), streamName=str(), stn=str(), stringValue=str(),
                 sv=str(), value=float(), v=float(), *args, **kwargs):
    pass


def editor(control=bool(), ctl=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), exists=bool(),
           ex=bool(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(), highlightConnection=str(), hlc=str(),
           lockMainConnection=bool(), lck=bool(), mainListConnection=str(), mlc=str(), panel=str(), pnl=str(),
           parent=str(), p=str(), selectionConnection=str(), slc=str(), stateString=bool(), sts=bool(), unParent=bool(),
           up=bool(), unlockMainConnection=bool(), ulk=bool(), updateMainConnection=bool(), upd=bool(),
           useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def editorTemplate(addAdskAssetControls=bool(), aac=bool(), addComponents=bool(), acp=bool(), addControl=list, ac=list,
                   addDynamicControl=list, adc=list, addExtraControls=bool(), aec=bool(), addSeparator=bool(),
                   annotateFieldOnly=bool(), afo=bool(), annotation=str(), ann=str(), beginLayout=str(), bl=str(),
                   beginNoOptimize=bool(), bn=bool(), beginScrollLayout=bool(), bsl=bool(), callCustom=list, ccu=list,
                   collapse=bool(), cl=bool(), debugMode=bool(), dbm=bool(), dimControl=list, dc=list, endLayout=bool(),
                   el=bool(), endNoOptimize=bool(), en=bool(), endScrollLayout=bool(), esl=bool(),
                   extraControlsLabel=str(), ecl=str(), forceRebuild=bool(), fr=bool(), interruptOptimize=bool(),
                   io=bool(), label=str(), l=str(), listExtraAttributes=str(), lea=str(), preventOverride=bool(),
                   po=bool(), queryControl=list, qc=list, queryLabel=list, ql=list, queryName=list, qn=list,
                   removeControl=list, rc=list, suppress=str(), s=str(), *args, **kwargs):
    pass


def editRenderLayerAdjustment(attributeLog=bool(), alg=bool(), layer=str(), lyr=str(), nodeLog=bool(), nlg=bool(),
                              remove=bool(), r=bool(), *args, **kwargs):
    pass


def editRenderLayerGlobals(baseId=int(), bi=int(), currentRenderLayer=str(), crl=str(), enableAutoAdjustments=bool(),
                           eaa=bool(), mergeType=int(), mt=int(), useCurrent=bool(), uc=bool(), *args, **kwargs):
    pass


def editRenderLayerMembers(fullNames=bool(), fn=bool(), noRecurse=bool(), nr=bool(), remove=bool(), r=bool(), *args,
                           **kwargs):
    pass


def effector(hide=bool(), hi=bool(), name=str(), n=str(), *args, **kwargs):
    pass


def emit(attribute=str(), at=str(), floatValue=float(), fv=float(), object=str(), o=str(), position=list, pos=list,
         vectorValue=list, vv=list, *args, **kwargs):
    pass


def emitter(alongAxis=float(), alx=float(), aroundAxis=float(), arx=float(), awayFromAxis=float(), afx=float(),
            awayFromCenter=float(), afc=float(), cycleEmission=str(), cye=str(), cycleInterval=int(), cyi=int(),
            directionX=float(), dx=float(), directionY=float(), dy=float(), directionZ=float(), dz=float(),
            directionalSpeed=float(), drs=float(), maxDistance=float(), mxd=float(), minDistance=float(), mnd=float(),
            name=str(), n=str(), needParentUV=bool(), nuv=bool(), normalSpeed=float(), nsp=float(), position=list,
            pos=list, randomDirection=float(), rnd=float(), rate=float(), r=float(), scaleRateByObjectSize=bool(),
            sro=bool(), scaleSpeedBySize=bool(), ssz=bool(), speed=float(), spd=float(), speedRandom=float(),
            srn=float(), spread=float(), sp=float(), tangentSpeed=float(), tsp=float(), torusSectionRadius=float(),
            tsr=float(), type=str(), typ=str(), volumeOffset=list, vof=list, volumeShape=str(), vsh=str(),
            volumeSweep=float(), vsw=float(), *args, **kwargs):
    pass


def enableDevice(apply=bool(), a=bool(), device=str(), d=str(), enable=bool(), en=bool(), monitor=bool(), m=bool(),
                 record=bool(), rec=bool(), *args, **kwargs):
    pass


def encodeString(*args, **kwargs):
    pass


def error(noContext=bool(), n=bool(), showLineNumber=bool(), sl=bool(), *args, **kwargs):
    pass


def eval(*args, **kwargs):
    pass


def evalDeferred(*args, evaluateNext=bool(), en=bool(), list=bool(), ls=bool(), lowPriority=bool(), low=bool(),
                 lowestPriority=bool(), lp=bool(), **kwargs):
    if callable(args[0]):
        # If the first argument is a callable, we assume it's a function to be evaluated
        func = args[0]
        args = args[1:]  # Remove the function from the args list
        kwargs = kwargs or {}
        if args:
            # If there are additional arguments, we call the function with them
            func(*args, **kwargs)
        else:
            func()
    elif isinstance(args[0], str):
        # If the first argument is a string, we assume it's a command to be evaluated
        command = args[0]
        # exec(command)


def evaluationManager(cycleCluster=str(), ccl=str(), disableInfo=str(), di=str(), downstreamFrom=str(), dst=str(),
                      empty=bool(), mt=bool(), enabled=bool(), e=bool(), fallbackTriggered=bool(), ft=bool(),
                      idleAction=int(), ia=int(), idleBuild=bool(), ib=bool(), invalidate=bool(), inv=bool(),
                      manipulation=bool(), man=bool(), manipulationPrevalidation=bool(), mp=bool(),
                      manipulationReady=bool(), mr=bool(), mode=str(), m=str(), nodeTypeGloballySerialize=bool(),
                      ntg=bool(), nodeTypeParallel=bool(), ntp=bool(), nodeTypeSerialize=bool(), nts=bool(),
                      nodeTypeUntrusted=bool(), ntu=bool(), reduceGraphRebuild=bool(), rgr=bool(), safeMode=bool(),
                      sfm=bool(), upstreamFrom=str(), ust=str(), *args, **kwargs):
    pass


def evaluator(clusters=bool(), cl=bool(), configuration=str(), c=str(), enable=bool(), en=bool(), info=bool(), i=bool(),
              name=str(), n=str(), nodeType=str(), nt=str(), nodeTypeChildren=bool(), ntc=bool(), priority=int(),
              p=int(), valueName=str(), vn=str(), *args, **kwargs):
    pass


def event(count=int(), ct=int(), delete=bool(), d=bool(), dieAtCollision=bool(), die=bool(), emit=int(), em=int(),
          list=bool(), ls=bool(), name=str(), n=str(), proc=str(), pr=str(), random=bool(), r=bool(), rename=str(),
          re=str(), select=bool(), s=bool(), split=int(), spl=int(), spread=float(), sp=float(), target=str(), t=str(),
          *args, **kwargs):
    pass


def exactWorldBoundingBox(calculateExactly=bool(), ce=bool(), ignoreInvisible=bool(), ii=bool(), *args, **kwargs):
    pass


def exclusiveLightCheckBox(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(),
                           docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
                           enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                           ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                           highlightColor=list, hlc=list, isObscured=bool(), io=bool(), label=str(), l=str(),
                           light=str(), lt=str(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                           numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(),
                           pma=bool(), preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(),
                           useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(),
                           vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def expandedSelection(depth=int(), d=int(), expansionType=str(), et=str(), *args, **kwargs):
    pass


def exportEdits(editCommand=str(), ec=str(), excludeHierarchy=bool(), ehr=bool(), excludeNode=str(), en=str(),
                exportSelected=bool(), exs=bool(), force=bool(), f=bool(), includeAnimation=bool(), ian=bool(),
                includeConstraints=bool(), ic=bool(), includeDeformers=bool(), idf=bool(), includeNetwork=bool(),
                inw=bool(), includeNode=str(), includeSetAttrs=bool(), isa=bool(), includeSetDrivenKeys=bool(),
                sdk=bool(), includeShaders=bool(), ish=bool(), onReferenceNode=str(), orn=str(), selected=bool(),
                sel=bool(), type=str(), typ=str(), *args, **kwargs):
    pass


def expression(alwaysEvaluate=int(), ae=int(), animated=int(), an=int(), attribute=str(), a=str(), name=str(), n=str(),
               object=str(), o=str(), safe=bool(), sf=bool(), shortNames=bool(), sn=bool(), string=str(), s=str(),
               timeDependent=bool(), td=bool(), unitConversion=str(), uc=str(), *args, **kwargs):
    pass


def expressionEditorListen(listenFile=str(), lf=str(), listenForAttr=str(), la=str(), listenForExpression=str(),
                           le=str(), listenForName=str(), ln=str(), stopListenForAttr=str(), sla=str(),
                           stopListenForExpression=str(), sle=str(), stopListenForName=str(), sln=str(), *args,
                           **kwargs):
    pass


def extendCurve(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), curveOnSurface=bool(), cos=bool(),
                distance=float(), d=float(), extendMethod=int(), em=int(), extensionType=int(), et=int(),
                inputPoint=list, ip=list, join=bool(), jn=bool(), name=str(), n=str(), noChanges=bool(), nc=bool(),
                nodeState=int(), nds=int(), object=bool(), o=bool(), pointX=float(), px=float(), pointY=float(),
                py=float(), pointZ=float(), pz=float(), range=bool(), rn=bool(), removeMultipleKnots=bool(), rmk=bool(),
                replaceOriginal=bool(), rpo=bool(), start=int(), s=int(), *args, **kwargs):
    pass


def extendSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), distance=float(), d=float(),
                  extendDirection=int(), ed=int(), extendMethod=int(), em=int(), extendSide=int(), es=int(),
                  extensionType=int(), et=int(), join=bool(), jn=bool(), name=str(), n=str(), nodeState=int(),
                  nds=int(), object=bool(), o=bool(), replaceOriginal=bool(), rpo=bool(), *args, **kwargs):
    pass


def extrude(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), degreeAlongLength=int(), dl=int(),
            direction=list, d=list, directionX=float(), dx=float(), directionY=float(), dy=float(), directionZ=float(),
            dz=float(), extrudeType=int(), et=int(), fixedPath=bool(), fpt=bool(), length=float(), l=float(),
            mergeItems=bool(), mi=bool(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(),
            pivot=list, p=list, polygon=int(), po=int(), range=bool(), rn=bool(), rebuild=bool(), rb=bool(),
            reverseSurfaceIfPathReversed=bool(), rsp=bool(), rotation=float(), ro=float(), scale=float(), sc=float(),
            subCurveSubSurface=bool(), scs=bool(), useComponentPivot=int(), ucp=int(), useProfileNormal=bool(),
            upn=bool(), *args, **kwargs):
    pass


def falloffCurve(addControlVertex=str(), acv=str(), annotation=str(), ann=str(), asString=str(), backgroundColor=list,
                 bgc=list, changeCommand=str(), cc=str(), currentKey=int(), ck=int(), currentKeyValue=list, ckv=list,
                 customCurveWidget=bool(), ccw=bool(), defineTemplate=str(), dt=str(), deleteControlVertex=int(),
                 dcv=int(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
                 enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(),
                 exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list,
                 hlc=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                 numberOfPopupMenus=bool(), npm=bool(), optionVar=str(), ov=str(), parent=str(), p=str(),
                 popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), readOnly=bool(), ro=bool(),
                 snapToGrid=bool(), stg=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
                 visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                 **kwargs):
    pass


def falloffCurveAttr(addControlVertex=str(), acv=str(), annotation=str(), ann=str(), asString=str(), attribute=str(),
                     at=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(), currentKey=int(),
                     ck=int(), currentKeyValue=list, ckv=list, customCurveWidget=int(), ccw=int(), defineTemplate=str(),
                     dt=str(), deleteControlVertex=int(), dcv=int(), docTag=str(), dtg=str(), dragCallback=str(),
                     dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(),
                     ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(),
                     fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(),
                     manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(),
                     parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
                     readOnly=int(), ro=int(), selectedPositionControl=str(), spc=str(), selectedValueControl=str(),
                     svc=str(), snapToGrid=int(), stg=int(), statusBarMessage=str(), sbm=str(), useTemplate=str(),
                     ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
                     *args, **kwargs):
    pass


def fcheck(*args, **kwargs):
    pass


def file(absoluteName=bool(), an=bool(), activate=bool(), a=bool(), activeProxy=bool(), ap=bool(), add=bool(),
         anyModified=bool(), amf=bool(), applyTo=str(), at=str(), buildLoadSettings=bool(), bls=bool(), channels=bool(),
         chn=bool(), cleanReference=str(), cr=str(), command=list, c=list, compress=bool(), cmp=bool(),
         constraints=bool(), con=bool(), constructionHistory=bool(), ch=bool(), copyNumberList=bool(), cnl=bool(),
         defaultExtensions=bool(), de=bool(), defaultNamespace=bool(), dns=bool(), deferReference=bool(), dr=bool(),
         editCommand=str(), ec=str(), errorStatus=bool(), err=bool(), executeScriptNodes=bool(), esn=bool(),
         exists=bool(), ex=bool(), expandName=bool(), exn=bool(), exportAll=bool(), ea=bool(), exportAnim=bool(),
         ean=bool(), exportAnimFromReference=bool(), ear=bool(), exportAsReference=bool(), er=bool(),
         exportAsSegment=bool(), exs=bool(), exportSelected=bool(), es=bool(), exportSelectedAnim=bool(), eas=bool(),
         exportSelectedAnimFromReference=bool(), esa=bool(), exportSelectedNoReference=bool(), esr=bool(),
         exportSelectedStrict=bool(), ess=bool(), exportSnapshotCallback=list, esc=list,
         exportUnloadedReferences=bool(), eur=bool(), expressions=bool(), exp=bool(), fileMetaData=bool(), fmd=bool(),
         flushReference=str(), fr=str(), force=bool(), f=bool(), groupLocator=bool(), gl=bool(), groupName=str(),
         gn=str(), groupReference=bool(), gr=bool(), i=bool(), ignoreVersion=bool(), iv=bool(), importFrameRate=bool(),
         ifr=bool(), importReference=bool(), ir=bool(), importTimeRange=str(), itr=str(), lastFileOption=bool(),
         lfo=bool(), lastTempFile=bool(), ltf=bool(), list=bool(), l=bool(), loadAllDeferred=bool(), lad=bool(),
         loadAllReferences=bool(), lar=bool(), loadNoReferences=bool(), lnr=bool(), loadReference=str(), lr=str(),
         loadReferenceDepth=str(), lrd=str(), loadReferencePreview=str(), lrp=str(), loadSettings=str(), ls=str(),
         location=bool(), loc=bool(), lockContainerUnpublished=bool(), lcu=bool(), lockFile=bool(), lf=bool(),
         lockReference=bool(), lck=bool(), mapPlaceHolderNamespace=list, mns=list, mergeBaseAnimLayer=bool(),
         mbl=bool(), mergeNamespaceWithParent=bool(), mnp=bool(), mergeNamespaceWithRoot=bool(), mnr=bool(),
         mergeNamespacesOnClash=bool(), mnc=bool(), modified=bool(), mf=bool(), moveSelected=bool(), ms=bool(),
         namespace=str(), ns=str(), newFile=bool(), new=bool(), open=bool(), o=bool(), options=str(), op=str(),
         parentNamespace=bool(), pns=bool(), postSaveScript=str(), pos=str(), preSaveScript=str(), prs=str(),
         preserveName=bool(), pn=bool(), preserveReferences=bool(), pr=bool(), preview=bool(), pv=bool(), prompt=bool(),
         pmt=bool(), proxyManager=str(), pm=str(), proxyTag=str(), pt=str(), reference=bool(), r=bool(),
         referenceDepthInfo=int(), rdi=int(), referenceNode=str(), rfn=str(), relativeNamespace=str(), rns=str(),
         removeDuplicateNetworks=bool(), rdn=bool(), removeReference=bool(), rr=bool(), rename=str(), rn=str(),
         renameAll=bool(), ra=bool(), renameToSave=bool(), rts=bool(), renamingPrefix=str(), rpr=str(),
         renamingPrefixList=bool(), rpl=bool(), replaceName=list, rep=list, reserveNamespaces=bool(), rvn=bool(),
         resetError=bool(), rer=bool(), returnNewNodes=bool(), rnn=bool(), save=bool(), s=bool(), saveDiskCache=str(),
         sdc=str(), saveReference=bool(), sr=bool(), saveReferencesUnloaded=bool(), sru=bool(), saveTextures=str(),
         stx=str(), sceneName=bool(), sn=bool(), segment=str(), seg=str(), selectAll=bool(), sa=bool(), shader=bool(),
         sh=bool(), sharedNodes=str(), shd=str(), sharedReferenceFile=bool(), srf=bool(), shortName=bool(), shn=bool(),
         strict=bool(), str=bool(), swapNamespace=list, sns=list, type=str(), typ=str(), uiConfiguration=bool(),
         uc=bool(), uiLoadConfiguration=bool(), ulc=bool(), unloadReference=str(), ur=str(), unresolvedName=bool(),
         un=bool(), usingNamespaces=bool(), uns=bool(), withoutCopyNumber=bool(), wcn=bool(), writable=bool(), w=bool(),
         *args, **kwargs):
    
    if new or newFile and force or f:
        om._NEW_SCENE_SIGNAL.send()


def fileBrowserDialog(actionName=str(), an=str(), dialogStyle=int(), ds=int(), fileCommand=str(), fc=str(),
                      fileType=str(), ft=str(), filterList=str(), fl=str(), includeName=str(), mode=int(), m=int(),
                      operationMode=str(), om=str(), tipMessage=str(), tm=str(), windowTitle=str(), wt=str(), *args,
                      **kwargs):
    pass


def fileDialog(application=bool(), app=bool(), defaultFileName=str(), dfn=str(), directoryMask=str(), dm=str(),
               mode=int(), m=int(), title=str(), t=str(), *args, **kwargs):
    pass


def fileDialog2(buttonBoxOrientation=int(), bbo=int(), cancelCaption=str(), cc=str(), caption=str(), cap=str(),
                dialogStyle=int(), ds=int(), fileFilter=str(), ff=str(), fileMode=int(), fm=int(),
                fileTypeChanged=str(), ftc=str(), hideNameEdit=bool(), hne=bool(), okCaption=str(), okc=str(),
                optionsUICancel=str(), oca=str(), optionsUICommit=str(), ocm=str(), optionsUICommit2=str(), oc2=str(),
                optionsUICreate=str(), ocr=str(), optionsUIInit=str(), oin=str(), optionsUITitle=str(), oti=str(),
                returnFilter=bool(), rf=bool(), selectFileFilter=str(), sff=str(), selectionChanged=str(), sc=str(),
                setProjectBtnEnabled=bool(), spe=bool(), startingDirectory=str(), dir=str(), *args, **kwargs):
    pass


def fileInfo(referenceNode=str(), rfn=str(), remove=str(), rm=str(), *args, **kwargs):
    pass


def filePathEditor(attributeOnly=bool(), ao=bool(), attributeType=str(), at=str(), byType=str(), bt=str(),
                   copyAndRepath=list, cr=list, deregisterType=str(), dt=str(), force=bool(), f=bool(),
                   listDirectories=str(), ld=str(), listFiles=str(), lf=str(), listRegisteredTypes=bool(), lrt=bool(),
                   preview=bool(), p=bool(), recursive=bool(), rc=bool(), refresh=bool(), rf=bool(), registerType=str(),
                   rt=str(), relativeNames=bool(), rel=bool(), repath=str(), r=str(), replaceAll=bool(), ra=bool(),
                   replaceField=str(), rfd=str(), replaceString=list, rs=list, status=bool(), s=bool(),
                   temporary=bool(), tmp=bool(), typeLabel=str(), tl=str(), unresolved=bool(), u=bool(),
                   withAttribute=bool(), wa=bool(), *args, **kwargs):
    pass


def filletCurve(bias=float(), b=float(), blendControl=bool(), bc=bool(), caching=bool(), cch=bool(), circular=bool(),
                cir=bool(), constructionHistory=bool(), ch=bool(), curveParameter1=float(), cp1=float(),
                curveParameter2=float(), cp2=float(), depth=float(), d=float(), freeformBlend=bool(), fb=bool(),
                join=bool(), jn=bool(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(),
                radius=float(), r=float(), replaceOriginal=bool(), rpo=bool(), trim=bool(), t=bool(), *args, **kwargs):
    pass


def filter(name=str(), n=str(), type=str(), t=str(), *args, **kwargs):
    pass


def filterButterworthCtx(apply=bool(), a=bool(), cutoffFrequency=float(), cof=float(), endTime=float(), e=float(),
                         exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                         i2=str(), image3=str(), i3=str(), keepKeysOnFrame=bool(), kof=bool(), name=str(), n=str(),
                         samplingRate=float(), sr=float(), selectedKeys=bool(), sk=bool(), startTime=float(), s=float(),
                         *args, **kwargs):
    pass


def filterCurve(cutoffFrequency=float(), cof=float(), endTime=float(), e=float(), filter=str(), f=str(),
                keepKeysOnFrame=bool(), kof=bool(), kernel=str(), ker=str(), keySync=bool(), ks=bool(),
                maxTimeStep=float(), mxs=float(), minTimeStep=float(), mns=float(), period=float(), per=float(),
                precision=float(), pre=float(), precisionMode=int(), pm=int(), preserveKeyTangent=str(), pkt=str(),
                sampleCount=int(), sc=int(), samplingRate=float(), sr=float(), selectedKeys=bool(), sk=bool(),
                startTime=float(), s=float(), timeTolerance=float(), tto=float(), tolerance=float(), tol=float(),
                useQuaternion=bool(), uq=bool(), width=float(), w=float(), *args, **kwargs):
    pass


def filterExpand(expand=bool(), ex=bool(), fullPath=bool(), fp=bool(), selectionMask=int(), sm=int(), symActive=bool(),
                 sma=bool(), symNegative=bool(), smn=bool(), symPositive=bool(), smp=bool(), symSeam=bool(), sms=bool(),
                 *args, **kwargs):
    pass


def filterGaussianCtx(apply=bool(), a=bool(), endTime=float(), e=float(), exists=bool(), ex=bool(), history=bool(),
                      ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(),
                      n=str(), sampleCount=int(), sc=int(), selectedKeys=bool(), sk=bool(), startTime=float(),
                      s=float(), useQuaternion=bool(), uq=bool(), width=float(), w=float(), *args, **kwargs):
    pass


def filterInstances(shapes=bool(), s=bool(), *args, **kwargs):
    pass


def filterKeyReducerCtx(apply=bool(), a=bool(), endTime=float(), e=float(), exists=bool(), ex=bool(), history=bool(),
                        ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                        keySync=bool(), ks=bool(), name=str(), n=str(), precision=float(), pre=float(),
                        precisionMode=int(), pm=int(), preserveKeyTangent=str(), pkt=str(), selectedKeys=bool(),
                        sk=bool(), startTime=float(), s=float(), *args, **kwargs):
    pass


def filterStudioImport(convertShellToPoly=bool(), sp=bool(), includeCameras=bool(), ic=bool(), includeLights=bool(),
                       il=bool(), transferDirectoryName=str(), td=str(), *args, **kwargs):
    pass


def findDeformers(*args, **kwargs):
    pass


def findKeyframe(animation=str(), an=str(), attribute=str(), at=str(), controlPoints=bool(), cp=bool(), curve=bool(),
                 c=bool(), float=tuple(), f=tuple(), hierarchy=str(), hi=str(), includeUpperBound=bool(), iub=bool(),
                 index=int(), shape=bool(), s=bool(), time=tuple(), t=tuple(), timeSlider=bool(), ts=bool(),
                 which=str(), w=str(), *args, **kwargs):
    pass


def findType(deep=bool(), d=bool(), exact=bool(), e=bool(), forward=bool(), f=bool(), type=str(), t=str(), *args,
             **kwargs):
    pass


def fitBspline(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(), nodeState=int(),
               nds=int(), object=bool(), o=bool(), tolerance=float(), tol=float(), *args, **kwargs):
    pass


def flexor(atBones=bool(), ab=bool(), atJoints=bool(), aj=bool(), deformerCommand=str(), dc=str(), list=bool(),
           l=bool(), name=str(), n=str(), noScale=bool(), ns=bool(), toSkeleton=bool(), ts=bool(), type=str(),
           typ=str(), *args, **kwargs):
    pass


def floatField(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(),
               defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
               dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(), editable=bool(), ed=bool(), enable=bool(),
               en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(),
               enterCommand=str(), ec=str(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(),
               h=int(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(),
               maxValue=float(), max=float(), minValue=float(), min=float(), noBackground=bool(), nbg=bool(),
               numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
               precision=int(), pre=int(), preventOverride=bool(), po=bool(), receiveFocusCommand=str(), rfc=str(),
               showTrailingZeros=bool(), tze=bool(), statusBarMessage=str(), sbm=str(), step=float(), s=float(),
               useTemplate=str(), ut=str(), value=float(), v=float(), visible=bool(), vis=bool(),
               visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def floatFieldGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                  ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                  adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                  changeCommand=str(), cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list,
                  columnAlign3=list, cl3=list, columnAlign4=list, cl4=list, columnAlign5=list, cl5=list,
                  columnAlign6=list, cl6=list, columnAttach=list, cat=list, columnAttach2=list, ct2=list,
                  columnAttach3=list, ct3=list, columnAttach4=list, ct4=list, columnAttach5=list, ct5=list,
                  columnAttach6=list, ct6=list, columnOffset2=list, co2=list, columnOffset3=list, co3=list,
                  columnOffset4=list, co4=list, columnOffset5=list, co5=list, columnOffset6=list, co6=list,
                  columnWidth=list, cw=list, columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list,
                  columnWidth3=list, cw3=list, columnWidth4=list, cw4=list, columnWidth5=list, cw5=list,
                  columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                  dragCallback=str(), dgc=str(), dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(),
                  enable=bool(), en=bool(), enable1=bool(), en1=bool(), enable2=bool(), en2=bool(), enable3=bool(),
                  en3=bool(), enable4=bool(), en4=bool(), enableBackground=bool(), ebg=bool(),
                  enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), extraLabel=str(), el=str(),
                  fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                  isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(),
                  nbg=bool(), numberOfFields=int(), nf=int(), numberOfPopupMenus=bool(), npm=bool(), parent=str(),
                  p=str(), popupMenuArray=bool(), pma=bool(), precision=int(), pre=int(), preventOverride=bool(),
                  po=bool(), rowAttach=list, rat=list, showTrailingZeros=bool(), tze=bool(), statusBarMessage=str(),
                  sbm=str(), step=float(), s=float(), useTemplate=str(), ut=str(), value=list, v=list, value1=float(),
                  v1=float(), value2=float(), v2=float(), value3=float(), v3=float(), value4=float(), v4=float(),
                  visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                  **kwargs):
    pass


def floatScrollBar(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(),
                   defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                   dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                   enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                   ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                   horizontal=bool(), hr=bool(), isObscured=bool(), io=bool(), largeStep=float(), ls=float(),
                   manage=bool(), m=bool(), maxValue=float(), max=float(), minValue=float(), min=float(),
                   noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                   popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), statusBarMessage=str(),
                   sbm=str(), step=float(), s=float(), useTemplate=str(), ut=str(), value=float(), v=float(),
                   visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                   **kwargs):
    pass


def floatSlider(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(),
                defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
                fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                horizontal=bool(), hr=bool(), isObscured=bool(), io=bool(), manage=bool(), m=bool(), maxValue=float(),
                max=float(), minValue=float(), min=float(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(),
                npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
                statusBarMessage=str(), sbm=str(), step=float(), s=float(), useTemplate=str(), ut=str(), value=float(),
                v=float(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
                *args, **kwargs):
    pass


def floatSlider2(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand1=str(), cc1=str(),
                 changeCommand2=str(), cc2=str(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                 dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                 enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
                 fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                 isObscured=bool(), io=bool(), manage=bool(), m=bool(), maximum=float(), max=float(), minimum=float(),
                 min=float(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(),
                 p=str(), polarity=int(), pol=int(), popupMenuArray=bool(), pma=bool(), positionControl1=str(),
                 pc1=str(), positionControl2=str(), pc2=str(), preventOverride=bool(), po=bool(),
                 statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), value1=float(), v1=float(),
                 value2=float(), v2=float(), values=list, vs=list, visible=bool(), vis=bool(),
                 visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def floatSliderButtonGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                         ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                         adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list,
                         bgc=list, buttonCommand=str(), bc=str(), buttonLabel=str(), bl=str(), changeCommand=str(),
                         cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list, columnAlign3=list, cl3=list,
                         columnAlign4=list, cl4=list, columnAlign5=list, cl5=list, columnAlign6=list, cl6=list,
                         columnAttach=list, cat=list, columnAttach2=list, ct2=list, columnAttach3=list, ct3=list,
                         columnAttach4=list, ct4=list, columnAttach5=list, ct5=list, columnAttach6=list, ct6=list,
                         columnOffset2=list, co2=list, columnOffset3=list, co3=list, columnOffset4=list, co4=list,
                         columnOffset5=list, co5=list, columnOffset6=list, co6=list, columnWidth=list, cw=list,
                         columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list, columnWidth3=list, cw3=list,
                         columnWidth4=list, cw4=list, columnWidth5=list, cw5=list, columnWidth6=list, cw6=list,
                         defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                         dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                         enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                         ex=bool(), extraLabel=str(), el=str(), field=bool(), f=bool(), fieldMaxValue=float(),
                         fmx=float(), fieldMinValue=float(), fmn=float(), fieldStep=float(), fs=float(),
                         fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                         image=str(), i=str(), isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(),
                         m=bool(), maxValue=float(), max=float(), minValue=float(), min=float(), noBackground=bool(),
                         nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                         popupMenuArray=bool(), pma=bool(), precision=int(), pre=int(), preventOverride=bool(),
                         po=bool(), rowAttach=list, rat=list, sliderStep=float(), ss=float(), statusBarMessage=str(),
                         sbm=str(), step=float(), s=float(), symbolButtonCommand=str(), sbc=str(),
                         symbolButtonDisplay=bool(), sbd=bool(), useTemplate=str(), ut=str(), value=float(), v=float(),
                         visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                         **kwargs):
    pass


def floatSliderGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                   ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                   adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                   changeCommand=str(), cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list,
                   columnAlign3=list, cl3=list, columnAlign4=list, cl4=list, columnAlign5=list, cl5=list,
                   columnAlign6=list, cl6=list, columnAttach=list, cat=list, columnAttach2=list, ct2=list,
                   columnAttach3=list, ct3=list, columnAttach4=list, ct4=list, columnAttach5=list, ct5=list,
                   columnAttach6=list, ct6=list, columnOffset2=list, co2=list, columnOffset3=list, co3=list,
                   columnOffset4=list, co4=list, columnOffset5=list, co5=list, columnOffset6=list, co6=list,
                   columnWidth=list, cw=list, columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list,
                   columnWidth3=list, cw3=list, columnWidth4=list, cw4=list, columnWidth5=list, cw5=list,
                   columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                   dragCallback=str(), dgc=str(), dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(),
                   enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                   ekf=bool(), exists=bool(), ex=bool(), extraLabel=str(), el=str(), field=bool(), f=bool(),
                   fieldMaxValue=float(), fmx=float(), fieldMinValue=float(), fmn=float(), fieldStep=float(),
                   fs=float(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                   isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(), m=bool(), maxValue=float(),
                   max=float(), minValue=float(), min=float(), noBackground=bool(), nbg=bool(),
                   numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                   precision=int(), pre=int(), preventOverride=bool(), po=bool(), rowAttach=list, rat=list,
                   sliderStep=float(), ss=float(), statusBarMessage=str(), sbm=str(), step=float(), s=float(),
                   useTemplate=str(), ut=str(), value=float(), v=float(), visible=bool(), vis=bool(),
                   visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def flow(divisions=list, dv=list, localCompute=bool(), lc=bool(), localDivisions=list, ld=list, objectCentered=bool(),
         oc=bool(), *args, **kwargs):
    pass


def flowLayout(annotation=str(), ann=str(), backgroundColor=list, bgc=list, childArray=bool(), ca=bool(),
               columnSpacing=int(), cs=int(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
               dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
               enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
               fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, horizontal=bool(),
               hr=bool(), isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
               numberOfChildren=bool(), nch=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
               popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(),
               useTemplate=str(), ut=str(), vertical=bool(), v=bool(), visible=bool(), vis=bool(),
               visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), wrap=bool(), wr=bool(), *args, **kwargs):
    pass


def fluidCacheInfo(attribute=str(), at=str(), cacheTime=float(), t=float(), endFrame=bool(), ef=bool(), hasCache=bool(),
                   hc=bool(), hasData=bool(), hd=bool(), initialConditions=bool(), ic=bool(), playback=bool(),
                   pb=bool(), resolution=bool(), re=bool(), startFrame=bool(), sf=bool(), *args, **kwargs):
    pass


def fluidEmitter(cycleEmission=str(), cye=str(), cycleInterval=int(), cyi=int(), densityEmissionRate=float(),
                 der=float(), fluidDropoff=float(), fdr=float(), fuelEmissionRate=float(), fer=float(),
                 heatEmissionRate=float(), her=float(), maxDistance=float(), mxd=float(), minDistance=float(),
                 mnd=float(), name=str(), n=str(), position=list, pos=list, rate=float(), r=float(),
                 torusSectionRadius=float(), tsr=float(), type=str(), typ=str(), volumeOffset=list, vof=list,
                 volumeShape=str(), vsh=str(), volumeSweep=float(), vsw=float(), *args, **kwargs):
    pass


def fluidVoxelInfo(checkBounds=bool(), cb=bool(), inBounds=list, ib=list, objectSpace=bool(), os=bool(), radius=float(),
                   r=float(), voxel=list, v=list, voxelCenter=bool(), vc=bool(), xIndex=int(), xi=int(), yIndex=int(),
                   yi=int(), zIndex=int(), zi=int(), *args, **kwargs):
    pass


def flushUndo():
    for nd in [x for x in _hierarchy.NodePool.all_nodes() if not x._alive]:
        om._NODE_DESTROYED_SIGNAL.send(nd)


def fontDialog(FontList=bool(), fl=bool(), scalable=bool(), sc=bool(), *args, **kwargs):
    pass


def format(stringArg=str(), s=str(), *args, **kwargs):
    pass


def formLayout(annotation=str(), ann=str(), attachControl=list, ac=list, attachForm=list, af=list, attachNone=list,
               an=list, attachOppositeControl=list, aoc=list, attachOppositeForm=list, aof=list, attachPosition=list,
               ap=list, backgroundColor=list, bgc=list, childArray=bool(), ca=bool(), defineTemplate=str(), dt=str(),
               docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
               en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
               ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
               isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
               numberOfChildren=bool(), nch=bool(), numberOfDivisions=int(), nd=int(), numberOfPopupMenus=bool(),
               npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
               statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
               visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def frameBufferName(autoTruncate=bool(), a=bool(), camera=str(), c=str(), renderLayer=str(), l=str(), renderPass=str(),
                    p=str(), *args, **kwargs):
    pass


def frameLayout(annotation=str(), ann=str(), backgroundColor=list, bgc=list, backgroundShade=bool(), bgs=bool(),
                borderStyle=str(), bs=str(), borderVisible=bool(), bv=bool(), childArray=bool(), ca=bool(),
                collapsable=bool(), cll=bool(), collapse=bool(), cl=bool(), collapseCommand=str(), cc=str(),
                defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), expandCommand=str(), ec=str(),
                font=str(), fn=str(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list,
                hlc=list, isObscured=bool(), io=bool(), label=str(), l=str(), labelAlign=str(), la=str(),
                labelIndent=int(), li=int(), labelVisible=bool(), lv=bool(), labelWidth=int(), lw=int(), manage=bool(),
                m=bool(), marginHeight=int(), mh=int(), marginWidth=int(), mw=int(), noBackground=bool(), nbg=bool(),
                numberOfChildren=bool(), nch=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                popupMenuArray=bool(), pma=bool(), preCollapseCommand=str(), pcc=str(), preExpandCommand=str(),
                pec=str(), preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(),
                ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
                *args, **kwargs):
    pass


def framelessDialog(button=str(), b=str(), message=str(), m=str(), parent=str(), p=str(), path=str(), pat=str(),
                    primary=str(), pr=str(), title=str(), t=str(), *args, **kwargs):
    pass


def freeFormFillet(bias=float(), b=float(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                   depth=float(), d=float(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(),
                   polygon=int(), po=int(), positionTolerance=float(), pt=float(), range=bool(), rn=bool(),
                   tangentTolerance=float(), tt=float(), *args, **kwargs):
    pass


def freeze(allNodes=bool(), all=bool(), displayLayers=bool(), dl=bool(), downstream=bool(), dn=bool(),
           forceDownstream=bool(), fd=bool(), frozen=bool(), f=bool(), invisible=bool(), i=bool(), noFreeze=bool(),
           n=bool(), unfreeze=bool(), uf=bool(), upstream=bool(), up=bool(), *args, **kwargs):
    pass


def freezeOptions(displayLayers=bool(), dl=bool(), downstream=str(), dn=str(), explicitPropagation=bool(), ep=bool(),
                  invisible=bool(), inv=bool(), referencedNodes=bool(), rn=bool(), runtimePropagation=bool(), rt=bool(),
                  upstream=str(), up=str(), *args, **kwargs):
    pass


def geomBind(bindMethod=int(), bm=int(), falloff=float(), fo=float(), geodesicVoxelParams=list, gvp=list,
             maxInfluences=int(), mi=int(), *args, **kwargs):
    pass


def geometryAttrInfo(boundingBox=bool(), bb=bool(), castToEdges=bool(), cte=bool(), castToFaces=bool(), ctf=bool(),
                     castToVerts=bool(), ctv=bool(), componentTagCategory=bool(), ccy=bool(),
                     componentTagExpression=str(), cex=str(), componentTagHash=bool(), hsh=bool(),
                     componentTagHistory=bool(), cth=bool(), componentTagHistoryHash=bool(), chh=bool(),
                     componentTagNames=bool(), cnm=bool(), components=bool(), cmp=bool(), deformerChain=bool(),
                     dch=bool(), elementCount=bool(), ec=bool(), groupId=int(), gid=int(), matrix=bool(), mtx=bool(),
                     nodeChain=bool(), nch=bool(), originalGeometry=bool(), og=bool(), outputPlugChain=bool(),
                     och=bool(), plugChain=bool(), pch=bool(), pointCount=bool(), pc=bool(), pointIndices=bool(),
                     pi=bool(), points=bool(), pnt=bool(), subsetState=bool(), sbs=bool(), *args, **kwargs):
    pass


def geometryConstraint(layer=str(), l=str(), name=str(), n=str(), remove=bool(), rm=bool(), targetList=bool(),
                       tl=bool(), weight=float(), w=float(), weightAliasList=bool(), wal=bool(), *args, **kwargs):
    pass


def geomToBBox(bakeAnimation=bool(), ba=bool(), combineMesh=bool(), cm=bool(), endTime=float(), et=float(),
               keepOriginal=bool(), ko=bool(), name=str(), n=str(), nameSuffix=str(), ns=str(), sampleBy=float(),
               sb=float(), shaderColor=list, sc=list, single=bool(), s=bool(), startTime=float(), st=float(), *args,
               **kwargs):
    pass


def getAttr(attribute_name, asString=bool(), caching=bool(), ca=bool(), channelBox=bool(), cb=bool(), expandEnvironmentVariables=bool(),
            x=bool(), keyable=bool(), k=bool(), lock=bool(), l=bool(), multiIndices=bool(), mi=bool(), settable=bool(),
            se=bool(), silent=bool(), sl=bool(), size=bool(), s=bool(), time=float(), t=float(), type=bool(),
            typ=bool(), *args, **kwargs):

    full_name: str = attribute_name
    node_name, attr_name= full_name.split('.')
    node_mobject = _hierarchy.NodePool.from_name(node_name)
    return om.MFnDependencyNode(node_mobject).findPlug(attr_name, False).attribute()._value


def getClassification(satisfies=str(), sat=str(), *args, **kwargs):
    pass


def getDefaultBrush(*args, **kwargs):
    pass


def getFileList(filespec=str(), fs=str(), folder=str(), fld=str(), *args, **kwargs):
    pass


def getFluidAttr(attribute=str(), at=str(), lowerFace=bool(), lf=bool(), xIndex=int(), xi=int(), xvalue=bool(),
                 x=bool(), yIndex=int(), yi=int(), yvalue=bool(), y=bool(), zIndex=int(), zi=int(), zvalue=bool(),
                 z=bool(), *args, **kwargs):
    pass


def getInputDeviceRange(maxValue=bool(), max=bool(), minValue=bool(), min=bool(), *args, **kwargs):
    pass


def getMetadata(channelName=str(), cn=str(), channelType=str(), cht=str(), dataType=bool(), dt=bool(), endIndex=str(),
                eix=str(), index=str(), idx=str(), indexType=str(), idt=str(), listChannelNames=bool(), lcn=bool(),
                listMemberNames=bool(), lmn=bool(), listStreamNames=bool(), lsn=bool(), memberName=str(), mn=str(),
                scene=bool(), scn=bool(), startIndex=str(), six=str(), streamName=str(), stn=str(), *args, **kwargs):
    pass


def getModifiers(*args, **kwargs):
    pass


def getModulePath(moduleName=str(), mn=str(), *args, **kwargs):
    pass


def getPanel(allConfigs=bool(), ac=bool(), allPanels=bool(), all=bool(), allScriptedTypes=bool(), ast=bool(),
             allTypes=bool(), at=bool(), atPosition=list, ap=list, configWithLabel=str(), cwl=str(), containing=str(),
             c=str(), invisiblePanels=bool(), inv=bool(), scriptType=str(), sty=str(), type=str(), typ=str(),
             typeOf=str(), to=str(), underPointer=bool(), up=bool(), visiblePanels=bool(), vis=bool(), withFocus=bool(),
             wf=bool(), withLabel=str(), wl=str(), *args, **kwargs):
    pass


def getParticleAttr(array=bool(), a=bool(), attribute=str(), at=str(), object=str(), o=str(), *args, **kwargs):
    pass


def getRenderDependencies(*args, **kwargs):
    pass


def getRenderTasks(camera=str(), c=str(), renderLayer=str(), rl=str(), *args, **kwargs):
    pass


def ghosting(action=str(), act=str(), allGhostedObjects=bool(), ago=bool(), allInRange=bool(), a=bool(),
             customFrames=int(), cf=int(), enable=bool(), en=bool(), farOpacity=float(), fo=float(), frames=bool(),
             f=bool(), geometryFilter=bool(), gf=bool(), ghostedObjects=bool(), go=bool(), ghostsStep=int(), gs=int(),
             hierarchy=bool(), h=bool(), jointFilter=bool(), jf=bool(), locatorFilter=bool(), lf=bool(), mode=str(),
             m=str(), nearOpacity=float(), no=float(), postColor=list, poc=list, postFrames=int(), pof=int(),
             preColor=list, prc=list, preFrames=int(), prf=int(), preset=str(), p=str(), resetAll=bool(), r=bool(),
             useDriver=bool(), ud=bool(), *args, **kwargs):
    pass


def globalStitch(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), lockSurface=bool(), lk=bool(),
                 maxSeparation=float(), ms=float(), modificationResistance=float(), mr=float(), name=str(), n=str(),
                 nodeState=int(), nds=int(), object=bool(), o=bool(), sampling=int(), sam=int(), stitchCorners=int(),
                 sc=int(), stitchEdges=int(), se=int(), stitchPartialEdges=bool(), spe=bool(), stitchSmoothness=int(),
                 ss=int(), *args, **kwargs):
    pass


def glRender(accumBufferPasses=int(), abp=int(), alphaSource=str(), antiAliasMethod=str(), aam=str(),
             cameraIcons=bool(), ci=bool(), clearClr=list, cc=list, collisionIcons=bool(), coi=bool(),
             crossingEffect=bool(), ce=bool(), currentFrame=bool(), cf=bool(), drawStyle=str(), ds=str(),
             edgeSmoothness=float(), es=float(), emitterIcons=bool(), ei=bool(), fieldIcons=bool(), fii=bool(),
             flipbookCallback=str(), fc=str(), frameEnd=int(), fe=int(), frameIncrement=int(), fi=int(),
             frameStart=int(), fs=int(), fullResolution=bool(), fr=bool(), grid=bool(), gr=bool(), imageDirectory=str(),
             id=str(), imageName=str(), imageSize=list, lightIcons=bool(), li=bool(), lightingMode=str(), lm=str(),
             lineSmoothing=bool(), ls=bool(), offScreen=bool(), os=bool(), renderFrame=str(), rf=str(),
             renderSequence=str(), rs=str(), sharpness=float(), sh=float(), shutterAngle=float(), sa=float(),
             textureDisplay=bool(), txd=bool(), transformIcons=bool(), ti=bool(), useAccumBuffer=bool(), uab=bool(),
             viewport=list, vp=list, writeDepthMap=bool(), wdm=bool(), *args, **kwargs):
    pass


def glRenderEditor(control=bool(), ctl=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), exists=bool(),
                   ex=bool(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(), highlightConnection=str(),
                   hlc=str(), lockMainConnection=bool(), lck=bool(), lookThru=str(), lt=str(), mainListConnection=str(),
                   mlc=str(), panel=str(), pnl=str(), parent=str(), p=str(), selectionConnection=str(), slc=str(),
                   stateString=bool(), sts=bool(), unParent=bool(), up=bool(), unlockMainConnection=bool(), ulk=bool(),
                   updateMainConnection=bool(), upd=bool(), useTemplate=str(), ut=str(), viewCameraName=bool(),
                   vcn=bool(), *args, **kwargs):
    pass


def goal(goal=str(), g=str(), index=bool(), i=bool(), useTransformAsGoal=bool(), utr=bool(), weight=float(), w=float(),
         *args, **kwargs):
    pass


def grabColor(hsvValue=bool(), hsv=bool(), rgbValue=bool(), rgb=bool(), *args, **kwargs):
    pass


def gradientControl(adaptiveScaling=bool(), annotation=str(), ann=str(), attribute=str(), at=str(),
                    backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                    dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                    enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                    ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                    isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                    numberOfControls=int(), nc=int(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                    popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), refreshOnRelease=int(),
                    ror=int(), selectedColorControl=str(), scc=str(), selectedInterpControl=str(), sic=str(),
                    selectedPositionControl=str(), spc=str(), staticNumberOfControls=bool(), snc=bool(),
                    staticPositions=bool(), sp=bool(), statusBarMessage=str(), sbm=str(), upperLimitControl=str(),
                    ulc=str(), useTemplate=str(), ut=str(), verticalLayout=bool(), vl=bool(), visible=bool(),
                    vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def gradientControlNoAttr(annotation=str(), ann=str(), asString=str(), backgroundColor=list, bgc=list,
                          changeCommand=str(), cc=str(), currentKey=int(), ck=int(), currentKeyChanged=str(), ckc=str(),
                          currentKeyColorValue=list, clv=list, currentKeyCurveValue=bool(), cvv=bool(),
                          currentKeyInterpValue=int(), civ=int(), defineTemplate=str(), dt=str(), docTag=str(),
                          dtg=str(), dragCallback=str(), dgc=str(), dragCommand=str(), dc=str(), dropCallback=str(),
                          dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                          enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(),
                          fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(),
                          io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                          numberOfPopupMenus=bool(), npm=bool(), optionVar=str(), ov=str(), parent=str(), p=str(),
                          popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rampAsColor=bool(),
                          rac=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
                          valueAtPoint=float(), vap=float(), visible=bool(), vis=bool(), visibleChangeCommand=str(),
                          vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def graphDollyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                  image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def graphSelectContext(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                       *args, **kwargs):
    pass


def graphTrackCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                  image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def gravity(attenuation=float(), att=float(), directionX=float(), dx=float(), directionY=float(), dy=float(),
            directionZ=float(), dz=float(), magnitude=float(), m=float(), maxDistance=float(), mxd=float(), name=str(),
            n=str(), perVertex=bool(), pv=bool(), position=list, pos=list, torusSectionRadius=float(), tsr=float(),
            volumeExclusion=bool(), vex=bool(), volumeOffset=list, vof=list, volumeShape=str(), vsh=str(),
            volumeSweep=float(), vsw=float(), *args, **kwargs):
    pass


def greasePencilCtx(autoCreateFrames=bool(), acf=bool(), canDraw=bool(), cd=bool(), createOrEditFrame=int(), cef=int(),
                    exists=bool(), ex=bool(), exportArchive=list, eac=list, fileTextureSize=int(), fts=int(),
                    greasePencilType=int(), gpt=int(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(),
                    i3=str(), importArchive=str(), iac=str(), makeStroke=int(), mst=int(), removeFrame=int(), rf=int(),
                    resetBrushes=bool(), rb=bool(), rgbcolor=list, rgb=list, sequenceNodeName=str(), snn=str(), *args,
                    **kwargs):
    pass


def grid(default=bool(), df=bool(), displayAxes=bool(), da=bool(), displayAxesBold=bool(), dab=bool(),
         displayDivisionLines=bool(), ddl=bool(), displayGridLines=bool(), dgl=bool(), displayOrthographicLabels=bool(),
         dol=bool(), displayPerspectiveLabels=bool(), dpl=bool(), divisions=int(), d=int(), drawInfiniteGrid=bool(),
         dig=bool(), drawMinimumCameraDistance=float(), dmd=float(), fogBase=float(), fb=float(), fogEnabled=bool(),
         fog=bool(), fogMinimumCameraDistance=float(), fmd=float(), fogPower=float(), fp=float(),
         gridSizeCameraDistanceFactor=float(), cdf=float(), gridSizeFixed=bool(), gsf=bool(),
         gridSizeLogFactorAdjustment=float(), lfa=float(), gridSizeMinimum=float(), gsm=float(), gridSizeVarying=bool(),
         gsv=bool(), lineWidth=float(), lw=float(), majorColor=list, mac=list, minorColor=list, mic=list,
         normalAxis=int(), na=int(), orthographicLabelPosition=str(), olp=str(), perspectiveLabelPosition=str(),
         plp=str(), reset=bool(), r=bool(), size=float(), s=float(), spacing=float(), sp=float(), style=int(), st=int(),
         toggle=bool(), tgl=bool(), xAxisColor=list, xac=list, yAxisColor=list, yac=list, zAxisColor=list, zac=list,
         *args, **kwargs):
    pass


def gridLayout(allowEmptyCells=bool(), aec=bool(), annotation=str(), ann=str(), autoGrow=bool(), ag=bool(),
               backgroundColor=list, bgc=list, cellHeight=int(), ch=int(), cellWidth=int(), cw=int(),
               cellWidthHeight=list, cwh=list, childArray=bool(), ca=bool(), columnsResizable=bool(), cr=bool(),
               defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
               dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
               enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(),
               gridOrder=bool(), go=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(),
               io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), numberOfChildren=bool(), nch=bool(),
               numberOfColumns=int(), nc=int(), numberOfPopupMenus=bool(), npm=bool(), numberOfRows=int(), nr=int(),
               numberOfRowsColumns=list, nrc=list, parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
               position=list, pos=list, preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(),
               useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
               width=int(), w=int(), *args, **kwargs):
    pass


def group(absolute=bool(), a=bool(), empty=bool(), em=bool(), name=str(), n=str(), parent=str(), p=str(),
          relative=bool(), r=bool(), useAsGroup=str(), uag=str(), world=bool(), w=bool(), *args, **kwargs):
    pass


def hardenPointCurve(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), multiplicity=int(), m=int(),
                     name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), replaceOriginal=bool(),
                     rpo=bool(), *args, **kwargs):
    pass


def hardware(brdType=bool(), brd=bool(), cpuType=bool(), cpu=bool(), graphicsType=bool(), gfx=bool(), megaHertz=bool(),
             mhz=bool(), numProcessors=bool(), npr=bool(), *args, **kwargs):
    pass


def hardwareRenderPanel(camera=str(), cam=str(), control=bool(), ctl=bool(), copy=str(), cp=str(), createString=bool(),
                        cs=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), editString=bool(),
                        es=bool(), exists=bool(), ex=bool(), glRenderEditor=bool(), gre=bool(), init=bool(),
                        isUnique=bool(), iu=bool(), label=str(), l=str(), menuBarRepeatLast=bool(), mrl=bool(),
                        menuBarVisible=bool(), mbv=bool(), needsInit=bool(), ni=bool(), parent=str(), p=str(),
                        popupMenuProcedure=str(), pmp=str(), replacePanel=str(), rp=str(), tearOff=bool(), to=bool(),
                        tearOffCopy=str(), toc=str(), tearOffRestore=bool(), tor=bool(), unParent=bool(), up=bool(),
                        useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def hasMetadata(asList=bool(), al=bool(), channelName=str(), cn=str(), channelType=str(), cht=str(), endIndex=str(),
                eix=str(), ignoreDefault=bool(), id=bool(), index=str(), idx=str(), indexType=str(), idt=str(),
                memberName=str(), mn=str(), scene=bool(), scn=bool(), startIndex=str(), six=str(), streamName=str(),
                stn=str(), *args, **kwargs):
    pass


def headsUpDisplay(allDescendants=bool(), ad=bool(), allowOverlap=bool(), ao=bool(), attachToRefresh=bool(), atr=bool(),
                   attributeChange=str(), ac=str(), block=int(), b=int(), blockAlignment=str(), ba=str(),
                   blockSize=str(), bs=str(), command=str(), c=str(), conditionChange=str(), cc=str(),
                   conditionFalse=str(), cf=str(), conditionTrue=str(), ct=str(), connectionChange=str(), con=str(),
                   dataAlignment=str(), da=str(), dataFontSize=str(), dfs=str(), dataWidth=int(), dw=int(),
                   decimalPrecision=int(), dp=int(), disregardIndex=bool(), di=bool(), event=str(), ev=str(),
                   exists=bool(), ex=bool(), getOption=str(), op=str(), gridColor=int(), gco=int(), label=str(),
                   l=str(), labelFontSize=str(), lfs=str(), labelWidth=int(), lw=int(), lastOccupiedBlock=int(),
                   lob=int(), layoutVisibility=bool(), lv=bool(), listConditions=bool(), lc=bool(), listEvents=bool(),
                   le=bool(), listHeadsUpDisplays=bool(), lh=bool(), listNodeChanges=bool(), lnc=bool(),
                   listPresets=bool(), lp=bool(), name=str(), n=str(), nextFreeBlock=int(), nfb=int(),
                   nodeChanges=str(), nc=str(), padding=int(), p=int(), preset=str(), pre=str(), refresh=bool(),
                   r=bool(), remove=bool(), rem=bool(), removeID=int(), rid=int(), removePosition=list, rp=list,
                   resetNodeChanges=str(), rnc=str(), scriptResult=bool(), sr=bool(), section=int(), s=int(),
                   setOption=list, so=list, showGrid=bool(), sg=bool(), visible=bool(), vis=bool(), *args, **kwargs):
    pass


def headsUpMessage(horizontalOffset=int(), ho=int(), object=str(), o=str(), selection=bool(), s=bool(), time=float(),
                   t=float(), uvTextureEditor=bool(), uve=bool(), verticalOffset=int(), vo=int(), viewport=bool(),
                   vp=bool(), *args, **kwargs):
    pass


def help(documentation=bool(), doc=bool(), language=str(), lng=str(), list=bool(), l=bool(), popupDisplayTime=int(),
         pdt=int(), popupMode=bool(), pm=bool(), popupPauseTime=int(), ppt=int(), popupSimpleMode=bool(), psm=bool(),
         rolloverMode=bool(), rm=bool(), syntaxOnly=bool(), so=bool(), *args, **kwargs):
    pass


def helpLine(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(), docTag=str(),
             dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
             enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
             fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(),
             io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(),
             parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
             statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
             visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def hide(allObjects=bool(), all=bool(), clearLastHidden=bool(), clh=bool(), clearSelection=bool(), cs=bool(),
         invertComponents=bool(), ic=bool(), returnHidden=bool(), rh=bool(), testVisibility=bool(), tv=bool(), *args,
         **kwargs):
    pass


def hikGlobals(releaseAllPinning=bool(), rap=bool(), *args, **kwargs):
    pass


def hilite(replace=bool(), r=bool(), toggle=bool(), tgl=bool(), unHilite=bool(), u=bool(), *args, **kwargs):
    pass


def hitTest(*args, **kwargs):
    pass


def hotBox(PaneOnlyMenus=bool(), po=bool(), PaneToggleMenus=bool(), pt=bool(), animationOnlyMenus=bool(), ao=bool(),
           animationToggleMenus=bool(), at=bool(), clothOnlyMenus=bool(), clo=bool(), clothToggleMenus=bool(),
           clt=bool(), commonOnlyMenus=bool(), co=bool(), commonToggleMenus=bool(), ct=bool(),
           customMenuSetsToggleMenus=bool(), cst=bool(), displayCenterOnly=bool(), dco=bool(), displayHotbox=bool(),
           dh=bool(), displayStyle=bool(), ds=bool(), displayZonesOnly=bool(), dzo=bool(), dynamicsOnlyMenus=bool(),
           do=bool(), dynamicsToggleMenus=bool(), dt=bool(), liveOnlyMenus=bool(), lo=bool(), liveToggleMenus=bool(),
           lt=bool(), menuSetOnly=str(), mso=str(), menuSetToggle=list, mst=list, modelingOnlyMenus=bool(), mdo=bool(),
           modelingToggleMenus=bool(), mdt=bool(), noClickCommand=str(), ncc=str(), noClickDelay=float(), ncd=float(),
           noClickPosition=bool(), ncp=bool(), noKeyPress=bool(), nkp=bool(), polygonsOnlyMenus=bool(), plo=bool(),
           polygonsToggleMenus=bool(), plt=bool(), position=list, pos=list, release=bool(), rl=bool(),
           renderingOnlyMenus=bool(), ro=bool(), renderingToggleMenus=bool(), rt=bool(), riggingOnlyMenus=bool(),
           rgo=bool(), riggingToggleMenus=bool(), rgt=bool(), rmbPopups=bool(), rmb=bool(), showAllToggleMenus=bool(),
           a=bool(), surfacesOnlyMenus=bool(), so=bool(), surfacesToggleMenus=bool(), st=bool(), transparenyLevel=int(),
           tr=int(), updateMenus=bool(), um=bool(), *args, **kwargs):
    pass


def hotkey(altModifier=bool(), alt=bool(), autoSave=bool(), commandModifier=bool(), cmd=bool(), ctrlModifier=bool(),
           ctl=bool(), ctxClient=str(), cc=str(), dragPress=bool(), dp=bool(), factorySettings=bool(), fs=bool(),
           isModifier=bool(), mod=bool(), keyShortcut=str(), k=str(), name=str(), n=str(), pressCommandRepeat=bool(),
           pcr=bool(), releaseCommandRepeat=bool(), rcr=bool(), releaseName=str(), rn=str(), shiftModifier=bool(),
           sht=bool(), sourceUserHotkeys=bool(), suh=bool(), *args, **kwargs):
    pass


def hotkeyCheck(altModifier=bool(), alt=bool(), commandModifier=bool(), cmd=bool(), ctrlModifier=bool(), ctl=bool(),
                isRepeatable=bool(), ir=bool(), keyString=str(), k=str(), keyUp=bool(), kup=bool(),
                optionModifier=bool(), opt=bool(), *args, **kwargs):
    pass


def hotkeyCtx(addClient=str(), ac=str(), clientArray=bool(), ca=bool(), currentClient=str(), cc=str(),
              insertTypeAt=list, ita=list, removeAllClients=bool(), rac=bool(), removeClient=str(), rc=str(),
              removeType=str(), rt=str(), type=str(), t=str(), typeArray=bool(), ta=bool(), typeExists=str(), te=str(),
              *args, **kwargs):
    pass


def hotkeyEditorPanel(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(),
                      docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
                      enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                      ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                      highlightColor=list, hlc=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(),
                      noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                      popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), statusBarMessage=str(),
                      sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(),
                      vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def hotkeySet(current=bool(), cu=bool(), delete=bool(), exists=bool(), ex=bool(), export=str(), ep=str(),
              hotkeySetArray=bool(), hsa=bool(), ip=str(), rename=str(), re=str(), source=str(), src=str(), *args,
              **kwargs):
    pass


def hudButton(allowOverlap=bool(), ao=bool(), block=int(), b=int(), blockAlignment=str(), ba=str(), blockSize=str(),
              bs=str(), buttonShape=str(), bsh=str(), buttonWidth=int(), bw=int(), label=str(), l=str(),
              labelFontSize=str(), lfs=str(), padding=int(), p=int(), pressCommand=str(), pc=str(),
              releaseCommand=str(), rc=str(), section=int(), s=int(), visible=bool(), vis=bool(), *args, **kwargs):
    pass


def hudSlider(allowOverlap=bool(), ao=bool(), block=int(), b=int(), blockAlignment=str(), ba=str(), blockSize=str(),
              bs=str(), decimalPrecision=int(), dp=int(), dragCommand=str(), dc=str(), internalPadding=int(), ip=int(),
              label=str(), l=str(), labelFontSize=str(), lfs=str(), labelWidth=int(), lw=int(), maxValue=float(),
              max=float(), minValue=float(), min=float(), padding=int(), p=int(), pressCommand=str(), pc=str(),
              releaseCommand=str(), rc=str(), section=int(), s=int(), sliderIncrement=float(), si=float(),
              sliderLength=int(), sl=int(), type=str(), t=str(), value=float(), v=float(), valueAlignment=str(),
              va=str(), valueFontSize=str(), vfs=str(), valueWidth=int(), vw=int(), visible=bool(), vis=bool(), *args,
              **kwargs):
    pass


def hudSliderButton(allowOverlap=bool(), ao=bool(), block=int(), b=int(), blockAlignment=str(), ba=str(),
                    blockSize=str(), bs=str(), buttonLabel=str(), bl=str(), buttonLabelFontSize=str(), bfs=str(),
                    buttonPressCommand=str(), bpc=str(), buttonReleaseCommand=str(), brc=str(), buttonShape=str(),
                    bsh=str(), buttonWidth=int(), bw=int(), decimalPrecision=int(), dp=int(), internalPadding=int(),
                    ip=int(), maxValue=float(), max=float(), minValue=float(), min=float(), padding=int(), p=int(),
                    section=int(), s=int(), sliderDragCommand=str(), sdc=str(), sliderIncrement=float(), si=float(),
                    sliderLabel=str(), sl=str(), sliderLabelFontSize=str(), sfs=str(), sliderLabelWidth=int(),
                    slw=int(), sliderLength=int(), sln=int(), sliderPressCommand=str(), spc=str(),
                    sliderReleaseCommand=str(), src=str(), type=str(), t=str(), value=float(), v=float(),
                    valueAlignment=str(), va=str(), valueFontSize=str(), vfs=str(), valueWidth=int(), vw=int(),
                    visible=bool(), vis=bool(), *args, **kwargs):
    pass


def hwReflectionMap(backTextureName=str(), bkn=str(), bottomTextureName=str(), bmn=str(), cubeMap=bool(), cm=bool(),
                    decalMode=bool(), dm=bool(), enable=bool(), en=bool(), frontTextureName=str(), ftn=str(),
                    leftTextureName=str(), ltn=str(), rightTextureName=str(), rtn=str(), sphereMapTextureName=str(),
                    smn=str(), topTextureName=str(), tpn=str(), *args, **kwargs):
    pass


def hwRender(acceleratedMultiSampleSupport=bool(), ams=bool(), activeTextureCount=bool(), atc=bool(), camera=str(),
             cam=str(), currentFrame=bool(), cf=bool(), currentView=bool(), cv=bool(), edgeAntiAliasing=list, eaa=list,
             fixFileNameNumberPattern=bool(), fnp=bool(), frame=float(), f=float(), fullRenderSupport=bool(),
             frs=bool(), height=int(), h=int(), imageFileName=bool(), ifn=bool(), layer=str(), l=str(),
             limitedRenderSupport=bool(), lrs=bool(), lowQualityLighting=bool(), lql=bool(), noRenderView=bool(),
             nrv=bool(), notWriteToFile=bool(), nwf=bool(), printGeometry=bool(), pg=bool(), renderHardwareName=bool(),
             rhw=bool(), renderRegion=list, reg=list, renderSelected=bool(), rs=bool(), textureResolution=int(),
             res=int(), width=int(), w=int(), writeAlpha=bool(), a=bool(), writeDepth=bool(), d=bool(), *args,
             **kwargs):
    pass


def hwRenderLoad(*args, **kwargs):
    pass


def hyperGraph(addBookmark=bool(), abk=bool(), addDependGraph=str(), adg=str(), addDependNode=str(), adn=str(),
               animateTransition=bool(), atr=bool(), attributeEditor=str(), ae=str(), backward=bool(), bak=bool(),
               bookmarkName=bool(), bn=bool(), breakConnectionCommand=str(), bco=str(), clear=bool(), clr=bool(),
               collapseContainer=bool(), cc=bool(), connectionDrawStyle=str(), cds=str(), control=bool(), ctl=bool(),
               currentEdge=str(), ced=str(), currentNode=str(), cno=str(), debug=str(), deb=str(), defineTemplate=str(),
               dt=str(), deleteBookmark=str(), dbk=str(), dependGraph=bool(), dg=bool(), dependNode=str(), dn=str(),
               directoryPressCommand=str(), dp=str(), docTag=str(), dtg=str(), down=bool(), do=bool(),
               downstream=bool(), ds=bool(), dragAndDropBehaviorCommand=str(), ddc=str(), dropNode=str(), dr=str(),
               dropTargetNode=str(), drt=str(), edgeDblClickCommand=str(), edc=str(), edgeDimmedDblClickCommand=str(),
               edd=str(), edgeDropCommand=str(), edr=str(), edgePressCommand=str(), ep=str(), edgeReleaseCommand=str(),
               er=str(), enableAutomaticLayout=bool(), eal=bool(), exists=bool(), ex=bool(), expandContainer=bool(),
               ec=bool(), feedbackGadget=str(), fbg=str(), feedbackNode=str(), fbn=str(), filter=str(), f=str(),
               filterDetail=list, fd=list, fitImageToHeight=bool(), fih=bool(), fitImageToWidth=bool(), fiw=bool(),
               focusCommand=str(), fc=str(), fold=bool(), fo=bool(), forceMainConnection=str(), fmc=str(),
               forceRefresh=bool(), frf=bool(), forward=bool(), fow=bool(), frame=bool(), fr=bool(), frameBranch=bool(),
               frb=bool(), frameGraph=bool(), fg=bool(), frameGraphNoRebuild=bool(), fgn=bool(), frameHierarchy=bool(),
               frh=bool(), freeform=bool(), fre=bool(), fromAttr=str(), fat=str(), fromNode=str(), frn=str(),
               getNodeList=bool(), gnl=bool(), getNodePosition=str(), gnp=str(), graphDescription=bool(), gd=bool(),
               graphLayoutStyle=str(), gls=str(), graphType=str(), gt=str(), heatMapDisplay=bool(), hmd=bool(),
               highlightConnection=str(), hlc=str(), iconSize=str(), ics=str(), image=str(), img=str(),
               imageEnabled=bool(), ime=bool(), imageForContainer=bool(), ifc=bool(), imagePosition=list, imp=list,
               imageScale=float(), ims=float(), initializeScript=str(), ini=str(), isHotkeyTarget=bool(), iht=bool(),
               layout=bool(), lay=bool(), layoutSelected=str(), lsl=str(), limitGraphTraversal=int(), lgt=int(),
               lockMainConnection=bool(), lck=bool(), look=list, loo=list, mainListConnection=str(), mlc=str(),
               mergeConnections=bool(), mc=bool(), navigateHome=bool(), hom=bool(), navup=bool(), nu=bool(),
               newInputConnection=str(), nin=str(), newOutputConnection=str(), nou=str(), nextView=bool(), nvw=bool(),
               nodeConnectCommand=str(), nco=str(), nodeDblClickCommand=str(), ndc=str(), nodeDropCommand=str(),
               ndr=str(), nodeMenuCommand=str(), nm=str(), nodePressCommand=str(), np=str(), nodeReleaseCommand=str(),
               nr=str(), opaqueContainers=bool(), opc=bool(), orientation=str(), panView=list, pan=list, panel=str(),
               pnl=str(), parent=str(), p=str(), popupMenuScript=str(), pms=str(), previousView=bool(), pvw=bool(),
               range=list, rg=list, rebuild=bool(), rb=bool(), removeNode=str(), rmn=str(), rename=bool(), rn=bool(),
               resetFreeform=bool(), rf=bool(), restoreBookmark=str(), rbk=str(), scrollUpDownNoZoom=bool(), snz=bool(),
               selectionConnection=str(), slc=str(), setNodePosition=list, snp=list, showCachedConnections=bool(),
               scc=bool(), showConnectionFromSelected=bool(), scf=bool(), showConnectionToSelected=bool(), sct=bool(),
               showConstraintLabels=bool(), scl=bool(), showConstraints=bool(), shc=bool(), showDeformers=bool(),
               shd=bool(), showExpressions=bool(), shx=bool(), showInvisible=bool(), shi=bool(),
               showRelationships=bool(), shr=bool(), showShapes=bool(), shs=bool(), showUnderworld=bool(), shu=bool(),
               stateString=bool(), sts=bool(), toAttr=str(), tat=str(), toNode=str(), ton=str(), transitionFrames=int(),
               tfr=int(), unParent=bool(), up=bool(), unfold=bool(), uf=bool(), unfoldAll=bool(), ua=bool(),
               unfoldAllShapes=bool(), uas=bool(), unfoldHidden=bool(), ufh=bool(), unlockMainConnection=bool(),
               ulk=bool(), updateMainConnection=bool(), upd=bool(), updateNodeAdded=bool(), una=bool(),
               updateSelection=bool(), us=bool(), upstream=bool(), ups=bool(), useDrawOverrideColor=bool(), drc=bool(),
               useFeedbackList=bool(), ufl=bool(), useTemplate=str(), ut=str(), viewOption=str(), vo=str(),
               visibility=bool(), vis=bool(), zoom=float(), zm=float(), *args, **kwargs):
    pass


def hyperPanel(control=bool(), ctl=bool(), copy=str(), cp=str(), createString=bool(), cs=bool(), defineTemplate=str(),
               dt=str(), docTag=str(), dtg=str(), editString=bool(), es=bool(), exists=bool(), ex=bool(),
               hyperEditor=bool(), he=bool(), init=bool(), isUnique=bool(), iu=bool(), label=str(), l=str(),
               menuBarRepeatLast=bool(), mrl=bool(), menuBarVisible=bool(), mbv=bool(), needsInit=bool(), ni=bool(),
               parent=str(), p=str(), popupMenuProcedure=str(), pmp=str(), replacePanel=str(), rp=str(), tearOff=bool(),
               to=bool(), tearOffCopy=str(), toc=str(), tearOffRestore=bool(), tor=bool(), unParent=bool(), up=bool(),
               useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def hyperShade(assign=str(), a=str(), clearWorkArea=bool(), cwa=bool(), collapse=str(), clp=str(), createNode=str(),
               rcn=str(), dependGraphArea=bool(), dg=bool(), downStream=bool(), ds=bool(), duplicate=bool(), dup=bool(),
               fixRenderSize=bool(), fix=bool(), incremental=bool(), inc=bool(), listDownstreamNodes=str(), ldn=str(),
               listDownstreamShaderNodes=str(), lds=str(), listUpstreamNodes=str(), lun=str(), name=str(), n=str(),
               networks=bool(), net=bool(), noSGShapes=bool(), nsg=bool(), noShapes=bool(), ns=bool(),
               noTransforms=bool(), nt=bool(), objects=str(), o=str(), renderCreateAndDrop=str(), rcd=str(),
               reset=bool(), rst=bool(), resetGraph=bool(), rsg=bool(), resetSwatch=bool(), rss=bool(),
               setAllowsRegraphing=bool(), sar=bool(), setWorkArea=str(), swa=str(), shaderNetwork=str(), sn=str(),
               shaderNetworks=bool(), sns=bool(), shaderNetworksSelectMaterialNodes=bool(), smn=bool(), snapShot=bool(),
               snp=bool(), uncollapse=str(), ucl=str(), upStream=bool(), ups=bool(), userDefinedLayout=bool(),
               udl=bool(), workAreaAddCmd=str(), waa=str(), workAreaDeleteCmd=str(), wad=str(), workAreaSelectCmd=str(),
               was=str(), *args, **kwargs):
    pass


def iconTextButton(align=str(), al=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list, command=str(),
                   c=str(), commandRepeatable=bool(), rpt=bool(), defineTemplate=str(), dt=str(), disabledImage=str(),
                   di=str(), docTag=str(), dtg=str(), doubleClickCommand=str(), dcc=str(), dragCallback=str(),
                   dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(),
                   ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), flat=bool(),
                   fla=bool(), flipX=bool(), fx=bool(), flipY=bool(), fy=bool(), font=str(), fn=str(),
                   fullPathName=bool(), fpn=bool(), handleNodeDropCallback=str(), hnd=str(), height=int(), h=int(),
                   highlightColor=list, hlc=list, highlightImage=str(), hi=str(), image=str(), i=str(), image1=str(),
                   i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), imageOverlayLabel=str(), iol=str(),
                   isObscured=bool(), io=bool(), label=str(), l=str(), labelEditingCallback=str(), lec=str(),
                   labelOffset=int(), lo=int(), ltVersion=str(), lt=str(), manage=bool(), m=bool(), marginHeight=int(),
                   mh=int(), marginWidth=int(), mw=int(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(),
                   npm=bool(), overlayLabelBackColor=list, olb=list, overlayLabelColor=list, olc=list, parent=str(),
                   p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rotation=float(),
                   rot=float(), scaleIcon=bool(), sic=bool(), selectionImage=str(), si=str(), sourceType=str(),
                   stp=str(), statusBarMessage=str(), sbm=str(), style=str(), st=str(), useAlpha=bool(), ua=bool(),
                   useTemplate=str(), ut=str(), version=str(), ver=str(), visible=bool(), vis=bool(),
                   visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def iconTextCheckBox(align=str(), al=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                     changeCommand=str(), cc=str(), defineTemplate=str(), dt=str(), disabledImage=str(), di=str(),
                     docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
                     enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                     ekf=bool(), exists=bool(), ex=bool(), flat=bool(), fla=bool(), flipX=bool(), fx=bool(),
                     flipY=bool(), fy=bool(), font=str(), fn=str(), fullPathName=bool(), fpn=bool(), height=int(),
                     h=int(), highlightColor=list, hlc=list, highlightImage=str(), hi=str(), image=str(), i=str(),
                     image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), imageOverlayLabel=str(),
                     iol=str(), isObscured=bool(), io=bool(), label=str(), l=str(), labelOffset=int(), lo=int(),
                     ltVersion=str(), lt=str(), manage=bool(), m=bool(), marginHeight=int(), mh=int(),
                     marginWidth=int(), mw=int(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(),
                     npm=bool(), offCommand=str(), ofc=str(), onCommand=str(), onc=str(), overlayLabelBackColor=list,
                     olb=list, overlayLabelColor=list, olc=list, parent=str(), p=str(), popupMenuArray=bool(),
                     pma=bool(), preventOverride=bool(), po=bool(), rotation=float(), rot=float(),
                     selectionHighlightImage=str(), shi=str(), selectionImage=str(), si=str(), statusBarMessage=str(),
                     sbm=str(), style=str(), st=str(), useAlpha=bool(), ua=bool(), useTemplate=str(), ut=str(),
                     value=bool(), v=bool(), version=str(), ver=str(), visible=bool(), vis=bool(),
                     visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def iconTextRadioButton(align=str(), al=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                        changeCommand=str(), cc=str(), collection=str(), cl=str(), defineTemplate=str(), dt=str(),
                        disabledImage=str(), di=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                        dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                        enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), flat=bool(), fla=bool(),
                        flipX=bool(), fx=bool(), flipY=bool(), fy=bool(), font=str(), fn=str(), fullPathName=bool(),
                        fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, highlightImage=str(),
                        hi=str(), image=str(), i=str(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(),
                        i3=str(), imageOverlayLabel=str(), iol=str(), isObscured=bool(), io=bool(), label=str(),
                        l=str(), labelOffset=int(), lo=int(), ltVersion=str(), lt=str(), manage=bool(), m=bool(),
                        marginHeight=int(), mh=int(), marginWidth=int(), mw=int(), noBackground=bool(), nbg=bool(),
                        numberOfPopupMenus=bool(), npm=bool(), offCommand=str(), ofc=str(), onCommand=str(), onc=str(),
                        overlayLabelBackColor=list, olb=list, overlayLabelColor=list, olc=list, parent=str(), p=str(),
                        popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rotation=float(),
                        rot=float(), select=bool(), sl=bool(), selectionHighlightImage=str(), shi=str(),
                        selectionImage=str(), si=str(), statusBarMessage=str(), sbm=str(), style=str(), st=str(),
                        useAlpha=bool(), ua=bool(), useTemplate=str(), ut=str(), version=str(), ver=str(),
                        visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                        **kwargs):
    pass


def iconTextRadioCollection(collectionItemArray=bool(), cia=bool(), defineTemplate=str(), dt=str(),
                            disableCommands=bool(), dcm=bool(), exists=bool(), ex=bool(), gl=bool(),
                            numberOfCollectionItems=bool(), nci=bool(), parent=str(), p=str(), select=str(), sl=str(),
                            useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def iconTextScrollList(allowMultiSelection=bool(), ams=bool(), annotation=str(), ann=str(), append=str(), a=str(),
                       backgroundColor=list, bgc=list, changeCommand=str(), cc=str(), defineTemplate=str(), dt=str(),
                       deselectAll=bool(), da=bool(), docTag=str(), dtg=str(), doubleClickCommand=str(), dcc=str(),
                       dragCallback=str(), dgc=str(), dragFeedbackVisible=bool(), dfv=bool(), dropCallback=str(),
                       dpc=str(), dropRectCallback=str(), drc=str(), editIndexed=int(), ei=int(), editable=bool(),
                       ed=bool(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                       enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(),
                       fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(),
                       itemAt=list, ia=list, itemTextColor=list, itc=list, manage=bool(), m=bool(), noBackground=bool(),
                       nbg=bool(), numberOfIcons=int(), nic=int(), numberOfPopupMenus=bool(), npm=bool(),
                       numberOfRows=bool(), nr=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                       preventOverride=bool(), po=bool(), removeAll=bool(), ra=bool(), selectCommand=str(), sc=str(),
                       selectIndexedItem=int(), sii=int(), selectItem=str(), si=str(), statusBarMessage=str(),
                       sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(),
                       vcc=str(), visualRectAt=list, vra=list, width=int(), w=int(), *args, **kwargs):
    pass


def iconTextStaticLabel(align=str(), al=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                        defineTemplate=str(), dt=str(), disabledImage=str(), di=str(), docTag=str(), dtg=str(),
                        dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                        enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                        ex=bool(), flipX=bool(), fx=bool(), flipY=bool(), fy=bool(), font=str(), fn=str(),
                        fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                        image=str(), i=str(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                        imageOverlayLabel=str(), iol=str(), isObscured=bool(), io=bool(), label=str(), l=str(),
                        labelOffset=int(), lo=int(), ltVersion=str(), lt=str(), manage=bool(), m=bool(),
                        marginHeight=int(), mh=int(), marginWidth=int(), mw=int(), noBackground=bool(), nbg=bool(),
                        numberOfPopupMenus=bool(), npm=bool(), overlayLabelBackColor=list, olb=list,
                        overlayLabelColor=list, olc=list, parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                        preventOverride=bool(), po=bool(), rotation=float(), rot=float(), statusBarMessage=str(),
                        sbm=str(), style=str(), st=str(), useAlpha=bool(), ua=bool(), useTemplate=str(), ut=str(),
                        version=str(), ver=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                        width=int(), w=int(), *args, **kwargs):
    pass


def ikfkDisplayMethod(display=str(), d=str(), *args, **kwargs):
    pass


def ikHandle(autoPriority=bool(), ap=bool(), connectEffector=bool(), ce=bool(), createCurve=bool(), ccv=bool(),
             createRootAxis=bool(), cra=bool(), curve=str(), c=str(), disableHandles=bool(), dh=bool(),
             enableHandles=bool(), eh=bool(), endEffector=str(), ee=str(), exists=str(), ex=str(), forceSolver=bool(),
             fs=bool(), freezeJoints=bool(), fj=bool(), jointList=bool(), jl=bool(), name=str(), n=str(),
             numSpans=int(), ns=int(), parentCurve=bool(), pcv=bool(), positionWeight=float(), pw=float(),
             priority=int(), p=int(), rootOnCurve=bool(), roc=bool(), rootTwistMode=bool(), rtm=bool(),
             setupForRPsolver=bool(), srp=bool(), simplifyCurve=bool(), scv=bool(), snapCurve=bool(), snc=bool(),
             snapHandleFlagToggle=bool(), shf=bool(), snapHandleToEffector=bool(), see=bool(), solver=str(), sol=str(),
             startJoint=str(), sj=str(), sticky=str(), s=str(), twistType=str(), tws=str(), weight=float(), w=float(),
             *args, **kwargs):
    pass


def ikHandleCtx(autoPriorityH=bool(), apH=bool(), createCurve=bool(), ccv=bool(), createRootAxis=bool(), cra=bool(),
                exists=bool(), ex=bool(), forceSolverH=bool(), fsH=bool(), history=bool(), ch=bool(), image1=str(),
                i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), numSpans=int(), ns=int(),
                parentCurve=bool(), pcv=bool(), poWeightH=float(), pwH=float(), priorityH=int(), pH=int(),
                rootOnCurve=bool(), roc=bool(), rootTwistMode=bool(), rtm=bool(), simplifyCurve=bool(), scv=bool(),
                snapCurve=bool(), snc=bool(), snapHandleH=bool(), snH=bool(), solverTypeH=str(), stH=str(),
                stickyH=str(), sH=str(), twistType=str(), tws=str(), weightH=float(), wH=float(), *args, **kwargs):
    pass


def ikHandleDisplayScale(*args, **kwargs):
    pass


def ikSolver(epsilon=float(), ep=float(), maxIterations=int(), mxi=int(), name=str(), n=str(), solverType=str(),
             st=str(), *args, **kwargs):
    pass


def ikSplineHandleCtx(autoPriorityH=bool(), apH=bool(), createCurve=bool(), ccv=bool(), createRootAxis=bool(),
                      cra=bool(), exists=bool(), ex=bool(), forceSolverH=bool(), fsH=bool(), history=bool(), ch=bool(),
                      image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(),
                      numSpans=int(), ns=int(), parentCurve=bool(), pcv=bool(), poWeightH=float(), pwH=float(),
                      priorityH=int(), pH=int(), rootOnCurve=bool(), roc=bool(), rootTwistMode=bool(), rtm=bool(),
                      simplifyCurve=bool(), scv=bool(), snapCurve=bool(), snc=bool(), snapHandleH=bool(), snH=bool(),
                      solverTypeH=str(), stH=str(), stickyH=str(), sH=str(), twistType=str(), tws=str(),
                      weightH=float(), wH=float(), *args, **kwargs):
    pass


def ikSystem(allowRotation=bool(), ar=bool(), autoPriority=bool(), ap=bool(), autoPriorityMC=bool(), apm=bool(),
             autoPrioritySC=bool(), aps=bool(), list=list, ls=list, snap=bool(), sn=bool(), solve=bool(), sol=bool(),
             solverTypes=bool(), st=bool(), *args, **kwargs):
    pass


def ikSystemInfo(globalSnapHandle=bool(), gsh=bool(), *args, **kwargs):
    pass


def illustratorCurves(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), illustratorFilename=str(),
                      ifn=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), tolerance=float(), tl=float(),
                      *args, **kwargs):
    pass


def image(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(), docTag=str(),
          dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
          enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
          fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, image=str(), i=str(),
          isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
          numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
          preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
          visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def imagePlane(camera=str(), c=str(), counter=bool(), cn=bool(), detach=bool(), d=bool(), dropFrame=bool(), df=bool(),
               fileName=str(), fn=str(), frameDuration=int(), fd=int(), height=float(), h=float(), imageSize=list,
               iz=list, lookThrough=str(), lt=str(), maintainRatio=bool(), mr=bool(), name=str(), n=str(),
               negTimesOK=bool(), nt=bool(), numFrames=int(), nf=int(), quickTime=bool(), qt=bool(),
               showInAllViews=bool(), sia=bool(), timeCode=int(), tc=int(), timeCodeTrack=bool(), tt=bool(),
               timeScale=int(), ts=int(), twentyFourHourMax=bool(), tf=bool(), width=float(), w=float(), *args,
               **kwargs):
    pass


def imfPlugins(extension=str(), ext=str(), keyword=str(), key=str(), multiFrameSupport=str(), mfs=str(),
               pluginName=str(), pn=str(), readSupport=str(), rs=str(), writeSupport=str(), ws=str(), *args, **kwargs):
    pass


def inheritTransform(off=bool(), on=bool(), preserve=bool(), p=bool(), toggle=bool(), tgl=bool(), *args, **kwargs):
    pass


def insertJoint(*args, **kwargs):
    pass


def insertJointCtx(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                   *args, **kwargs):
    pass


def insertKeyCtx(breakdown=bool(), bd=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
                 i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), preserveTangent=bool(),
                 pt=bool(), *args, **kwargs):
    pass


def insertKnotCurve(addKnots=bool(), add=bool(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                    curveOnSurface=bool(), cos=bool(), insertBetween=bool(), ib=bool(), name=str(), n=str(),
                    nodeState=int(), nds=int(), numberOfKnots=int(), nk=int(), object=bool(), o=bool(),
                    parameter=float(), p=float(), replaceOriginal=bool(), rpo=bool(), *args, **kwargs):
    pass


def insertKnotSurface(addKnots=bool(), add=bool(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                      direction=int(), d=int(), insertBetween=bool(), ib=bool(), name=str(), n=str(), nodeState=int(),
                      nds=int(), numberOfKnots=int(), nk=int(), object=bool(), o=bool(), parameter=float(), p=float(),
                      replaceOriginal=bool(), rpo=bool(), *args, **kwargs):
    pass


def instance(leaf=bool(), lf=bool(), name=str(), n=str(), smartTransform=bool(), st=bool(), *args, **kwargs):
    pass


def instanceable(allow=bool(), a=bool(), recursive=bool(), r=bool(), shape=bool(), s=bool(), *args, **kwargs):
    pass


def instancer(addObject=bool(), a=bool(), cycle=str(), c=str(), cycleStep=float(), cs=float(), cycleStepUnits=str(),
              csu=str(), index=int(), i=int(), levelOfDetail=str(), lod=str(), name=str(), n=str(), object=str(),
              obj=str(), objectPosition=str(), op=str(), objectRotation=str(), objectScale=str(), os=str(),
              pointDataSource=bool(), pds=bool(), removeObject=bool(), rm=bool(), rotationOrder=str(), ro=str(),
              rotationUnits=str(), ru=str(), valueName=str(), vn=str(), *args, **kwargs):
    pass


def internalVar(mayaInstallDir=bool(), mid=bool(), userAppDir=bool(), uad=bool(), userBitmapsDir=bool(), ubd=bool(),
                userHotkeyDir=bool(), uhk=bool(), userMarkingMenuDir=bool(), umm=bool(), userPrefDir=bool(), upd=bool(),
                userPresetsDir=bool(), ups=bool(), userScriptDir=bool(), usd=bool(), userShelfDir=bool(), ush=bool(),
                userTmpDir=bool(), utd=bool(), userWorkspaceDir=bool(), uwd=bool(), *args, **kwargs):
    pass


def intersect(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), curveOnSurface=bool(), cos=bool(),
              firstSurface=bool(), fs=bool(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(),
              tolerance=float(), tol=float(), *args, **kwargs):
    pass


def intField(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(),
             defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dragCommand=str(),
             dc=str(), dropCallback=str(), dpc=str(), editable=bool(), ed=bool(), enable=bool(), en=bool(),
             enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), enterCommand=str(), ec=str(),
             exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list,
             hlc=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(), maxValue=int(), max=int(), minValue=int(),
             min=int(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
             popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), receiveFocusCommand=str(), rfc=str(),
             statusBarMessage=str(), sbm=str(), step=int(), s=int(), useTemplate=str(), ut=str(), value=int(), v=int(),
             visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def intFieldGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                changeCommand=str(), cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list,
                columnAlign3=list, cl3=list, columnAlign4=list, cl4=list, columnAlign5=list, cl5=list,
                columnAlign6=list, cl6=list, columnAttach=list, cat=list, columnAttach2=list, ct2=list,
                columnAttach3=list, ct3=list, columnAttach4=list, ct4=list, columnAttach5=list, ct5=list,
                columnAttach6=list, ct6=list, columnOffset2=list, co2=list, columnOffset3=list, co3=list,
                columnOffset4=list, co4=list, columnOffset5=list, co5=list, columnOffset6=list, co6=list,
                columnWidth=list, cw=list, columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list,
                columnWidth3=list, cw3=list, columnWidth4=list, cw4=list, columnWidth5=list, cw5=list,
                columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                dragCallback=str(), dgc=str(), dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(),
                enable=bool(), en=bool(), enable1=bool(), en1=bool(), enable2=bool(), en2=bool(), enable3=bool(),
                en3=bool(), enable4=bool(), en4=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                ekf=bool(), exists=bool(), ex=bool(), extraLabel=str(), el=str(), fullPathName=bool(), fpn=bool(),
                height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(), label=str(),
                l=str(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), numberOfFields=int(), nf=int(),
                numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                preventOverride=bool(), po=bool(), rowAttach=list, rat=list, statusBarMessage=str(), sbm=str(),
                useTemplate=str(), ut=str(), value=list, v=list, value1=int(), v1=int(), value2=int(), v2=int(),
                value3=int(), v3=int(), value4=int(), v4=int(), visible=bool(), vis=bool(), visibleChangeCommand=str(),
                vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def intScrollBar(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(),
                 defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                 dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                 enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
                 fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                 horizontal=bool(), hr=bool(), isObscured=bool(), io=bool(), largeStep=int(), ls=int(), manage=bool(),
                 m=bool(), maxValue=int(), max=int(), minValue=int(), min=int(), noBackground=bool(), nbg=bool(),
                 numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                 preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(), step=int(), s=int(),
                 useTemplate=str(), ut=str(), value=int(), v=int(), visible=bool(), vis=bool(),
                 visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def intSlider(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(),
              defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dragCommand=str(),
              dc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
              enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(),
              height=int(), h=int(), highlightColor=list, hlc=list, horizontal=bool(), hr=bool(), isObscured=bool(),
              io=bool(), manage=bool(), m=bool(), maxValue=int(), max=int(), minValue=int(), min=int(),
              noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
              popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(),
              step=int(), s=int(), useTemplate=str(), ut=str(), value=int(), v=int(), visible=bool(), vis=bool(),
              visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def intSliderGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                 ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                 adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                 changeCommand=str(), cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list,
                 columnAlign3=list, cl3=list, columnAlign4=list, cl4=list, columnAlign5=list, cl5=list,
                 columnAlign6=list, cl6=list, columnAttach=list, cat=list, columnAttach2=list, ct2=list,
                 columnAttach3=list, ct3=list, columnAttach4=list, ct4=list, columnAttach5=list, ct5=list,
                 columnAttach6=list, ct6=list, columnOffset2=list, co2=list, columnOffset3=list, co3=list,
                 columnOffset4=list, co4=list, columnOffset5=list, co5=list, columnOffset6=list, co6=list,
                 columnWidth=list, cw=list, columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list,
                 columnWidth3=list, cw3=list, columnWidth4=list, cw4=list, columnWidth5=list, cw5=list,
                 columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                 dragCallback=str(), dgc=str(), dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(),
                 enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(),
                 exists=bool(), ex=bool(), extraLabel=str(), el=str(), field=bool(), f=bool(), fieldMaxValue=int(),
                 fmx=int(), fieldMinValue=int(), fmn=int(), fieldStep=int(), fs=int(), fullPathName=bool(), fpn=bool(),
                 height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(), label=str(),
                 l=str(), manage=bool(), m=bool(), maxValue=int(), max=int(), minValue=int(), min=int(),
                 noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                 popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rowAttach=list, rat=list,
                 sliderStep=int(), ss=int(), statusBarMessage=str(), sbm=str(), step=int(), s=int(), useTemplate=str(),
                 ut=str(), value=int(), v=int(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                 width=int(), w=int(), *args, **kwargs):
    pass


def inViewEditor(visible=bool(), v=bool(), *args, **kwargs):
    pass


def inViewMessage(alpha=float(), a=float(), assistMessage=str(), amg=str(), backColor=int(), bkc=int(), clear=str(),
                  cl=str(), clickKill=bool(), ck=bool(), dragKill=bool(), dk=bool(), fade=bool(), f=bool(),
                  fadeInTime=int(), fit=int(), fadeOutTime=int(), fot=int(), fadeStayTime=int(), fst=int(), font=str(),
                  ft=str(), fontSize=int(), fts=int(), frameOffset=int(), fof=int(), hide=bool(), hd=bool(),
                  message=str(), msg=str(), minimize=bool(), min=bool(), position=str(), pos=str(), restore=bool(),
                  res=bool(), show=bool(), sh=bool(), statusMessage=str(), smg=str(), textAlpha=float(), ta=float(),
                  textOffset=int(), tof=int(), uvEditor=bool(), uv=bool(), *args, **kwargs):
    pass


def iprEngine(copy=str(), cp=str(), defineTemplate=str(), dt=str(), diagnostics=bool(), dig=bool(),
              estimatedMemory=bool(), mem=bool(), exists=bool(), ex=bool(), iprImage=str(), ipr=str(),
              motionVectorFile=bool(), mvf=bool(), object=str(), obj=str(), region=list, r=list, relatedFiles=bool(),
              rel=bool(), releaseIprImage=bool(), rii=bool(), resolution=bool(), res=bool(), scanlineIncrement=str(),
              sli=str(), showProgressBar=bool(), spb=bool(), startTuning=bool(), st=bool(), stopTuning=bool(),
              spt=bool(), underPixel=list, un=list, update=bool(), u=bool(), updateDepthOfField=bool(), udf=bool(),
              updateLightGlow=bool(), ulg=bool(), updateMotionBlur=bool(), umb=bool(), updatePort=str(), up=str(),
              updateShaderGlow=bool(), usg=bool(), updateShading=bool(), us=bool(), updateShadowMaps=bool(), usm=bool(),
              useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def isConnected(ignoreUnitConversion=bool(), iuc=bool(), *args, **kwargs):
    pass


def isDirty(connection=bool(), c=bool(), datablock=bool(), d=bool(), *args, **kwargs):
    pass


def isolateSelect(addDagObject=str(), ado=str(), addSelected=bool(), addSelectedObjects=bool(), aso=bool(),
                  loadSelected=bool(), ls=bool(), removeDagObject=str(), rdo=str(), removeSelected=bool(), rs=bool(),
                  state=bool(), s=bool(), update=bool(), u=bool(), viewObjects=bool(), vo=bool(), *args, **kwargs):
    pass


def isTrue(*args, **kwargs):
    pass


def itemFilter(byBin=str(), bk=str(), byName=str(), bn=str(), byScript=str(), bs=str(), byType=str(), bt=str(),
               category=str(), cat=str(), classification=str(), cls=str(), clearByBin=bool(), cbk=bool(),
               clearByType=bool(), cbt=bool(), difference=list, di=list, exists=bool(), ex=bool(), intersect=list,
               listBuiltInFilters=bool(), lbf=bool(), listOtherFilters=bool(), lof=bool(), listUserFilters=bool(),
               luf=bool(), negate=bool(), neg=bool(), parent=str(), p=str(), pythonModule=str(), pym=str(),
               secondScript=str(), ss=str(), text=str(), t=str(), union=list, un=list, uniqueNodeNames=bool(),
               unn=bool(), *args, **kwargs):
    pass


def itemFilterAttr(byName=str(), bn=str(), byNameString=str(), bns=str(), byScript=str(), bs=str(),
                   classification=str(), cls=str(), dynamic=bool(), dy=bool(), exists=bool(), ex=bool(),
                   hasCurve=bool(), hc=bool(), hasDrivenKey=bool(), hdk=bool(), hasExpression=bool(), he=bool(),
                   hidden=bool(), h=bool(), intersect=list, keyable=bool(), k=bool(), listBuiltInFilters=bool(),
                   lbf=bool(), listOtherFilters=bool(), lof=bool(), listUserFilters=bool(), luf=bool(), negate=bool(),
                   neg=bool(), parent=str(), p=str(), published=bool(), pub=bool(), readable=bool(), r=bool(),
                   scaleRotateTranslate=bool(), srt=bool(), secondScript=str(), ss=str(), text=str(), t=str(),
                   union=list, un=list, writable=bool(), w=bool(), *args, **kwargs):
    pass


def itemFilterType(text=str(), t=str(), type=bool(), typ=bool(), *args, **kwargs):
    pass


def joint(absolute=bool(), a=bool(), angleX=float(), ax=float(), angleY=float(), ay=float(), angleZ=float(), az=float(),
          assumePreferredAngles=bool(), apa=bool(), automaticLimits=bool(), al=bool(), children=bool(), ch=bool(),
          component=bool(), co=bool(), degreeOfFreedom=str(), dof=str(), exists=str(), ex=str(), limitSwitchX=bool(),
          lsx=bool(), limitSwitchY=bool(), lsy=bool(), limitSwitchZ=bool(), lsz=bool(), limitX=list, lx=list,
          limitY=list, ly=list, limitZ=list, lz=list, name=str(), n=str(), orientJoint=str(), oj=str(),
          orientation=list, o=list, position=list, p=list, radius=float(), rad=float(), relative=bool(), r=bool(),
          rotationOrder=str(), roo=str(), scale=list, s=list, scaleCompensate=bool(), sc=bool(), scaleOrientation=list,
          so=list, secondaryAxisOrient=str(), sao=str(), setPreferredAngles=bool(), spa=bool(), stiffnessX=float(),
          stx=float(), stiffnessY=float(), sty=float(), stiffnessZ=float(), stz=float(), symmetry=bool(), sym=bool(),
          symmetryAxis=str(), sa=str(), zeroScaleOrient=bool(), zso=bool(), *args, **kwargs):
    return createNode('joint', name=name)


def jointCluster(aboveBound=float(), ab=float(), aboveCluster=bool(), ac=bool(), aboveDropoffType=str(), adt=str(),
                 aboveValue=float(), av=float(), belowBound=float(), bb=float(), belowCluster=bool(), bc=bool(),
                 belowDropoffType=str(), bdt=str(), belowValue=float(), bv=float(), deformerTools=bool(), dt=bool(),
                 joint=str(), j=str(), name=str(), n=str(), *args, **kwargs):
    pass


def jointCtx(autoJointOrient=str(), ajo=str(), autoPriorityH=bool(), apH=bool(), createIKHandle=bool(), ikh=bool(),
             degreeOfFreedomJ=str(), dJ=str(), exists=bool(), ex=bool(), forceSolverH=bool(), fsH=bool(), image1=str(),
             i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), jointAutoLimits=bool(), jal=bool(),
             jointOrientationJ=list, joJ=list, largeBoneLength=float(), lbl=float(), largeBoneRadius=float(),
             lbr=float(), poWeightH=float(), pwH=float(), priorityH=int(), pH=int(), scaleCompensateJ=bool(),
             scJ=bool(), scaleJ=list, sJ=list, scaleOrientationJ=list, soJ=list, secondaryAxisOrient=str(), sao=str(),
             smallBoneLength=float(), sbl=float(), smallBoneRadius=float(), sbr=float(), snapHandleH=bool(), snH=bool(),
             solverTypeH=str(), stH=str(), stickyH=str(), sH=str(), symmetry=bool(), sym=bool(), symmetryAxis=str(),
             sa=str(), variableBoneSize=bool(), vbs=bool(), weightH=float(), wH=float(), *args, **kwargs):
    pass


def jointDisplayScale(absolute=bool(), a=bool(), ikfk=float(), ik=float(), *args, **kwargs):
    pass


def jointLattice(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(), creasing=float(),
                 cr=float(), deformerTools=bool(), dt=bool(), exclusive=str(), ex=str(), frontOfChain=bool(),
                 foc=bool(), geometry=str(), g=str(), geometryIndices=bool(), gi=bool(), ignoreSelected=bool(),
                 includeHiddenSelections=bool(), ihs=bool(), joint=str(), j=str(), lengthIn=float(), li=float(),
                 lengthOut=float(), lo=float(), lowerBindSkin=str(), lb=str(), lowerTransform=str(), lt=str(),
                 name=str(), n=str(), parallel=bool(), par=bool(), prune=bool(), pr=bool(), remove=bool(), rm=bool(),
                 rounding=float(), ro=float(), split=bool(), sp=bool(), upperBindSkin=str(), ub=str(),
                 upperTransform=str(), ut=str(), useComponentTags=bool(), uct=bool(), widthLeft=float(), wl=float(),
                 widthRight=float(), wr=float(), *args, **kwargs):
    pass


def keyframe(absolute=bool(), a=bool(), adjustBreakdown=bool(), abd=bool(), animation=str(), an=str(), attribute=str(),
             at=str(), breakdown=bool(), bd=bool(), clipTime=list, ct=list, controlPoints=bool(), cp=bool(),
             eval=bool(), ev=bool(), float=tuple(), f=tuple(), floatChange=float(), fc=float(), hierarchy=str(),
             hi=str(), includeUpperBound=bool(), iub=bool(), index=int(), indexValue=bool(), iv=bool(),
             keyframeCount=bool(), kc=bool(), lastSelected=bool(), lsl=bool(), name=bool(), n=bool(), option=str(),
             o=str(), relative=bool(), r=bool(), selected=bool(), sl=bool(), shape=bool(), s=bool(),
             tickDrawSpecial=bool(), tds=bool(), time=tuple(), t=tuple(), timeChange=float(), tc=float(),
             valueChange=float(), vc=float(), *args, **kwargs):
    pass


def keyframeOutliner(animCurve=str(), ac=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                     defineTemplate=str(), dt=str(), display=str(), dsp=str(), docTag=str(), dtg=str(),
                     dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                     enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                     ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                     isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                     numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                     preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
                     visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                     **kwargs):
    pass


def keyframeRegionCurrentTimeCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(),
                                 image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def keyframeRegionDirectKeyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(),
                               image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), option=str(),
                               o=str(), *args, **kwargs):
    pass


def keyframeRegionDollyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                           i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def keyframeRegionInsertKeyCtx(breakdown=bool(), bd=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(),
                               image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(),
                               n=str(), *args, **kwargs):
    pass


def keyframeRegionMoveKeyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                             i2=str(), image3=str(), i3=str(), name=str(), n=str(), option=str(), o=str(), *args,
                             **kwargs):
    pass


def keyframeRegionScaleKeyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                              i2=str(), image3=str(), i3=str(), name=str(), n=str(), scaleSpecifiedKeys=bool(),
                              ssk=bool(), type=str(), typ=str(), *args, **kwargs):
    pass


def keyframeRegionSelectKeyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(),
                               image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def keyframeRegionSetKeyCtx(breakdown=bool(), bd=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(),
                            image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(),
                            *args, **kwargs):
    pass


def keyframeRegionTrackCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                           i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def keyframeStats(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                  ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                  adjustableColumn6=int(), ad6=int(), animEditor=str(), ae=str(), annotation=str(), ann=str(),
                  backgroundColor=list, bgc=list, classicMode=bool(), cm=bool(), columnAlign=list, cal=list,
                  columnAlign2=list, cl2=list, columnAlign3=list, cl3=list, columnAlign4=list, cl4=list,
                  columnAlign5=list, cl5=list, columnAlign6=list, cl6=list, columnAttach=list, cat=list,
                  columnAttach2=list, ct2=list, columnAttach3=list, ct3=list, columnAttach4=list, ct4=list,
                  columnAttach5=list, ct5=list, columnAttach6=list, ct6=list, columnOffset2=list, co2=list,
                  columnOffset3=list, co3=list, columnOffset4=list, co4=list, columnOffset5=list, co5=list,
                  columnOffset6=list, co6=list, columnWidth=list, cw=list, columnWidth1=int(), cw1=int(),
                  columnWidth2=list, cw2=list, columnWidth3=list, cw3=list, columnWidth4=list, cw4=list,
                  columnWidth5=list, cw5=list, columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(),
                  docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
                  en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                  ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                  isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                  numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                  precision=int(), pre=int(), preventOverride=bool(), po=bool(), rowAttach=list, rat=list,
                  statusBarMessage=str(), sbm=str(), timeAnnotation=str(), tan=str(), useTemplate=str(), ut=str(),
                  valueAnnotation=str(), van=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                  width=int(), w=int(), *args, **kwargs):
    pass


def keyingGroup(activator=str(), act=str(), addElement=str(), add=str(), afterFilters=bool(), af=bool(),
                anyMember=str(), am=str(), category=str(), cat=str(), clear=str(), cl=str(), color=int(), co=int(),
                copy=str(), cp=str(), edges=bool(), eg=bool(), editPoints=bool(), ep=bool(), empty=bool(), em=bool(),
                excludeDynamic=bool(), ed=bool(), excludeRotate=bool(), er=bool(), excludeScale=bool(), es=bool(),
                excludeTranslate=bool(), et=bool(), excludeVisibility=bool(), ev=bool(), facets=bool(), fc=bool(),
                flatten=str(), fl=str(), forceElement=str(), fe=str(), include=str(), intersection=str(), int=str(),
                isIntersecting=str(), ii=str(), isMember=str(), im=str(), layer=bool(), l=bool(),
                minimizeRotation=bool(), mr=bool(), name=str(), n=str(), noIntermediate=bool(), ni=bool(),
                noSurfaceShader=bool(), nss=bool(), noWarnings=bool(), nw=bool(), nodesOnly=bool(), no=bool(),
                remove=str(), rm=str(), removeActivator=str(), rac=str(), renderable=bool(), r=bool(),
                setActiveFilter=str(), fil=str(), size=bool(), s=bool(), split=str(), sp=str(), subtract=str(),
                sub=str(), text=str(), t=str(), union=str(), un=str(), vertices=bool(), v=bool(), *args, **kwargs):
    pass


def keyTangent(absolute=bool(), a=bool(), animation=str(), an=str(), attribute=str(), at=str(), controlPoints=bool(),
               cp=bool(), float=tuple(), f=tuple(), g=bool(), hierarchy=str(), hi=str(), inAngle=float(), ia=float(),
               inTangentType=str(), itt=str(), inWeight=float(), iw=float(), includeUpperBound=bool(), iub=bool(),
               index=int(), ix=float(), iy=float(), lock=bool(), l=bool(), outAngle=float(), oa=float(),
               outTangentType=str(), ott=str(), outWeight=float(), ow=float(), ox=float(), oy=float(),
               pluginTangentTypes=str(), ptt=str(), relative=bool(), r=bool(), shape=bool(), s=bool(),
               stepAttributes=bool(), sa=bool(), time=tuple(), t=tuple(), unify=bool(), uni=bool(), weightLock=bool(),
               wl=bool(), weightedTangents=bool(), wt=bool(), *args, **kwargs):
    pass


def lassoContext(drawClosed=bool(), dc=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
                 i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def lattice(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(), commonParent=bool(),
            cp=bool(), deformerTools=bool(), dt=bool(), divisions=list, dv=list, dualBase=bool(), db=bool(),
            exclusive=str(), ex=str(), freezeMapping=bool(), fm=bool(), frontOfChain=bool(), foc=bool(), geometry=str(),
            g=str(), geometryIndices=bool(), gi=bool(), ignoreSelected=bool(), includeHiddenSelections=bool(),
            ihs=bool(), latticeReset=bool(), lr=bool(), ldivisions=list, ldv=list, name=str(), n=str(),
            objectCentered=bool(), oc=bool(), outsideFalloffDistance=float(), ofd=float(), outsideLattice=int(),
            ol=int(), parallel=bool(), par=bool(), position=list, pos=list, prune=bool(), pr=bool(), remove=bool(),
            rm=bool(), removeTweaks=bool(), rt=bool(), rotation=list, ro=list, scale=list, s=list, split=bool(),
            sp=bool(), useComponentTags=bool(), uct=bool(), *args, **kwargs):
    pass


def latticeDeformKeyCtx(envelope=float(), ev=float(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
                        i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), latticeColumns=int(), lc=int(),
                        latticeRows=int(), lr=int(), name=str(), n=str(), scaleLatticePts=bool(), slp=bool(), *args,
                        **kwargs):
    pass


def launch(directory=str(), dir=str(), movie=str(), mov=str(), pdfFile=str(), pdf=str(), webPage=str(), web=str(),
           *args, **kwargs):
    pass


def launchImageEditor(editImageFile=str(), eif=str(), viewImageFile=str(), vif=str(), *args, **kwargs):
    pass


def layerButton(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(), color=list,
                cl=list, command=str(), c=str(), current=bool(), cr=bool(), defineTemplate=str(), dt=str(),
                docTag=str(), dtg=str(), doubleClickCommand=str(), dcc=str(), dragCallback=str(), dgc=str(),
                dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(),
                height=int(), h=int(), hideOnPlaybackCommand=str(), hpc=str(), highlightColor=list, hlc=list,
                identification=int(), id=int(), isObscured=bool(), io=bool(), label=str(), l=str(), labelWidth=bool(),
                lw=bool(), layerHideOnPlayback=bool(), hp=bool(), layerState=str(), ls=str(), layerVisible=bool(),
                lv=bool(), manage=bool(), m=bool(), name=str(), n=str(), noBackground=bool(), nbg=bool(),
                numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                preventOverride=bool(), po=bool(), renameCommand=str(), rc=str(), select=bool(), s=bool(),
                statusBarMessage=str(), sbm=str(), transparent=bool(), t=bool(), typeCommand=str(), tc=str(),
                useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                visibleCommand=str(), vc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def layeredShaderPort(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(),
                      docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
                      enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                      ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                      highlightColor=list, hlc=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(),
                      noBackground=bool(), nbg=bool(), node=str(), n=str(), numberOfPopupMenus=bool(), npm=bool(),
                      parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
                      selectedColorControl=str(), scc=str(), selectedTransparencyControl=str(), stc=str(),
                      statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                      visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def layeredTexturePort(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(),
                       docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
                       enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                       ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                       highlightColor=list, hlc=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(),
                       noBackground=bool(), nbg=bool(), node=str(), n=str(), numberOfPopupMenus=bool(), npm=bool(),
                       parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
                       selectedAlphaControl=str(), sac=str(), selectedBlendModeControl=str(), sbc=str(),
                       selectedColorControl=str(), scc=str(), selectedIsVisibleControl=str(), svc=str(),
                       statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                       visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def layout(annotation=str(), ann=str(), backgroundColor=list, bgc=list, childArray=bool(), ca=bool(),
           defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(),
           dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
           ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
           highlightColor=list, hlc=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(),
           nbg=bool(), numberOfChildren=bool(), nch=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(),
           p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), statusBarMessage=str(),
           sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
           width=int(), w=int(), *args, **kwargs):
    pass


def layoutDialog(backgroundColor=list, bgc=list, dismiss=str(), dis=str(), parent=str(), p=str(), title=str(), t=str(),
                 uiScript=str(), ui=str(), *args, **kwargs):
    pass


def license(borrow=bool(), b=bool(), info=bool(), i=bool(), isBorrowed=bool(), ib=bool(), isExported=bool(), ie=bool(),
            isTrial=bool(), it=bool(), licenseMethod=bool(), lm=bool(), productChoice=bool(), pc=bool(), r=bool(),
            showBorrowInfo=bool(), sbi=bool(), showProductInfoDialog=bool(), spi=bool(), status=bool(), s=bool(),
            usage=bool(), u=bool(), *args, **kwargs):
    pass


def lightlink(b=bool(), hierarchy=bool(), h=bool(), light=str(), l=str(), make=bool(), m=bool(), object=str(), o=str(),
              sets=bool(), set=bool(), shadow=bool(), shd=bool(), shapes=bool(), shp=bool(), transforms=bool(),
              t=bool(), useActiveLights=bool(), ual=bool(), useActiveObjects=bool(), uao=bool(), *args, **kwargs):
    pass


def lightList(add=str(), remove=str(), rm=str(), *args, **kwargs):
    pass


def linearPrecision(*args, **kwargs):
    pass


def listAnimatable(active=bool(), act=bool(), manip=bool(), m=bool(), manipHandle=bool(), mh=bool(), shape=bool(),
                   s=bool(), type=bool(), typ=bool(), *args, **kwargs):
    pass


def listAttr(array=bool(), a=bool(), caching=bool(), ca=bool(), category=str(), ct=str(), changedSinceFileOpen=bool(),
             cfo=bool(), channelBox=bool(), cb=bool(), connectable=bool(), c=bool(), extension=bool(), ex=bool(),
             fromPlugin=bool(), fp=bool(), hasData=bool(), hd=bool(), hasNullData=bool(), hnd=bool(), inUse=bool(),
             iu=bool(), keyable=bool(), k=bool(), leaf=bool(), lf=bool(), locked=bool(), l=bool(), multi=bool(),
             m=bool(), output=bool(), o=bool(), ramp=bool(), ra=bool(), read=bool(), r=bool(), readOnly=bool(),
             ro=bool(), scalar=bool(), s=bool(), scalarAndArray=bool(), sa=bool(), settable=bool(), se=bool(),
             shortNames=bool(), sn=bool(), string=str(), st=str(), unlocked=bool(), u=bool(), usedAsFilename=bool(),
             uf=bool(), userDefined=bool(), ud=bool(), visible=bool(), v=bool(), write=bool(), w=bool(), *args,
             **kwargs):
    pass


def listAttrPatterns(patternType=bool(), pt=bool(), verbose=bool(), v=bool(), *args, **kwargs):
    pass


def listCameras(orthographic=bool(), o=bool(), perspective=bool(), p=bool(), *args, **kwargs):
    pass


def listConnections(connections=bool(), c=bool(), destination=bool(), d=bool(), exactType=bool(), et=bool(),
                    plugs=bool(), p=bool(), shapes=bool(), sh=bool(), skipConversionNodes=bool(), scn=bool(),
                    source=bool(), s=bool(), type=str(), t=str(), *args, **kwargs):
    pass


def listDeviceAttachments(attribute=str(), at=str(), axis=str(), ax=str(), clutch=str(), c=str(), device=str(), d=str(),
                          file=str(), f=str(), selection=bool(), sl=bool(), write=bool(), w=bool(), *args, **kwargs):
    pass


def listHistory(allConnections=bool(), ac=bool(), allFuture=bool(), af=bool(), allGraphs=bool(), ag=bool(),
                breadthFirst=bool(), bf=bool(), fastIteration=bool(), fi=bool(), future=bool(), f=bool(),
                futureLocalAttr=bool(), fl=bool(), futureWorldAttr=bool(), fw=bool(), groupLevels=bool(), gl=bool(),
                historyAttr=bool(), ha=bool(), interestLevel=int(), il=int(), leaf=bool(), lf=bool(), levels=int(),
                lv=int(), pruneDagObjects=bool(), pdo=bool(), *args, **kwargs):
    pass


def listInputDeviceAxes(*args, **kwargs):
    pass


def listInputDeviceButtons(*args, **kwargs):
    pass


def listInputDevices(free=bool(), f=bool(), primary=bool(), p=bool(), secondary=bool(), s=bool(), *args, **kwargs):
    pass


def listNodesWithIncorrectNames(*args, **kwargs):
    pass


def listNodeTypes(exclude=str(), ex=str(), *args, **kwargs):
    pass


def listRelatives(allDescendents=bool(), ad=bool(), allParents=bool(), ap=bool(), children=bool(), c=bool(),
                  fullPath=bool(), f=bool(), noIntermediate=bool(), ni=bool(), parent=bool(), p=bool(), path=bool(),
                  pa=bool(), shapes=bool(), s=bool(), type=str(), typ=str(), *args, **kwargs):
    pass


def listSets(allSets=bool(), extendToShape=bool(), ets=bool(), object=str(), o=str(), type=int(), t=int(), *args,
             **kwargs):
    pass


def loadFluid(currentTime=bool(), ct=bool(), frame=float(), f=float(), initialConditions=bool(), ic=bool(), *args,
              **kwargs):
    pass


def loadModule(allModules=bool(), a=bool(), load=str(), ld=str(), scan=bool(), sc=bool(), *args, **kwargs):
    pass


def loadPlugin(addCallback=str(), ac=str(), allPlugins=bool(), a=bool(), name=str(), n=str(), quiet=bool(), qt=bool(),
               removeCallback=str(), rc=str(), *args, **kwargs):
    pass


def loadPrefObjects(*args, **kwargs):
    pass


def loadUI(listTypes=bool(), lt=bool(), uiFile=str(), f=str(), uiString=str(), s=str(), verbose=bool(), v=bool(),
           workingDirectory=str(), wd=str(), *args, **kwargs):
    pass


def lockNode(ignoreComponents=bool(), ic=bool(), lock=bool(), l=bool(), lockName=bool(), ln=bool(),
             lockUnpublished=bool(), lu=bool(), *args, **kwargs):
    pass


def loft(autoReverse=bool(), ar=bool(), caching=bool(), cch=bool(), close=bool(), c=bool(), constructionHistory=bool(),
         ch=bool(), createCusp=bool(), cc=bool(), degree=int(), d=int(), name=str(), n=str(), nodeState=int(),
         nds=int(), object=bool(), o=bool(), polygon=int(), po=int(), range=bool(), rn=bool(), rebuild=bool(),
         rb=bool(), reverse=bool(), r=bool(), reverseSurfaceNormals=bool(), rsn=bool(), sectionSpans=int(), ss=int(),
         uniform=bool(), u=bool(), *args, **kwargs):
    pass


def lookThru(farClip=float(), fc=float(), nearClip=float(), nc=float(), *args, **kwargs):
    pass


def ls(*args, absoluteName=bool(), an=bool(), allPaths=bool(), ap=bool(), assemblies=bool(), cameras=bool(), ca=bool(),
       containerType=str(), ct=str(), containers=bool(), con=bool(), dagObjects=bool(), dag=bool(), defaultNodes=bool(),
       dn=bool(), dependencyNodes=bool(), dep=bool(), exactType=str(), et=str(), excludeType=str(), ext=str(),
       flatten=bool(), fl=bool(), geometry=bool(), g=bool(), ghost=bool(), gh=bool(), head=int(), hd=int(),
       hilite=bool(), hl=bool(), intermediateObjects=bool(), io=bool(), invisible=bool(), iv=bool(), leaf=bool(),
       lf=bool(), lights=bool(), lt=bool(), live=bool(), lv=bool(), lockedNodes=bool(), ln=bool(), long=bool(),
       l=bool(), materials=bool(), mat=bool(), modified=bool(), mod=bool(), noIntermediate=bool(), ni=bool(),
       nodeTypes=bool(), nt=bool(), objectsOnly=bool(), o=bool(), orderedSelection=bool(), os=bool(), partitions=bool(),
       pr=bool(), persistentNodes=bool(), pn=bool(), planes=bool(), pl=bool(), preSelectHilite=bool(), psh=bool(),
       readOnly=bool(), ro=bool(), recursive=bool(), r=bool(), referencedNodes=bool(), rn=bool(), references=bool(),
       rf=bool(), renderGlobals=bool(), rg=bool(), renderQualities=bool(), rq=bool(), renderResolutions=bool(),
       rr=bool(), renderSetups=bool(), rs=bool(), selection=bool(), sl=bool(), sets=bool(), set=bool(), shapes=bool(),
       s=bool(), shortNames=bool(), sn=bool(), showNamespace=bool(), sns=bool(), showType=bool(), st=bool(), tail=int(),
       tl=int(), templated=bool(), tm=bool(), textures=bool(), tex=bool(), transforms=bool(), tr=bool(), type=str(),
       typ=str(), ufeObjects=bool(), ufe=bool(), undeletable=bool(), ud=bool(), untemplated=bool(), ut=bool(),
       uuid=bool(), uid=bool(), visible=bool(), v=bool()):
    
    from builtins import set as _set

    def match_pattern(pattern, string):
        # Convert the pattern to a regex pattern
        regex_pattern = pattern.replace('?', '.').replace('*', '.*')
        return re.match(regex_pattern, string) is not None
    def filter_nodes(pattern, nodes):
        return [node for node in nodes if match_pattern(pattern, node._name)]

    l: list[om.MObject] = []

    if selection == True or sl == True:
        selection = ACTIVE_SELECTION.as_list
        if selection:
            l = selection

    if args:
        if isinstance(args[0], str):
            filtered_pattern = filter_nodes(args[0], _hierarchy.NodePool.all_nodes())
            if selection or sl:
                l = _set(filtered_pattern).intersection_update(_set(l))
            else:
                l = filtered_pattern
    else:
        l = l or _hierarchy.NodePool.all_nodes()

    
    if transforms == True or tr == True:
        l = [node for node in l if node.hasFn(om.MFn.kTransform) and not node.hasFn(om.MFn.kShape)]
    if shapes == True or s == True:
        l = [node for node in l if node.hasFn(om.MFn.kShape)]
    if cameras == True or ca == True:
        l = [node for node in l if node.hasFn(om.MFn.kCamera)]
    if lights == True or lt == True:
        l = [node for node in l if node.hasFn(om.MFn.kLight)]
    if materials == True or mat == True:
        l = [node for node in l if node.hasFn(om.MFn.kLambert) or node.hasFn(om.MFn.kPhong)]
    if geometry == True or g == True:
        l = [node for node in l if node.hasFn(om.MFn.kMesh) or node.hasFn(om.MFn.kNurbsSurface)]
    if containers == True or con == True:
        l = [node for node in l if node.hasFn(om.MFn.kContainer)]
    if assemblies == True:
        l = [node for node in l if node.hasFn(om.MFn.kAssembly)]
    if nodeTypes == True or nt == True:
        l = [node for node in l if node.hasFn(om.MFn.kPluginDependNode)]
    if dependencyNodes == True or dep == True:
        l = [node for node in l if node.hasFn(om.MFn.kDependencyNode)]
    if dagObjects == True or dag == True:
        l = [node for node in l if node.hasFn(om.MFn.kDagNode)]
    if defaultNodes == True or dn == True:
        l = [node for node in l if node.hasFn(om.MFn.kDefaultLightList)]
    
    if type != '' or typ != '':
        typ = type or typ
        as_constant = getattr(om.MFn, f'k{typ[0].upper()}{typ[1:]}')
        l = [node for node in l if node.hasFn(as_constant)]
        if typ == 'transform':
            l = [node for node in l if not node.hasFn(om.MFn.kShape)]
    if exactType:
        typ = type or typ
        as_constant = getattr(om.MFn, f'k{typ[0].upper()}{typ[1:]}')
        l = [node for node in l if node.hasFn(as_constant) and node.apiType() == as_constant]
    if excludeType:
        typ = type or typ
        as_constant = getattr(om.MFn, f'k{typ[0].upper()}{typ[1:]}')
        l = [node for node in l if not node.hasFn(as_constant)]
    
    if long == True or l == True:
        return [om.MDagPath.getAPathTo(node).fullPathName() for node in l]
    elif shortNames == True or sn == True:
        l = [node._name for node in l]
    elif uuid == True or uid == True:
        l = [node._uuid for node in l]
    else:
        l = [node._name for node in l]

    return l

def lsThroughFilter(item=str(), it=str(), nodeArray=bool(), na=bool(), reverse=bool(), rv=bool(), selection=bool(),
                    sl=bool(), sort=str(), so=str(), *args, **kwargs):
    pass


def lsUI(cmdTemplates=bool(), ct=bool(), collection=bool(), col=bool(), contexts=bool(), ctx=bool(),
         controlLayouts=bool(), cl=bool(), controls=bool(), ctl=bool(), dumpWidgets=bool(), dw=bool(), editors=bool(),
         ed=bool(), head=int(), hd=int(), long=bool(), l=bool(), menuItems=bool(), mi=bool(), menus=bool(), m=bool(),
         numWidgets=bool(), nw=bool(), panels=bool(), p=bool(), radioMenuItemCollections=bool(), rmc=bool(), tail=int(),
         tl=int(), type=str(), typ=str(), windows=bool(), wnd=bool(), *args, **kwargs):
    pass


def makebot(checkdepends=bool(), c=bool(), checkres=int(), r=int(), input=str(), i=str(), nooverwrite=bool(),
            nov=bool(), output=str(), o=str(), verbose=bool(), v=bool(), *args, **kwargs):
    pass


def makeIdentity(apply=bool(), a=bool(), jointOrient=bool(), jo=bool(), normal=int(), n=int(), preserveNormals=bool(),
                 pn=bool(), rotate=bool(), r=bool(), scale=bool(), s=bool(), translate=bool(), t=bool(), *args,
                 **kwargs):
    pass


def makeLive(none=bool(), n=bool(), *args, **kwargs):
    pass


def makePaintable(activate=bool(), ac=bool(), activateAll=bool(), aca=bool(), altAttribute=str(), aa=str(),
                  attrType=str(), at=str(), clearAll=bool(), ca=bool(), remove=bool(), rm=bool(), shapeMode=str(),
                  sm=str(), uiName=str(), ui=str(), *args, **kwargs):
    pass


def makeSingleSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                      nodeState=int(), nds=int(), object=bool(), o=bool(), stitchTolerance=float(), st=float(), *args,
                      **kwargs):
    pass


def manipMoveContext(activeHandle=int(), ah=int(), activeHandleNormal=int(), ahn=int(), alignAlong=list, aa=list,
                     bakePivotOri=bool(), bpo=bool(), constrainAlongNormal=bool(), xn=bool(), currentActiveHandle=int(),
                     cah=int(), editPivotMode=bool(), epm=bool(), editPivotPosition=bool(), epp=bool(), exists=bool(),
                     ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                     interactiveUpdate=bool(), iu=bool(), lastMode=int(), lm=int(), manipVisible=bool(), vis=bool(),
                     mode=int(), m=int(), orientAxes=list, oa=list, orientJoint=str(), oj=str(),
                     orientJointEnabled=bool(), oje=bool(), orientObject=str(), oo=str(), orientTowards=list, ot=list,
                     pinPivot=bool(), pin=bool(), pivotOriHandle=bool(), poh=bool(), position=bool(), p=bool(),
                     postCommand=str(), psc=str(), postDragCommand=list, pod=list, preCommand=str(), prc=str(),
                     preDragCommand=list, prd=list, preserveChildPosition=bool(), pcp=bool(), preserveUV=bool(),
                     puv=bool(), reflection=bool(), rfl=bool(), reflectionAbout=int(), rab=int(), reflectionAxis=int(),
                     rfa=int(), reflectionTolerance=float(), rft=float(), secondaryAxisOrient=str(), sao=str(),
                     snap=bool(), s=bool(), snapComponentsRelative=bool(), scr=bool(), snapLiveFaceCenter=bool(),
                     slf=bool(), snapLivePoint=bool(), slp=bool(), snapPivotOri=bool(), spo=bool(), snapPivotPos=bool(),
                     spp=bool(), snapRelative=bool(), sr=bool(), snapValue=float(), sv=float(), translate=list, tr=list,
                     tweakMode=bool(), twk=bool(), xformConstraint=str(), xc=str(), *args, **kwargs):
    pass


def manipMoveLimitsCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                       i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def manipOptions(enableSmartDuplicate=bool(), esd=bool(), enableSmartExtrude=bool(), ese=bool(), forceRefresh=bool(),
                 fr=bool(), handleSize=float(), hs=float(), hideManipOnCtrl=bool(), hmc=bool(), hideManipOnShift=bool(),
                 hms=bool(), hideManipOnShiftCtrl=bool(), hsc=bool(), linePick=float(), lp=float(), lineSize=float(),
                 ls=float(), middleMouseRepositioning=bool(), mm=bool(), pivotRotateHandleOffset=int(), pro=int(),
                 planeHandleOffset=int(), pho=int(), pointSize=float(), ps=float(), preselectHighlight=bool(),
                 psh=bool(), refreshMode=int(), rm=int(), relative=bool(), r=bool(), rememberActiveHandle=bool(),
                 rah=bool(), rememberActiveHandleAfterToolSwitch=bool(), rhs=bool(), scale=float(), s=float(),
                 showExtrudeSliders=bool(), ses=bool(), showPivotRotateHandle=bool(), spr=bool(),
                 showPlaneHandles=bool(), sph=bool(), smartDuplicateType=int(), sdt=int(), *args, **kwargs):
    pass


def manipPivot(bakeOri=bool(), bo=bool(), moveToolOri=int(), mto=int(), ori=list, o=list, oriValid=bool(), ov=bool(),
               pinPivot=bool(), pin=bool(), pos=list, p=list, posValid=bool(), pv=bool(), reset=bool(), r=bool(),
               resetOri=bool(), ro=bool(), resetPos=bool(), rp=bool(), rotateToolOri=int(), rto=int(),
               scaleToolOri=int(), sto=int(), snapOri=bool(), so=bool(), snapPos=bool(), sp=bool(), valid=bool(),
               v=bool(), *args, **kwargs):
    pass


def manipRotateContext(activeHandle=int(), ah=int(), alignAlong=list, aa=list, bakePivotOri=bool(), bpo=bool(),
                       centerTrackball=bool(), ctb=bool(), constrainAlongNormal=bool(), xn=bool(),
                       currentActiveHandle=int(), cah=int(), editPivotMode=bool(), epm=bool(), editPivotPosition=bool(),
                       epp=bool(), exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                       image3=str(), i3=str(), lastMode=int(), lm=int(), manipVisible=bool(), vis=bool(), mode=int(),
                       m=int(), modifyTranslation=bool(), mt=bool(), orientAxes=list, oa=list, orientObject=str(),
                       oo=str(), orientTowards=list, ot=list, pinPivot=bool(), pin=bool(), pivotOriHandle=bool(),
                       poh=bool(), position=bool(), p=bool(), postCommand=str(), psc=str(), postDragCommand=list,
                       pod=list, preCommand=str(), prc=str(), preDragCommand=list, prd=list,
                       preserveChildPosition=bool(), pcp=bool(), preserveUV=bool(), puv=bool(), reflection=bool(),
                       rfl=bool(), reflectionAbout=int(), rab=int(), reflectionAxis=int(), rfa=int(),
                       reflectionTolerance=float(), rft=float(), rotate=list, ro=list, snap=bool(), s=bool(),
                       snapPivotOri=bool(), spo=bool(), snapPivotPos=bool(), spp=bool(), snapRelative=bool(), sr=bool(),
                       snapValue=float(), sv=float(), tweakMode=bool(), twk=bool(), useCenterPivot=bool(), ucp=bool(),
                       useManipPivot=bool(), ump=bool(), useObjectPivot=bool(), uop=bool(), xformConstraint=str(),
                       xc=str(), *args, **kwargs):
    pass


def manipRotateLimitsCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                         i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def manipScaleContext(activeHandle=int(), ah=int(), alignAlong=list, aa=list, bakePivotOri=bool(), bpo=bool(),
                      constrainAlongNormal=bool(), xn=bool(), currentActiveHandle=int(), cah=int(),
                      editPivotMode=bool(), epm=bool(), editPivotPosition=bool(), epp=bool(), exists=bool(), ex=bool(),
                      image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), lastMode=int(), lm=int(),
                      manipVisible=bool(), vis=bool(), mode=int(), m=int(), orientAxes=list, oa=list,
                      orientObject=str(), oo=str(), orientTowards=list, ot=list, pinPivot=bool(), pin=bool(),
                      pivotOriHandle=bool(), poh=bool(), position=bool(), p=bool(), postCommand=str(), psc=str(),
                      postDragCommand=list, pod=list, preCommand=str(), prc=str(), preDragCommand=list, prd=list,
                      preserveChildPosition=bool(), pcp=bool(), preserveUV=bool(), puv=bool(),
                      preventNegativeScale=bool(), pns=bool(), reflection=bool(), rfl=bool(), reflectionAbout=int(),
                      rab=int(), reflectionAxis=int(), rfa=int(), reflectionTolerance=float(), rft=float(), scale=list,
                      sc=list, snap=bool(), s=bool(), snapPivotOri=bool(), spo=bool(), snapPivotPos=bool(), spp=bool(),
                      snapRelative=bool(), sr=bool(), snapValue=float(), sv=float(), tweakMode=bool(), twk=bool(),
                      useManipPivot=bool(), ump=bool(), useObjectPivot=bool(), uop=bool(), xformConstraint=str(),
                      xc=str(), *args, **kwargs):
    pass


def manipScaleLimitsCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                        i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def marker(attach=bool(), a=bool(), detach=bool(), d=bool(), frontTwist=float(), ft=float(), orientationMarker=bool(),
           om=bool(), positionMarker=bool(), pm=bool(), sideTwist=float(), st=float(), time=float(), t=float(),
           upTwist=float(), ut=float(), valueU=float(), u=float(), *args, **kwargs):
    pass


def matchTransform(*args, pivots=bool(), piv=bool(), position=bool(), pos=bool(), positionX=bool(), px=bool(),
                   positionY=bool(), py=bool(), positionZ=bool(), pz=bool(), rotatePivot=bool(), rp=bool(),
                   rotation=bool(), rot=bool(), rotationX=bool(), rx=bool(), rotationY=bool(), ry=bool(),
                   rotationZ=bool(), rz=bool(), scale=bool(), scl=bool(), scaleBox=bool(), box=bool(),
                   scalePivot=bool(), sp=bool(), scaleX=bool(), sx=bool(), scaleY=bool(), sy=bool(), scaleZ=bool(),
                   sz=bool()):
    pass


def matrixUtil(inverse=bool(), iv=bool(), quaternion=list, qt=list, relative=bool(), rt=bool(), rotation=list, r=list,
               scale=list, s=list, shear=list, sh=list, translation=list, t=list, transpose=bool(), tp=bool(), *args,
               **kwargs):
    pass


def mayaDpiSetting(mode=int(), m=int(), realScaleValue=bool(), rsv=bool(), scaleValue=float(), sv=float(),
                   systemDpi=bool(), sd=bool(), *args, **kwargs):
    pass


def mayaHasRenderSetup(enableCurrentSession=bool(), ecs=bool(), enableDuringTests=bool(), edt=bool(), *args, **kwargs):
    pass


def melInfo(*args, **kwargs):
    pass


def melOptions(duplicateVariableWarnings=bool(), dvw=bool(), *args, **kwargs):
    pass


def memory(adjustedVirtualMemory=bool(), av=bool(), asFloat=bool(), af=bool(), debug=bool(), dbg=bool(),
           freeMemory=bool(), fr=bool(), gigaByte=bool(), gb=bool(), heapMemory=bool(), he=bool(), kiloByte=bool(),
           kb=bool(), megaByte=bool(), mb=bool(), pageFaults=bool(), pf=bool(), pageReclaims=bool(), pr=bool(),
           physicalMemory=bool(), phy=bool(), processVirtualMemory=bool(), pv=bool(), summary=bool(), sum=bool(),
           swapFree=bool(), swf=bool(), swapLogical=bool(), swl=bool(), swapMax=bool(), swm=bool(), swapPhysical=bool(),
           swp=bool(), swapReserved=bool(), swr=bool(), swapVirtual=bool(), swv=bool(), swaps=bool(), sw=bool(), *args,
           **kwargs):
    pass


def menu(allowOptionBoxes=bool(), aob=bool(), defineTemplate=str(), dt=str(), deleteAllItems=bool(), dai=bool(),
         docTag=str(), dtg=str(), enable=bool(), en=bool(), exists=bool(), ex=bool(), familyImage=str(), fi=str(),
         helpMenu=bool(), hm=bool(), itemArray=bool(), ia=bool(), label=str(), l=str(), ltVersion=str(), lt=str(),
         mnemonic=str(), mn=str(), numberOfItems=bool(), ni=bool(), parent=str(), p=str(), postMenuCommand=str(),
         pmc=str(), postMenuCommandOnce=bool(), pmo=bool(), scrollable=bool(), srb=bool(), tearOff=bool(), to=bool(),
         useTemplate=str(), ut=str(), version=str(), ver=str(), visible=bool(), vis=bool(), *args, **kwargs):
    pass


def menuBarLayout(annotation=str(), ann=str(), backgroundColor=list, bgc=list, childArray=bool(), ca=bool(),
                  defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                  dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                  enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(),
                  height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(), manage=bool(),
                  m=bool(), menuArray=bool(), ma=bool(), menuBarVisible=bool(), mbv=bool(), menuIndex=list, mi=list,
                  noBackground=bool(), nbg=bool(), numberOfChildren=bool(), nch=bool(), numberOfMenus=bool(), nm=bool(),
                  numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                  preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
                  visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                  **kwargs):
    pass


def menuEditor(annotation=str(), ann=str(), backgroundColor=list, bgc=list, cellHeight=int(), ch=int(), cellWidth=int(),
               cw=int(), cellWidthHeight=list, cwh=list, checkBoxPresent=list, cbp=list, checkBoxState=list, cbs=list,
               childArray=bool(), ca=bool(), command=list, c=list, defineTemplate=str(), dt=str(), delete=list, d=list,
               docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
               en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
               ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
               iconMenuCallback=str(), imc=str(), image=list, i=list, isObscured=bool(), io=bool(), label=list, l=list,
               manage=bool(), m=bool(), menuItemTypes=bool(), mit=bool(), noBackground=bool(), nbg=bool(),
               numberOfChildren=bool(), nch=bool(), numberOfPopupMenus=bool(), npm=bool(), optionBoxCommand=list,
               obc=list, optionBoxPresent=list, obp=list, parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
               preventOverride=bool(), po=bool(), radioButtonPresent=list, rbp=list, radioButtonState=list, rbs=list,
               separator=list, sp=list, statusBarMessage=str(), sbm=str(), style=str(), st=str(), subMenuAt=list,
               sma=list, subMenuEditorWindow=str(), sew=str(), subMenuEditorsOpen=bool(), seo=bool(), subMenuOf=list,
               smo=list, topLevelMenu=str(), tlm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
               visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def menuItem(allowOptionBoxes=bool(), aob=bool(), annotation=str(), ann=str(), boldFont=bool(), bld=bool(),
             checkBox=bool(), cb=bool(), collection=str(), cl=str(), command=str(), c=str(), data=int(), da=int(),
             defineTemplate=str(), dt=str(), divider=bool(), d=bool(), dividerLabel=str(), dl=str(), docTag=str(),
             dtg=str(), dragDoubleClickCommand=str(), ddc=str(), dragMenuCommand=str(), dmc=str(), echoCommand=bool(),
             ec=bool(), enable=bool(), en=bool(), enableCommandRepeat=bool(), ecr=bool(), exists=bool(), ex=bool(),
             familyImage=str(), fi=str(), image=str(), i=str(), imageOverlayLabel=str(), iol=str(), insertAfter=str(),
             ia=str(), isCheckBox=bool(), icb=bool(), isOptionBox=bool(), iob=bool(), isRadioButton=bool(), irb=bool(),
             italicized=bool(), itl=bool(), label=str(), l=str(), longDivider=bool(), ld=bool(), ltVersion=str(),
             lt=str(), optionBox=bool(), ob=bool(), optionBoxIcon=str(), obi=str(), parent=str(), p=str(),
             postMenuCommand=str(), pmc=str(), postMenuCommandOnce=bool(), pmo=bool(), radialPosition=str(), rp=str(),
             radioButton=bool(), rb=bool(), runTimeCommand=str(), rtc=str(), sourceType=str(), stp=str(),
             subMenu=bool(), sm=bool(), tearOff=bool(), to=bool(), useTemplate=str(), ut=str(), version=str(),
             ver=str(), visible=bool(), vis=bool(), *args, **kwargs):
    pass


def menuSet(addMenu=str(), am=str(), allMenuSets=bool(), ams=bool(), currentMenuSet=str(), cms=str(), exists=str(),
            ex=str(), hotBoxVisible=bool(), hbv=bool(), insertMenu=list, im=list, label=str(), l=str(), menuArray=list,
            ma=list, moveMenu=list, mm=list, moveMenuSet=list, mms=list, numberOfMenuSets=bool(), nms=bool(),
            numberOfMenus=bool(), nm=bool(), permanent=bool(), p=bool(), removeMenu=str(), rm=str(),
            removeMenuSet=str(), rms=str(), *args, **kwargs):
    pass


def menuSetPref(exists=bool(), e=bool(), force=bool(), f=bool(), loadAll=bool(), la=bool(), removeAll=bool(), ra=bool(),
                saveAll=bool(), sa=bool(), saveBackup=bool(), sb=bool(), version=bool(), v=bool(), *args, **kwargs):
    pass


def messageLine(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(),
                docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
                en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
                visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                **kwargs):
    pass


def mimicManipulation(manipulations=str(), m=str(), prevalidation=bool(), p=bool(), refresh=bool(), r=bool(), *args,
                      **kwargs):
    pass


def minimizeApp(*args, **kwargs):
    pass


def mirrorJoint(mirrorBehavior=bool(), mb=bool(), mirrorXY=bool(), mxy=bool(), mirrorXZ=bool(), mxz=bool(),
                mirrorYZ=bool(), myz=bool(), searchReplace=list, sr=list, *args, **kwargs):
    pass


def modelCurrentTimeCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                        i2=str(), image3=str(), i3=str(), name=str(), n=str(), percent=float(), per=float(), *args,
                        **kwargs):
    pass


def modelEditor(activeComponentsXray=bool(), acx=bool(), activeCustomEnvironment=str(), ace=str(),
                activeCustomGeometry=str(), acg=str(), activeCustomLighSet=str(), acl=str(),
                activeCustomOverrideGeometry=str(), aog=str(), activeCustomRenderer=str(), acr=str(), activeOnly=bool(),
                ao=bool(), activeShadingGraph=str(), asg=str(), activeView=bool(), av=bool(), addObjects=str(),
                aob=str(), addSelected=bool(), addSelectedObjects=bool(), aso=bool(), allObjects=bool(), alo=bool(),
                backfaceCulling=bool(), bfc=bool(), bufferMode=str(), bm=str(), bumpResolution=list, brz=list,
                camera=str(), cam=str(), cameraName=str(), cn=str(), cameraSet=str(), cst=str(), cameraSetup=bool(),
                cs=bool(), cameras=bool(), ca=bool(), capture=str(), cpt=str(), captureSequenceNumber=int(), csn=int(),
                clipGhosts=bool(), cg=bool(), cmEnabled=bool(), cme=bool(), colorMap=bool(), cm=bool(),
                colorResolution=list, crz=list, control=bool(), ctl=bool(), controlVertices=bool(), cv=bool(),
                cullingOverride=str(), cov=str(), default=bool(), d=bool(), defineTemplate=str(), dt=str(),
                deformers=bool(), df=bool(), dimensions=bool(), dim=bool(), displayAppearance=str(), da=str(),
                displayLights=str(), dl=str(), displayTextures=bool(), dtx=bool(), docTag=str(), dtg=str(),
                dynamicConstraints=bool(), dc=bool(), dynamics=bool(), dy=bool(), editorChanged=str(), ec=str(),
                exists=bool(), ex=bool(), exposure=float(), exp=float(), filter=str(), f=str(),
                filteredObjectList=bool(), fol=bool(), fluids=bool(), fl=bool(), fogColor=list, fcl=list,
                fogDensity=float(), fdn=float(), fogEnd=float(), fen=float(), fogMode=str(), fmd=str(), fogSource=str(),
                fsc=str(), fogStart=float(), fst=float(), fogging=bool(), fg=bool(), follicles=bool(), fo=bool(),
                forceMainConnection=str(), fmc=str(), gamma=float(), ga=float(), greasePencils=bool(), gp=bool(),
                grid=bool(), gr=bool(), hairSystems=bool(), hs=bool(), handles=bool(), ha=bool(), headsUpDisplay=bool(),
                hud=bool(), height=bool(), h=bool(), highlightConnection=str(), hlc=str(), hulls=bool(), hu=bool(),
                ignorePanZoom=bool(), ipz=bool(), ikHandles=bool(), ikh=bool(), imagePlane=bool(), imp=bool(),
                interactive=bool(), i=bool(), interactiveBackFaceCull=bool(), ibc=bool(),
                interactiveDisableShadows=bool(), dis=bool(), isFiltered=bool(), jointXray=bool(), jx=bool(),
                joints=bool(), j=bool(), lights=bool(), lt=bool(), lineWidth=float(), lw=float(), locators=bool(),
                lc=bool(), lockMainConnection=bool(), lck=bool(), lowQualityLighting=bool(), lql=bool(),
                mainListConnection=str(), mlc=str(), manipulators=bool(), m=bool(), maxConstantTransparency=float(),
                mct=float(), maximumNumHardwareLights=bool(), mhl=bool(), modelPanel=str(), mp=str(),
                motionTrails=bool(), mt=bool(), nCloths=bool(), ncl=bool(), nParticles=bool(), npa=bool(),
                nRigids=bool(), nr=bool(), noUndo=bool(), nud=bool(), nurbsCurves=bool(), nc=bool(),
                nurbsSurfaces=bool(), ns=bool(), objectFilter=str(), obf=str(), objectFilterList=str(), ofl=str(),
                objectFilterListUI=str(), ofu=str(), objectFilterShowInHUD=bool(), ofs=bool(), objectFilterUI=str(),
                obu=str(), occlusionCulling=bool(), ocl=bool(), panel=str(), pnl=str(), parent=str(), p=str(),
                particleInstancers=bool(), pi=bool(), pivots=bool(), pv=bool(), planes=bool(), pl=bool(),
                pluginObjects=list, po=list, pluginShapes=bool(), ps=bool(), polymeshes=bool(), pm=bool(),
                queryPluginObjects=str(), qpo=str(), removeSelected=bool(), rs=bool(), rendererDeviceName=bool(),
                rdn=bool(), rendererList=bool(), rls=bool(), rendererListUI=bool(), rlu=bool(), rendererName=str(),
                rnm=str(), rendererOverrideList=bool(), rol=bool(), rendererOverrideListUI=bool(), rou=bool(),
                rendererOverrideName=str(), rom=str(), resetCustomCamera=bool(), rcc=bool(), sceneRenderFilter=str(),
                srf=str(), selectionConnection=str(), slc=str(), selectionHiliteDisplay=bool(), sel=bool(),
                setSelected=bool(), ss=bool(), shadingModel=int(), sml=int(), shadows=bool(), sdw=bool(),
                smallObjectCulling=bool(), soc=bool(), smallObjectThreshold=float(), sot=float(),
                smoothWireframe=bool(), swf=bool(), sortTransparent=bool(), st=bool(), stateString=bool(), sts=bool(),
                stereoDrawMode=bool(), sdm=bool(), strokes=bool(), str=bool(), subdivSurfaces=bool(), sds=bool(),
                textureAnisotropic=bool(), ta=bool(), textureCompression=bool(), tcp=bool(), textureDisplay=str(),
                td=str(), textureEnvironmentMap=bool(), tem=bool(), textureHilight=bool(), th=bool(),
                textureMaxSize=int(), tms=int(), textureMemoryUsed=bool(), tmu=bool(), textureSampling=int(), ts=int(),
                textures=bool(), tx=bool(), toggleExposure=bool(), tge=bool(), toggleGamma=bool(), tgg=bool(),
                transpInShadows=bool(), tis=bool(), transparencyAlgorithm=str(), tal=str(), twoSidedLighting=bool(),
                tsl=bool(), unParent=bool(), up=bool(), unlockMainConnection=bool(), ulk=bool(), updateColorMode=bool(),
                ucm=bool(), updateMainConnection=bool(), upd=bool(), useBaseRenderer=bool(), ubr=bool(),
                useColorIndex=bool(), uci=bool(), useDefaultMaterial=bool(), udm=bool(), useInteractiveMode=bool(),
                ui=bool(), useRGBImagePlane=bool(), ip=bool(), useReducedRenderer=bool(), urr=bool(), useTemplate=str(),
                ut=str(), userNode=str(), un=str(), viewObjects=bool(), vo=bool(), viewSelected=bool(), vs=bool(),
                viewTransformName=str(), vtn=str(), viewType=bool(), vt=bool(), width=bool(), w=bool(),
                wireframeBackingStore=bool(), wbs=bool(), wireframeOnShaded=bool(), wos=bool(), xray=bool(), xr=bool(),
                *args, **kwargs):
    pass


def modelPanel(barLayout=bool(), bl=bool(), camera=str(), cam=str(), control=bool(), ctl=bool(), copy=str(), cp=str(),
               createString=bool(), cs=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
               editString=bool(), es=bool(), exists=bool(), ex=bool(), init=bool(), isUnique=bool(), iu=bool(),
               label=str(), l=str(), menuBarRepeatLast=bool(), mrl=bool(), menuBarVisible=bool(), mbv=bool(),
               modelEditor=bool(), me=bool(), needsInit=bool(), ni=bool(), parent=str(), p=str(),
               popupMenuProcedure=str(), pmp=str(), replacePanel=str(), rp=str(), tearOff=bool(), to=bool(),
               tearOffCopy=str(), toc=str(), tearOffRestore=bool(), tor=bool(), unParent=bool(), up=bool(),
               useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def moduleInfo(definition=bool(), d=bool(), listModules=bool(), lm=bool(), moduleName=str(), mn=str(), path=bool(),
               p=bool(), version=bool(), v=bool(), *args, **kwargs):
    pass


def mouse(enableScrollWheel=bool(), esw=bool(), mouseButtonTracking=int(), mbt=int(), mouseButtonTrackingStatus=bool(),
          mbs=bool(), scrollWheelStatus=bool(), sws=bool(), *args, **kwargs):
    pass


def move(absolute=bool(), a=bool(), componentOffset=bool(), co=bool(), componentSpace=bool(), cs=bool(),
         constrainAlongNormal=bool(), xn=bool(), deletePriorHistory=bool(), dph=bool(), localSpace=bool(), ls=bool(),
         moveX=bool(), x=bool(), moveXY=bool(), xy=bool(), moveXYZ=bool(), xyz=bool(), moveXZ=bool(), xz=bool(),
         moveY=bool(), y=bool(), moveYZ=bool(), yz=bool(), moveZ=bool(), z=bool(), objectSpace=bool(), os=bool(),
         orientJoint=str(), oj=str(), parameter=bool(), p=bool(), preserveChildPosition=bool(), pcp=bool(),
         preserveGeometryPosition=bool(), pgp=bool(), preserveUV=bool(), puv=bool(), reflection=bool(), rfl=bool(),
         reflectionAboutBBox=bool(), rab=bool(), reflectionAboutOrigin=bool(), rao=bool(), reflectionAboutX=bool(),
         rax=bool(), reflectionAboutY=bool(), ray=bool(), reflectionAboutZ=bool(), raz=bool(),
         reflectionTolerance=float(), rft=float(), relative=bool(), r=bool(), rotatePivotRelative=bool(), rpr=bool(),
         scalePivotRelative=bool(), spr=bool(), secondaryAxisOrient=str(), sao=str(), symNegative=bool(), smn=bool(),
         worldSpace=bool(), ws=bool(), worldSpaceDistance=bool(), wd=bool(), xformConstraint=str(), xc=str(), *args,
         **kwargs):
    pass


def moveKeyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
               image3=str(), i3=str(), moveFunction=str(), mf=str(), name=str(), n=str(), option=str(), o=str(), *args,
               **kwargs):
    pass


def moveVertexAlongDirection(direction=list, d=list, magnitude=float(), m=float(), normalDirection=float(), n=float(),
                             uDirection=float(), u=float(), uvNormalDirection=list, uvn=list, vDirection=float(),
                             v=float(), *args, **kwargs):
    pass


def movieInfo(counter=bool(), cn=bool(), dropFrame=bool(), df=bool(), frameCount=bool(), f=bool(), frameDuration=bool(),
              fd=bool(), height=bool(), h=bool(), movieTexture=bool(), mt=bool(), negTimesOK=bool(), nt=bool(),
              numFrames=bool(), nf=bool(), quickTime=bool(), qt=bool(), timeCode=bool(), tc=bool(),
              timeCodeTrack=bool(), tt=bool(), timeScale=bool(), ts=bool(), twentyFourHourMax=bool(), tf=bool(),
              width=bool(), w=bool(), *args, **kwargs):
    pass


def movIn(file=str(), f=str(), startTime=float(), st=float(), *args, **kwargs):
    pass


def movOut(comment=bool(), c=bool(), file=str(), f=str(), precision=int(), pre=int(), time=tuple(), t=tuple(), *args,
           **kwargs):
    pass


def multiProfileBirailSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                              nodeState=int(), nds=int(), object=bool(), o=bool(), polygon=int(), po=int(),
                              tangentContinuityProfile1=bool(), tp1=bool(), tangentContinuityProfile2=bool(),
                              tp2=bool(), transformMode=int(), tm=int(), *args, **kwargs):
    pass


def multiTouch(gestures=bool(), g=bool(), trackpad=int(), t=int(), *args, **kwargs):
    pass


def mute(disable=bool(), d=bool(), force=bool(), f=bool(), *args, **kwargs):
    pass


def nameCommand(annotation=str(), ann=str(), command=str(), c=str(), data1=str(), da1=str(), data2=str(), da2=str(),
                data3=str(), da3=str(), default=bool(), d=bool(), sourceType=str(), stp=str(), *args, **kwargs):
    pass


def nameField(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(),
              defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
              drawInactiveFrame=bool(), dif=bool(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
              enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
              fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(),
              io=bool(), manage=bool(), m=bool(), nameChangeCommand=str(), ncc=str(), noBackground=bool(), nbg=bool(),
              numberOfPopupMenus=bool(), npm=bool(), object=str(), o=str(), parent=str(), p=str(),
              popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), receiveFocusCommand=str(),
              rfc=str(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
              visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def namespace(absoluteName=bool(), an=bool(), addNamespace=str(), add=str(), collapseAncestors=str(), ch=str(),
              deleteNamespaceContent=bool(), dnc=bool(), exists=str(), ex=str(), force=bool(), f=bool(),
              isRootNamespace=str(), ir=str(), mergeNamespaceWithOther=str(), mno=str(),
              mergeNamespaceWithParent=bool(), mnp=bool(), mergeNamespaceWithRoot=bool(), mnr=bool(),
              moveNamespace=list, mv=list, parent=str(), p=str(), recurse=bool(), r=bool(), relativeNames=bool(),
              rel=bool(), removeNamespace=str(), rm=str(), rename=list, ren=list, setNamespace=str(), set=str(),
              validateName=str(), vn=str(), *args, **kwargs):
    pass


def namespaceInfo(absoluteName=bool(), an=bool(), baseName=bool(), bn=bool(), currentNamespace=bool(), cur=bool(),
                  dagPath=bool(), dp=bool(), fullName=bool(), fn=bool(), internal=bool(), int=bool(),
                  isRootNamespace=bool(), ir=bool(), listNamespace=bool(), ls=bool(), listOnlyDependencyNodes=bool(),
                  lod=bool(), listOnlyNamespaces=bool(), lon=bool(), parent=bool(), p=bool(), recurse=bool(), r=bool(),
                  shortName=bool(), sn=bool(), *args, **kwargs):
    pass


def nBase(clearCachedTextureMap=str(), cct=str(), clearStart=bool(), cs=bool(), stuffStart=bool(), ss=bool(),
          textureToVertex=str(), ttv=str(), *args, **kwargs):
    pass


def newton(attenuation=float(), att=float(), magnitude=float(), m=float(), maxDistance=float(), mxd=float(),
           minDistance=float(), mnd=float(), name=str(), n=str(), perVertex=bool(), pv=bool(), position=list, pos=list,
           torusSectionRadius=float(), tsr=float(), volumeExclusion=bool(), vex=bool(), volumeOffset=list, vof=list,
           volumeShape=str(), vsh=str(), volumeSweep=float(), vsw=float(), *args, **kwargs):
    pass


def nodeCast(copyDynamicAttrs=bool(), cda=bool(), disableAPICallbacks=bool(), dsa=bool(),
             disableScriptJobCallbacks=bool(), dsj=bool(), disconnectUnmatchedAttrs=bool(), dua=bool(), force=bool(),
             f=bool(), swapNames=bool(), sn=bool(), swapValues=bool(), sv=bool(), *args, **kwargs):
    pass


def nodeEditor(activeTab=int(), at=int(), addNewNodes=bool(), ann=bool(), addNode=str(), an=str(),
               additiveGraphingMode=bool(), agm=bool(), allAttributes=bool(), ala=bool(), allNodes=bool(), aln=bool(),
               allowNewTabs=bool(), ant=bool(), allowTabTearoff=bool(), att=bool(), autoSizeNodes=bool(), asn=bool(),
               beginCreateNode=bool(), bcn=bool(), beginNewConnection=str(), bnc=str(), breakSelectedConnections=bool(),
               bsc=bool(), closeAllTabs=bool(), cat=bool(), closeTab=int(), clt=int(), connectSelectedNodes=bool(),
               csn=bool(), connectionMinSegment=float(), csm=float(), connectionOffset=float(), cso=float(),
               connectionRoundness=float(), csr=float(), connectionStyle=str(), cs=str(), connectionTension=int(),
               cst=int(), consistentNameSize=bool(), cns=bool(), contentsChangedCommand=str(), cc=str(), control=bool(),
               ctl=bool(), createInfo=str(), ci=str(), createNodeCommand=str(), cnc=str(), createTab=list, ct=list,
               crosshairOnEdgeDragging=bool(), ced=bool(), customAttributeListEdit=list, cal=list, cycleHUD=bool(),
               ch=bool(), defaultPinnedState=bool(), dps=bool(), defineTemplate=str(), dt=str(), deleteSelected=bool(),
               docTag=str(), dtg=str(), dotFormat=str(), dot=str(), downstream=bool(), ds=bool(), duplicateTab=list,
               dpt=list, enableOpenGL=bool(), egl=bool(), exists=bool(), ex=bool(), extendToShapes=bool(), ets=bool(),
               feedbackConnection=bool(), fbc=bool(), feedbackNode=bool(), fbn=bool(), feedbackPlug=bool(), fbp=bool(),
               feedbackTabIndex=bool(), fbi=bool(), feedbackType=bool(), fbt=bool(), filter=str(), f=str(),
               filterCreateNodeTypes=str(), fcn=str(), focusCommand=str(), fc=str(), forceMainConnection=str(),
               fmc=str(), frameAll=bool(), fa=bool(), frameModelSelection=bool(), fms=bool(), frameSelected=bool(),
               fs=bool(), getNodeList=bool(), gnl=bool(), graphSelectedConnections=bool(), gsc=bool(),
               graphSelection=bool(), gsl=bool(), gridSnap=bool(), gs=bool(), gridVisibility=bool(), gv=bool(),
               hasWatchpoint=bool(), hw=bool(), highlightConnection=str(), hlc=str(), highlightConnections=list,
               hc=list, hudMessage=list, hm=list, ignoreAssets=bool(), ia=bool(), island=bool(), isl=bool(),
               keyPressCommand=str(), kpc=str(), keyReleaseCommand=str(), krc=str(), layout=bool(), lay=bool(),
               layoutCommand=str(), lc=str(), lockMainConnection=bool(), lck=bool(), mainListConnection=str(),
               mlc=str(), nodeSwatchSize=str(), nss=str(), nodeTitleMode=str(), ntm=str(), nodeViewMode=str(),
               nvm=str(), overrideNodeDropPosition=list, onp=list, panView=list, pv=list, panel=str(), pnl=str(),
               parent=str(), p=str(), pinSelectedNodes=bool(), psn=bool(), popupMenuScript=str(), pms=str(),
               primary=bool(), pr=bool(), redockTab=bool(), rdt=bool(), removeDownstream=bool(), rd=bool(),
               removeNode=str(), rem=str(), removeUnselected=bool(), run=bool(), removeUpstream=bool(), ru=bool(),
               renameNode=str(), ren=str(), renameTab=list, rt=list, restoreInfo=str(), ri=str(),
               restoreLastClosedTab=bool(), rlt=bool(), rootNode=str(), rn=str(), rootsFromSelection=bool(), rfs=bool(),
               scaleView=float(), sv=float(), selectAll=bool(), sa=bool(), selectConnectionNodes=bool(), scn=bool(),
               selectDownstream=bool(), sd=bool(), selectFeedbackConnection=bool(), sfc=bool(), selectNode=str(),
               sln=str(), selectUpstream=bool(), su=bool(), selectionConnection=str(), slc=str(), setWatchpoint=bool(),
               sw=bool(), settingsChangedCallback=str(), scc=str(), shaderNetworks=bool(), sns=bool(),
               showAllNodeAttributes=str(), saa=str(), showNamespace=bool(), sn=bool(), showSGShapes=bool(), ssg=bool(),
               showShapes=bool(), ss=bool(), showTabs=bool(), tab=bool(), showTransforms=bool(), st=bool(),
               stateString=bool(), sts=bool(), syncedSelection=bool(), ssl=bool(), tabChangeCommand=str(), tcc=str(),
               toggleAttrFilter=bool(), taf=bool(), toggleSelectedPins=bool(), tsp=bool(), toggleSwatchSize=str(),
               tss=str(), toolTipCommand=str(), ttc=str(), traversalDepthLimit=int(), tdl=int(), unParent=bool(),
               up=bool(), unlockMainConnection=bool(), ulk=bool(), updateMainConnection=bool(), upd=bool(),
               upstream=bool(), ups=bool(), useAssets=bool(), ua=bool(), useLongName=int(), uln=int(),
               useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def nodeIconButton(align=str(), al=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list, command=str(),
                   c=str(), defineTemplate=str(), dt=str(), disabledImage=str(), di=str(), docTag=str(), dtg=str(),
                   dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                   enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                   ex=bool(), flipX=bool(), fx=bool(), flipY=bool(), fy=bool(), font=str(), fn=str(),
                   fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, image=str(),
                   i=str(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                   imageOverlayLabel=str(), iol=str(), isObscured=bool(), io=bool(), label=str(), l=str(),
                   labelOffset=int(), lo=int(), ltVersion=str(), lt=str(), manage=bool(), m=bool(), marginHeight=int(),
                   mh=int(), marginWidth=int(), mw=int(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(),
                   npm=bool(), overlayLabelBackColor=list, olb=list, overlayLabelColor=list, olc=list, parent=str(),
                   p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rotation=float(),
                   rot=float(), statusBarMessage=str(), sbm=str(), style=str(), st=str(), useAlpha=bool(), ua=bool(),
                   useTemplate=str(), ut=str(), version=str(), ver=str(), visible=bool(), vis=bool(),
                   visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def nodeOutliner(addCommand=str(), ac=str(), addObject=str(), a=str(), annotation=str(), ann=str(),
                 attrAlphaOrder=str(), aao=str(), backgroundColor=list, bgc=list, connectivity=str(), c=str(),
                 currentSelection=bool(), cs=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                 dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                 enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
                 fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                 isObscured=bool(), io=bool(), lastClickedNode=bool(), lcn=bool(), lastMenuChoice=str(), lmc=str(),
                 longNames=bool(), ln=bool(), manage=bool(), m=bool(), menuCommand=str(), mc=str(),
                 menuMultiOption=bool(), mmo=bool(), multiSelect=bool(), ms=bool(), niceNames=bool(), nn=bool(),
                 noBackground=bool(), nbg=bool(), noConnectivity=bool(), nc=bool(), nodesDisplayed=bool(), nd=bool(),
                 numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                 pressHighlightsUnconnected=bool(), phu=bool(), preventOverride=bool(), po=bool(), redraw=bool(),
                 r=bool(), redrawRow=bool(), rr=bool(), remove=str(), rm=str(), removeAll=bool(), rma=bool(),
                 replace=str(), rpl=str(), selectCommand=str(), sc=str(), showConnectedOnly=bool(), sco=bool(),
                 showHidden=bool(), sh=bool(), showInputs=bool(), si=bool(), showNonConnectable=bool(), snc=bool(),
                 showNonKeyable=bool(), snk=bool(), showOutputs=bool(), so=bool(), showPublished=bool(), sp=bool(),
                 showReadOnly=bool(), sro=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
                 visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                 **kwargs):
    pass


def nodePreset(attributes=str(), atr=str(), custom=str(), ctm=str(), delete=list, exists=list, ex=list,
               isValidName=str(), ivn=str(), list=str(), ls=str(), load=list, ld=list, save=list, sv=list, *args,
               **kwargs):
    pass


def nodeTreeLister(addFavorite=str(), af=str(), addItem=list, add=list, addVnnItem=list, avi=list, annotation=str(),
                   ann=str(), backgroundColor=list, bgc=list, clearContents=bool(), clr=bool(), collapsePath=str(),
                   cp=str(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                   dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                   enableKeyboardFocus=bool(), ekf=bool(), executeItem=str(), ei=str(), exists=bool(), ex=bool(),
                   expandPath=str(), ep=str(), expandToDepth=int(), etd=int(), favoritesCallback=str(), fcb=str(),
                   favoritesList=bool(), fl=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                   highlightColor=list, hlc=list, isObscured=bool(), io=bool(), itemScript=str(), isc=str(),
                   manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), nodeLibrary=str(), nl=str(),
                   numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                   preventOverride=bool(), po=bool(), refreshCommand=str(), rc=str(), removeFavorite=str(), rf=str(),
                   removeItem=str(), rem=str(), resultsPathUnderCursor=bool(), ruc=bool(), selectPath=str(), sp=str(),
                   statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                   visibleChangeCommand=str(), vcc=str(), vnnString=bool(), vnn=bool(), width=int(), w=int(), *args,
                   **kwargs):
    pass


def nodeType(apiType=bool(), api=bool(), derived=bool(), d=bool(), inherited=bool(), i=bool(), isTypeName=bool(),
             itn=bool(), ufeRuntimeName=bool(), urn=bool(), *args, **kwargs):
    pass


def nonLinear(after=bool(), af=bool(), afterReference=bool(), ar=bool(), autoParent=bool(), ap=bool(), before=bool(),
              bf=bool(), commonParent=bool(), cp=bool(), defaultScale=bool(), ds=bool(), deformerTools=bool(),
              dt=bool(), exclusive=str(), ex=str(), frontOfChain=bool(), foc=bool(), geometry=str(), g=str(),
              geometryIndices=bool(), gi=bool(), ignoreSelected=bool(), includeHiddenSelections=bool(), ihs=bool(),
              name=str(), n=str(), parallel=bool(), par=bool(), prune=bool(), pr=bool(), remove=bool(), rm=bool(),
              split=bool(), sp=bool(), type=str(), typ=str(), useComponentTags=bool(), uct=bool(), *args, **kwargs):
    pass


def normalConstraint(aimVector=list, aim=list, layer=str(), l=str(), name=str(), n=str(), remove=bool(), rm=bool(),
                     targetList=bool(), tl=bool(), upVector=list, u=list, weight=float(), w=float(),
                     weightAliasList=bool(), wal=bool(), worldUpObject=str(), wuo=str(), worldUpType=str(), wut=str(),
                     worldUpVector=list, wu=list, *args, **kwargs):
    pass


def nParticle(attribute=str(), at=str(), cache=bool(), ch=bool(), conserve=float(), c=float(), count=bool(), ct=bool(),
              deleteCache=bool(), dc=bool(), dynamicAttrList=bool(), dal=bool(), floatValue=float(), fv=float(),
              gridSpacing=float(), grs=float(), inherit=float(), i=float(), jitterBasePoint=list, jbp=list,
              jitterRadius=float(), jr=float(), lowerLeft=list, ll=list, name=str(), n=str(), numJitters=int(),
              nj=int(), order=int(), particleId=int(), id=int(), perParticleDouble=bool(), ppd=bool(),
              perParticleVector=bool(), ppv=bool(), position=list, p=list, shapeName=str(), sn=str(), upperRight=list,
              ur=list, vectorValue=list, vv=list, *args, **kwargs):
    pass


def nSoft(convert=bool(), c=bool(), duplicate=bool(), d=bool(), duplicateHistory=bool(), dh=bool(), goal=float(),
          g=float(), hideOriginal=bool(), h=bool(), *args, **kwargs):
    pass


def nurbsBoolean(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                 nodeState=int(), nds=int(), nsrfsInFirstShell=int(), nsf=int(), object=bool(), o=bool(),
                 operation=int(), op=int(), smartConnection=bool(), sc=bool(), tolerance=float(), tlb=float(), *args,
                 **kwargs):
    pass


def nurbsCopyUVSet(*args, **kwargs):
    pass


def nurbsCube(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), degree=int(),
              d=int(), heightRatio=float(), hr=float(), lengthRatio=float(), lr=float(), name=str(), n=str(),
              nodeState=int(), nds=int(), object=bool(), o=bool(), patchesU=int(), u=int(), patchesV=int(), v=int(),
              pivot=list, p=list, polygon=int(), po=int(), width=float(), w=float(), *args, **kwargs):
    pass


def nurbsCurveToBezier(*args, **kwargs):
    pass


def nurbsEditUV(angle=float(), a=float(), pivotU=float(), pu=float(), pivotV=float(), pv=float(), relative=bool(),
                r=bool(), rotateRatio=float(), rr=float(), rotation=bool(), rot=bool(), scale=bool(), s=bool(),
                scaleU=float(), su=float(), scaleV=float(), sv=float(), uValue=float(), u=float(), vValue=float(),
                v=float(), *args, **kwargs):
    pass


def nurbsPlane(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), degree=int(),
               d=int(), lengthRatio=float(), lr=float(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(),
               o=bool(), patchesU=int(), u=int(), patchesV=int(), v=int(), pivot=list, p=list, polygon=int(), po=int(),
               width=float(), w=float(), *args, **kwargs):
    pass


def nurbsSelect(borderSelection=bool(), bs=bool(), bottomBorder=bool(), bb=bool(), growSelection=int(), gs=int(),
                leftBorder=bool(), lb=bool(), rightBorder=bool(), rb=bool(), shrinkSelection=int(), ss=int(),
                topBorder=bool(), tb=bool(), *args, **kwargs):
    pass


def nurbsSquare(caching=bool(), cch=bool(), center=list, c=list, centerX=float(), cx=float(), centerY=float(),
                cy=float(), centerZ=float(), cz=float(), constructionHistory=bool(), ch=bool(), degree=int(), d=int(),
                name=str(), n=str(), nodeState=int(), nds=int(), normal=list, nr=list, normalX=float(), nrx=float(),
                normalY=float(), nry=float(), normalZ=float(), nrz=float(), object=bool(), o=bool(),
                sideLength1=float(), sl1=float(), sideLength2=float(), sl2=float(), spansPerSide=int(), sps=int(),
                *args, **kwargs):
    pass


def nurbsToPoly(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), curvatureTolerance=int(), cvt=int(),
                explicitTessellationAttributes=bool(), eta=bool(), name=str(), n=str(), nodeState=int(), nds=int(),
                object=bool(), o=bool(), smoothEdge=bool(), ues=bool(), smoothEdgeRatio=float(), esr=float(),
                uDivisionsFactor=float(), nuf=float(), vDivisionsFactor=float(), nvf=float(), *args, **kwargs):
    pass


def nurbsToPolygonsPref(chordHeight=float(), cht=float(), chordHeightRatio=float(), chr=float(), delta3D=float(),
                        d=float(), edgeSwap=bool(), es=bool(), format=int(), f=int(), fraction=float(), ft=float(),
                        matchRenderTessellation=int(), mrt=int(), merge=int(), m=int(), mergeTolerance=float(),
                        mt=float(), minEdgeLen=float(), mel=float(), polyCount=int(), pc=int(), polyType=int(),
                        pt=int(), uNumber=int(), un=int(), uType=int(), ut=int(), useChordHeight=bool(), uch=bool(),
                        useChordHeightRatio=bool(), ucr=bool(), vNumber=int(), vn=int(), vType=int(), vt=int(), *args,
                        **kwargs):
    pass


def nurbsToSubdiv(addUnderTransform=bool(), aut=bool(), caching=bool(), cch=bool(), collapsePoles=bool(), cp=bool(),
                  constructionHistory=bool(), ch=bool(), matchPeriodic=bool(), mp=bool(), maxPolyCount=int(), mpc=int(),
                  name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), reverseNormal=bool(),
                  rn=bool(), *args, **kwargs):
    pass


def nurbsToSubdivPref(bridge=int(), br=int(), capType=int(), ct=int(), collapsePoles=bool(), cp=bool(),
                      matchPeriodic=bool(), mp=bool(), maxPolyCount=int(), mpc=int(), offset=float(), o=float(),
                      reverseNormal=bool(), rn=bool(), solidType=int(), st=int(), trans00=float(), t00=float(),
                      trans01=float(), t01=float(), trans02=float(), t02=float(), trans10=float(), t10=float(),
                      trans11=float(), t11=float(), trans12=float(), t12=float(), trans20=float(), t20=float(),
                      trans21=float(), t21=float(), trans22=float(), t22=float(), trans30=float(), t30=float(),
                      trans31=float(), t31=float(), trans32=float(), t32=float(), *args, **kwargs):
    pass


def nurbsUVSet(create=bool(), c=bool(), useExplicit=bool(), ue=bool(), *args, **kwargs):
    pass


def objectCenter(gl=bool(), local=bool(), l=bool(), x=bool(), y=bool(), z=bool(), *args, **kwargs):
    pass


def objectType(*args, isAType: str = None, isa: str = None, isType: str = None, i: str = None, tagFromType: str = None,
               tgt: str = None, typeFromTag: int = None, tpt: int = None, typeTag: bool = None, tt: bool = None,
               **kwargs):
    
    if args:
        object_name = args[0]
        as_obj = _hierarchy.NodePool.from_name(object_name)
        if not as_obj:
            raise RuntimeError(f"No object matches name: {object_name}")
        if isType or i:
            compare = isType or i
            return f"{as_obj.apiTypeStr[1].lower()}{as_obj.apiTypeStr[2:]}" == compare


def objectTypeUI(isType=str(), i=str(), listAll=bool(), la=bool(), superClasses=bool(), sc=bool(), *args, **kwargs):
    pass


def objExists(node_name: str) -> bool:
    if node := _hierarchy.NodePool.from_name(node_name):
        return node._alive
    else:
        return False


def offsetCurve(caching=bool(), cch=bool(), connectBreaks=int(), cb=int(), constructionHistory=bool(), ch=bool(),
                cutLoop=bool(), cl=bool(), cutRadius=float(), cr=float(), distance=float(), d=float(), name=str(),
                n=str(), nodeState=int(), nds=int(), normal=list, nr=list, object=bool(), o=bool(), range=bool(),
                rn=bool(), reparameterize=bool(), rp=bool(), stitch=bool(), st=bool(), subdivisionDensity=int(),
                sd=int(), tolerance=float(), tol=float(), useGivenNormal=bool(), ugn=bool(), *args, **kwargs):
    pass


def offsetCurveOnSurface(caching=bool(), cch=bool(), checkPoints=int(), cp=int(), connectBreaks=int(), cb=int(),
                         constructionHistory=bool(), ch=bool(), cutLoop=bool(), cl=bool(), distance=float(), d=float(),
                         name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), range=bool(),
                         rn=bool(), stitch=bool(), st=bool(), subdivisionDensity=int(), sd=int(), tolerance=float(),
                         tol=float(), *args, **kwargs):
    pass


def offsetSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), distance=float(), d=float(),
                  method=int(), m=int(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(),
                  *args, **kwargs):
    pass


def ogs(deviceInformation=bool(), di=bool(), disposeReleasableTextures=bool(), drt=bool(), dumpTexture=str(), dt=str(),
        enableHardwareInstancing=bool(), hwi=bool(), fragmentEditor=str(), fe=str(), fragmentXML=str(), xml=str(),
        gpuMemoryTotal=int(), gmt=int(), gpuMemoryUsed=bool(), gpu=bool(), isLegacyViewportEnabled=bool(), lve=bool(),
        isRemoteGLSessionEnabled=bool(), rgl=bool(), isWinRemoteSession=bool(), irs=bool(), pause=bool(), p=bool(),
        rebakeTextures=bool(), rbt=bool(), regenerateUVTilePreview=str(), rup=str(), reloadTextures=bool(), rlt=bool(),
        reset=bool(), r=bool(), shaderSource=str(), ss=str(), toggleTexturePaging=bool(), ttp=bool(),
        traceRenderPipeline=bool(), trp=bool(), *args, **kwargs):
    pass


def ogsRender(activeMultisampleType=str(), mst=str(), activeRenderOverride=str(), cro=str(),
              activeRenderTargetFormat=str(), fpt=str(), availableFloatingPointTargetFormat=bool(), afp=bool(),
              availableMultisampleType=bool(), amt=bool(), availableRenderOverrides=bool(), aro=bool(), camera=str(),
              cam=str(), currentFrame=bool(), cf=bool(), currentView=bool(), cv=bool(),
              enableFloatingPointRenderTarget=bool(), efp=bool(), enableMultisample=bool(), ems=bool(), frame=float(),
              f=float(), height=int(), h=int(), layer=str(), l=str(), noRenderView=bool(), nrv=bool(), width=int(),
              w=int(), *args, **kwargs):
    pass


def openCLInfo(minVertexBuffer=bool(), mvb=bool(), valid=bool(), v=bool(), *args, **kwargs):
    pass


def openGLExtension(extension=str(), ext=str(), renderer=bool(), rnd=bool(), vendor=bool(), vnd=bool(), version=bool(),
                    ver=bool(), *args, **kwargs):
    pass


def openMayaPref(errlog=bool(), el=bool(), lazyLoad=bool(), lz=bool(), oldPluginWarning=bool(), ow=bool(), *args,
                 **kwargs):
    pass


def optionMenu(alwaysCallChangeCommand=bool(), acc=bool(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
               beforeShowPopup=str(), bsp=str(), changeCommand=str(), cc=str(), defineTemplate=str(), dt=str(),
               deleteAllItems=bool(), dai=bool(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
               dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
               enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(),
               height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(), itemListLong=bool(),
               ill=bool(), itemListShort=bool(), ils=bool(), label=str(), l=str(), manage=bool(), m=bool(),
               maxVisibleItems=int(), mvi=int(), noBackground=bool(), nbg=bool(), numberOfItems=bool(), ni=bool(),
               numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
               postMenuCommand=str(), pmc=str(), postMenuCommandOnce=bool(), pmo=bool(), preventOverride=bool(),
               po=bool(), select=int(), sl=int(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
               value=str(), v=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(),
               w=int(), *args, **kwargs):
    pass


def optionMenuGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                  ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                  adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                  changeCommand=str(), cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list,
                  columnAlign3=list, cl3=list, columnAlign4=list, cl4=list, columnAlign5=list, cl5=list,
                  columnAlign6=list, cl6=list, columnAttach=list, cat=list, columnAttach2=list, ct2=list,
                  columnAttach3=list, ct3=list, columnAttach4=list, ct4=list, columnAttach5=list, ct5=list,
                  columnAttach6=list, ct6=list, columnOffset2=list, co2=list, columnOffset3=list, co3=list,
                  columnOffset4=list, co4=list, columnOffset5=list, co5=list, columnOffset6=list, co6=list,
                  columnWidth=list, cw=list, columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list,
                  columnWidth3=list, cw3=list, columnWidth4=list, cw4=list, columnWidth5=list, cw5=list,
                  columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), deleteAllItems=bool(), dai=bool(),
                  docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
                  en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                  ex=bool(), extraLabel=str(), el=str(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                  highlightColor=list, hlc=list, isObscured=bool(), io=bool(), itemListLong=bool(), ill=bool(),
                  itemListShort=bool(), ils=bool(), label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(),
                  nbg=bool(), numberOfItems=bool(), ni=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(),
                  p=str(), popupMenuArray=bool(), pma=bool(), postMenuCommand=str(), pmc=str(),
                  postMenuCommandOnce=bool(), pmo=bool(), preventOverride=bool(), po=bool(), rowAttach=list, rat=list,
                  select=int(), sl=int(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), value=str(),
                  v=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
                  *args, **kwargs):
    pass


def optionVar(arraySize=str(), clearArray=str(), ca=str(), clearStash=str(), cs=str(), exists=str(), ex=str(),
              floatValue=list, fv=list, floatValueAppend=list, fva=list, intValue=list, iv=list, intValueAppend=list,
              iva=list, list=bool(), l=bool(), remove=str(), rm=str(), removeFromArray=list, rfa=list, stash=str(),
              st=str(), stringValue=list, sv=list, stringValueAppend=list, sva=list, unstash=str(), us=str(),
              version=int(), v=int(), *args, **kwargs):
    pass


def orbit(horizontalAngle=float(), ha=float(), pivotPoint=list, pp=list, rotationAngles=list, ra=list,
          verticalAngle=float(), va=float(), *args, **kwargs):
    pass


def orbitCtx(alternateContext=bool(), ac=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
             i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), localOrbit=bool(), lo=bool(), name=str(),
             n=str(), orbitScale=float(), os=float(), toolName=str(), tn=str(), *args, **kwargs):
    pass


def orientConstraint(createCache=list, cc=list, deleteCache=bool(), dc=bool(), layer=str(), l=str(),
                     maintainOffset=bool(), mo=bool(), name=str(), n=str(), offset=list, o=list, remove=bool(),
                     rm=bool(), skip=str(), sk=str(), targetList=bool(), tl=bool(), weight=float(), w=float(),
                     weightAliasList=bool(), wal=bool(), *args, **kwargs):
    pass


def outlinerEditor(allowMultiSelection=bool(), ams=bool(), alwaysToggleSelect=bool(), ats=bool(),
                   animLayerFilterOptions=str(), alf=str(), attrAlphaOrder=str(), aao=str(), attrFilter=str(), af=str(),
                   autoExpand=bool(), xpd=bool(), autoExpandAnimatedShapes=bool(), xas=bool(), autoExpandLayers=bool(),
                   ael=bool(), autoSelectNewObjects=bool(), containersIgnoreFilters=bool(), cif=bool(), control=bool(),
                   ctl=bool(), defineTemplate=str(), dt=str(), directSelect=bool(), ds=bool(), displayMode=str(),
                   dm=str(), doNotSelectNewObjects=bool(), dns=bool(), docTag=str(), dtg=str(), dropIsParent=bool(),
                   dip=bool(), editAttrName=bool(), ean=bool(), exists=bool(), ex=bool(), expandAllItems=bool(),
                   eai=bool(), expandAllSelectedItems=bool(), eas=bool(), expandAttribute=bool(), att=bool(),
                   expandConnections=bool(), xc=bool(), expandObjects=bool(), eo=bool(), feedbackItemName=bool(),
                   fbn=bool(), feedbackRowNumber=bool(), fbr=bool(), filter=str(), f=str(), forceMainConnection=str(),
                   fmc=str(), getCurrentSetOfItem=int(), gcs=int(), highlightActive=bool(), ha=bool(),
                   highlightConnection=str(), hlc=str(), highlightSecondary=bool(), hs=bool(),
                   ignoreDagHierarchy=bool(), hir=bool(), ignoreHiddenAttribute=bool(), iha=bool(),
                   ignoreOutlinerColor=bool(), ioc=bool(), isChildSelected=str(), ics=str(), isSet=int(),
                   isSetMember=int(), ism=int(), isUfeItem=int(), isu=int(), lockMainConnection=bool(), lck=bool(),
                   longNames=bool(), ln=bool(), mainListConnection=str(), mlc=str(), mapMotionTrails=bool(), mmt=bool(),
                   masterOutliner=str(), mst=str(), niceNames=bool(), nn=bool(), object=str(), obj=str(),
                   organizeByClip=bool(), obc=bool(), organizeByLayer=bool(), obl=bool(), panel=str(), pnl=str(),
                   parent=str(), p=str(), parentObject=bool(), po=bool(), pinPlug=str(), pin=str(), refresh=bool(),
                   rfs=bool(), removeFromCurrentSet=int(), rcs=int(), renameItem=int(), rni=int(),
                   renameSelectedItem=bool(), rsi=bool(), renderFilterActive=bool(), rfa=bool(),
                   renderFilterIndex=int(), rfi=int(), renderFilterVisible=bool(), rfv=bool(), selectCommand=str(),
                   sec=str(), selectionConnection=str(), slc=str(), selectionOrder=str(), sod=str(), setFilter=str(),
                   sf=str(), setsIgnoreFilters=bool(), sif=bool(), showAnimCurvesOnly=bool(), aco=bool(),
                   showAnimLayerWeight=bool(), saw=bool(), showAssets=bool(), a=bool(), showAssignedMaterials=bool(),
                   sam=bool(), showAttrValues=bool(), av=bool(), showAttributes=bool(), atr=bool(),
                   showCompounds=bool(), cmp=bool(), showConnected=bool(), con=bool(), showContainedOnly=bool(),
                   sco=bool(), showContainerContents=bool(), scc=bool(), showDagOnly=bool(), dag=bool(),
                   showLeafs=bool(), laf=bool(), showMuteInfo=bool(), smi=bool(), showNamespace=bool(), sn=bool(),
                   showNumericAttrsOnly=bool(), num=bool(), showParentContainers=bool(), spa=bool(),
                   showPinIcons=bool(), spi=bool(), showPublishedAsConnected=bool(), spc=bool(),
                   showReferenceMembers=bool(), rm=bool(), showReferenceNodes=bool(), rn=bool(), showSelected=bool(),
                   sc=bool(), showSetMembers=bool(), ssm=bool(), showShapes=bool(), shp=bool(),
                   showTextureNodesOnly=bool(), tno=bool(), showTimeEditor=bool(), ste=bool(), showUVAttrsOnly=bool(),
                   uv=bool(), showUnitlessCurves=bool(), su=bool(), showUpstreamCurves=bool(), suc=bool(),
                   sortOrder=str(), so=str(), stateString=bool(), sts=bool(), transmitFilters=bool(), tf=bool(),
                   ufeFilter=list, uf=list, ufeFilterValue=bool(), ufv=bool(), unParent=bool(), up=bool(),
                   unlockMainConnection=bool(), ulk=bool(), unpinPlug=str(), unp=str(), updateMainConnection=bool(),
                   upd=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def outlinerPanel(control=bool(), ctl=bool(), copy=str(), cp=str(), createString=bool(), cs=bool(),
                  defineTemplate=str(), dt=str(), divider=int(), div=int(), docTag=str(), dtg=str(), editString=bool(),
                  es=bool(), exists=bool(), ex=bool(), init=bool(), isUnique=bool(), iu=bool(), label=str(), l=str(),
                  menuBarRepeatLast=bool(), mrl=bool(), menuBarVisible=bool(), mbv=bool(), needsInit=bool(), ni=bool(),
                  outlinerEditor=bool(), oe=bool(), parent=str(), p=str(), popupMenuProcedure=str(), pmp=str(),
                  replacePanel=str(), rp=str(), tearOff=bool(), to=bool(), tearOffCopy=str(), toc=str(),
                  tearOffRestore=bool(), tor=bool(), unParent=bool(), up=bool(), useTemplate=str(), ut=str(), *args,
                  **kwargs):
    pass


def outputWindow(show=bool(), s=bool(), *args, **kwargs):
    pass


def overrideModifier(clear=bool(), cl=bool(), press=str(), p=str(), release=str(), r=str(), *args, **kwargs):
    pass


def paintEffectsDisplay(meshDrawEnable=bool(), me=bool(), *args, **kwargs):
    pass


def pairBlend(attribute=str(), at=str(), input1=bool(), i1=bool(), input2=bool(), i2=bool(), node=str(), nd=str(),
              *args, **kwargs):
    pass


def palettePort(actualTotal=int(), at=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                changeCommand=str(), cc=str(), colorEditable=bool(), ced=bool(), colorEdited=str(), ce=str(),
                defineTemplate=str(), dt=str(), dimensions=list, dim=list, docTag=str(), dtg=str(), dragCallback=str(),
                dgc=str(), dropCallback=str(), dpc=str(), editable=bool(), ed=bool(), enable=bool(), en=bool(),
                enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
                fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, hsvValue=list,
                hsv=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                preventOverride=bool(), po=bool(), redraw=bool(), r=bool(), rgbValue=list, rgb=list, setCurCell=int(),
                scc=int(), statusBarMessage=str(), sbm=str(), topDown=bool(), td=bool(), transparent=int(), t=int(),
                useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                width=int(), w=int(), *args, **kwargs):
    pass


def panel(control=bool(), ctl=bool(), copy=str(), cp=str(), createString=bool(), cs=bool(), defineTemplate=str(),
          dt=str(), docTag=str(), dtg=str(), editString=bool(), es=bool(), exists=bool(), ex=bool(), init=bool(),
          isUnique=bool(), iu=bool(), label=str(), l=str(), menuBarRepeatLast=bool(), mrl=bool(), menuBarVisible=bool(),
          mbv=bool(), needsInit=bool(), ni=bool(), parent=str(), p=str(), popupMenuProcedure=str(), pmp=str(),
          replacePanel=str(), rp=str(), tearOff=bool(), to=bool(), tearOffCopy=str(), toc=str(), tearOffRestore=bool(),
          tor=bool(), unParent=bool(), up=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def paneLayout(activeFrameThickness=int(), aft=int(), activePane=str(), ap=str(), activePaneIndex=int(), api=int(),
               annotation=str(), ann=str(), backgroundColor=list, bgc=list, childArray=bool(), ca=bool(),
               configuration=str(), cn=str(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
               dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
               enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
               fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(),
               io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), numberOfChildren=bool(), nch=bool(),
               numberOfPopupMenus=bool(), npm=bool(), numberOfVisiblePanes=bool(), nvp=bool(), pane1=bool(), p1=bool(),
               pane2=bool(), p2=bool(), pane3=bool(), p3=bool(), pane4=bool(), p4=bool(), paneSize=list, ps=list,
               paneUnderPointer=bool(), pup=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
               preventOverride=bool(), po=bool(), separatorMovedCommand=str(), smc=str(), separatorThickness=int(),
               st=int(), setPane=list, sp=list, staticHeightPane=int(), shp=int(), staticWidthPane=int(), swp=int(),
               statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
               visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def panelConfiguration(addPanel=list, ap=list, configString=str(), cfs=str(), createStrings=bool(), cs=bool(),
                       defaultImage=str(), di=str(), defineTemplate=str(), dt=str(), editStrings=bool(), es=bool(),
                       exists=bool(), ex=bool(), image=str(), i=str(), isFixedState=bool(), label=str(), l=str(),
                       labelStrings=bool(), ls=bool(), numberOfPanels=bool(), np=bool(), removeAllPanels=bool(),
                       rap=bool(), removeLastPanel=bool(), rlp=bool(), replaceCreateString=list, rcs=list,
                       replaceEditString=list, res=list, replaceFixedState=list, rfs=list, replaceLabel=list, rl=list,
                       replacePanel=list, rp=list, replaceTypeString=list, rts=list, sceneConfig=bool(), sc=bool(),
                       typeStrings=bool(), ts=bool(), useTemplate=str(), ut=str(), userCreated=bool(), uc=bool(), *args,
                       **kwargs):
    pass


def panelHistory(back=bool(), b=bool(), clear=bool(), cl=bool(), defineTemplate=str(), dt=str(), exists=bool(),
                 ex=bool(), forward=bool(), f=bool(), historyDepth=int(), hd=int(), isEmpty=bool(), ie=bool(),
                 suspend=bool(), s=bool(), targetPane=str(), tp=str(), useTemplate=str(), ut=str(), wrap=bool(),
                 w=bool(), *args, **kwargs):
    pass


def panZoom(absolute=bool(), abs=bool(), downDistance=float(), d=float(), leftDistance=float(), l=float(),
            relative=bool(), rel=bool(), rightDistance=float(), r=float(), upDistance=float(), u=float(),
            zoomRatio=float(), z=float(), *args, **kwargs):
    pass


def panZoomCtx(alternateContext=bool(), ac=bool(), buttonDown=bool(), btd=bool(), buttonUp=bool(), btu=bool(),
               exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
               image3=str(), i3=str(), name=str(), n=str(), panMode=bool(), pm=bool(), toolName=str(), tn=str(),
               zoomMode=bool(), zm=bool(), zoomScale=float(), zs=float(), *args, **kwargs):
    pass


def paramDimContext(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                    image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def paramDimension(*args, **kwargs):
    pass


def paramLocator(position=bool(), p=bool(), *args, **kwargs):
    pass


def parent(absolute=bool(), a=bool(), addObject=bool(), add=bool(), noConnections=bool(), nc=bool(), noInvScale=bool(),
           nis=bool(), relative=bool(), r=bool(), removeObject=bool(), rm=bool(), shape=bool(), s=bool(), world=bool(),
           w=bool(), *args, **kwargs):
    pass


def parentConstraint(createCache=list, cc=list, decompRotationToChild=bool(), dr=bool(), deleteCache=bool(), dc=bool(),
                     layer=str(), l=str(), maintainOffset=bool(), mo=bool(), name=str(), n=str(), remove=bool(),
                     rm=bool(), skipRotate=str(), sr=str(), skipTranslate=str(), st=str(), targetList=bool(), tl=bool(),
                     weight=float(), w=float(), weightAliasList=bool(), wal=bool(), *args, **kwargs):
    pass


def particle(attribute=str(), at=str(), cache=bool(), ch=bool(), conserve=float(), c=float(), count=bool(), ct=bool(),
             deleteCache=bool(), dc=bool(), dynamicAttrList=bool(), dal=bool(), floatValue=float(), fv=float(),
             gridSpacing=float(), grs=float(), inherit=float(), i=float(), jitterBasePoint=list, jbp=list,
             jitterRadius=float(), jr=float(), lowerLeft=list, ll=list, name=str(), n=str(), numJitters=int(), nj=int(),
             order=int(), particleId=int(), id=int(), perParticleDouble=bool(), ppd=bool(), perParticleVector=bool(),
             ppv=bool(), position=list, p=list, shapeName=str(), sn=str(), upperRight=list, ur=list, vectorValue=list,
             vv=list, *args, **kwargs):
    pass


def particleExists(*args, **kwargs):
    pass


def particleFill(closePacking=bool(), cp=bool(), doubleWalled=bool(), dw=bool(), maxX=float(), mxx=float(),
                 maxY=float(), mxy=float(), maxZ=float(), mxz=float(), minX=float(), mnx=float(), minY=float(),
                 mny=float(), minZ=float(), mnz=float(), particleDensity=float(), pd=float(), resolution=int(),
                 rs=int(), *args, **kwargs):
    pass


def particleInstancer(addObject=bool(), a=bool(), aimAxis=str(), aa=str(), aimDirection=str(), ad=str(),
                      aimPosition=str(), ap=str(), aimUpAxis=str(), aua=str(), aimWorldUp=str(), awu=str(),
                      attributeMapping=bool(), am=bool(), cycle=str(), c=str(), cycleStartObject=str(), sto=str(),
                      cycleStep=float(), cs=float(), cycleStepUnits=str(), csu=str(), index=int(), i=int(),
                      instanceId=str(), id=str(), levelOfDetail=str(), lod=str(), name=str(), n=str(), object=str(),
                      obj=str(), objectIndex=str(), oi=str(), particleAge=str(), age=str(), position=str(), p=str(),
                      removeObject=bool(), rm=bool(), rotation=str(), r=str(), rotationOrder=str(), ro=str(),
                      rotationType=str(), rt=str(), rotationUnits=str(), ru=str(), scale=str(), sc=str(), shear=str(),
                      sh=str(), visibility=str(), vis=str(), *args, **kwargs):
    pass


def particleRenderInfo(attrList=int(), al=int(), attrListAll=bool(), ala=bool(), name=int(), n=int(),
                       renderTypeCount=bool(), rtc=bool(), *args, **kwargs):
    pass


def partition(addSet=str(), add=str(), name=str(), n=str(), removeSet=str(), rm=str(), render=bool(), re=bool(), *args,
              **kwargs):
    pass


def pasteKey(animLayer=str(), al=str(), animation=str(), an=str(), attribute=str(), at=str(), clipboard=str(), cb=str(),
             connect=bool(), c=bool(), copies=int(), cp=int(), float=tuple(), f=tuple(), floatOffset=float(),
             fo=float(), includeUpperBound=bool(), iub=bool(), index=int(), matchByName=bool(), mn=bool(), option=str(),
             o=str(), time=tuple(), t=tuple(), timeOffset=float(), to=float(), valueOffset=float(), vo=float(), *args,
             **kwargs):
    pass


def pathAnimation(bank=bool(), b=bool(), bankScale=float(), bs=float(), bankThreshold=float(), bt=float(), curve=str(),
                  c=str(), endTimeU=float(), etu=float(), endU=float(), eu=float(), follow=bool(), f=bool(),
                  followAxis=str(), fa=str(), fractionMode=bool(), fm=bool(), inverseFront=bool(), inverseUp=bool(),
                  iu=bool(), name=str(), n=str(), startTimeU=float(), stu=float(), startU=float(), su=float(),
                  upAxis=str(), ua=str(), useNormal=bool(), un=bool(), worldUpObject=str(), wuo=str(),
                  worldUpType=str(), wut=str(), worldUpVector=list, wu=list, *args, **kwargs):
    pass


def pause(seconds=int(), sec=int(), *args, **kwargs):
    pass


def perCameraVisibility(camera=str(), c=str(), exclusive=bool(), ex=bool(), hide=bool(), hi=bool(), remove=bool(),
                        rm=bool(), removeAll=bool(), ra=bool(), removeCamera=bool(), rc=bool(), *args, **kwargs):
    pass


def percent(addPercent=bool(), ap=bool(), dropoffAxis=list, dax=list, dropoffCurve=str(), dc=str(),
            dropoffDistance=float(), dds=float(), dropoffPosition=list, dp=list, dropoffType=str(), dt=str(),
            multiplyPercent=bool(), mp=bool(), value=float(), v=float(), *args, **kwargs):
    pass


def performanceOptions(clusterResolution=float(), cr=float(), disableStitch=str(), ds=str(),
                       disableTrimBoundaryDisplay=str(), dtb=str(), disableTrimDisplay=str(), dt=str(),
                       latticeResolution=float(), lr=float(), passThroughBindSkinAndFlexors=str(), pbf=str(),
                       passThroughBlendShape=str(), pbs=str(), passThroughCluster=str(), pc=str(),
                       passThroughDeltaMush=str(), pdm=str(), passThroughFlexors=str(), pf=str(),
                       passThroughLattice=str(), pl=str(), passThroughPaintEffects=str(), pp=str(),
                       passThroughSculpt=str(), ps=str(), passThroughWire=str(), pw=str(),
                       skipHierarchyTraversal=bool(), sht=bool(), useClusterResolution=str(), ucr=str(),
                       useLatticeResolution=str(), ulr=str(), *args, **kwargs):
    pass


def pfxstrokes(filename=str(), fn=str(), postCallback=bool(), pc=bool(), selected=bool(), sl=bool(), *args, **kwargs):
    pass


def pickWalk(direction=str(), d=str(), recurse=bool(), r=bool(), type=str(), typ=str(), *args, **kwargs):
    pass


def picture(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(), docTag=str(),
            dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
            enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
            fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, image=str(), i=str(),
            isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
            numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
            preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(), tile=bool(), tl=bool(),
            useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(),
            w=int(), *args, **kwargs):
    pass


def pixelMove(*args, **kwargs):
    pass


def planarSrf(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), degree=int(), d=int(),
              keepOutside=bool(), ko=bool(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(),
              polygon=int(), po=int(), range=bool(), rn=bool(), tolerance=float(), tol=float(), *args, **kwargs):
    pass


def plane(length=float(), l=float(), name=str(), n=str(), position=list, p=list, rotation=list, r=list, size=float(),
          s=float(), width=float(), w=float(), *args, **kwargs):
    pass


def play(forward=bool(), f=bool(), playSound=bool(), ps=bool(), record=bool(), rec=bool(), sound=str(), s=str(),
         state=bool(), st=bool(), wait=bool(), w=bool(), *args, **kwargs):
    pass


def playbackOptions(animationEndTime=float(), aet=float(), animationStartTime=float(), ast=float(), blockingAnim=bool(),
                    ba=bool(), by=float(), framesPerSecond=bool(), fps=bool(), loop=str(), l=str(),
                    maxPlaybackSpeed=float(), mps=float(), maxTime=float(), max=float(), minTime=float(), min=float(),
                    playbackSpeed=float(), ps=float(), stepLoop=bool(), slp=bool(), view=str(), v=str(), *args,
                    **kwargs):
    pass


def playblast(activeEditor=bool(), ae=bool(), cameraSetup=list, cs=list, clearCache=bool(), cc=bool(),
              codecOptions=bool(), co=bool(), combineSound=bool(), csd=bool(), completeFilename=str(), cf=str(),
              compression=str(), c=str(), editorPanelName=str(), epn=str(), endTime=float(), et=float(), filename=str(),
              f=str(), forceOverwrite=bool(), fo=bool(), format=str(), fmt=str(), frame=float(), fr=float(),
              framePadding=int(), fp=int(), height=int(), h=int(), indexFromZero=bool(), ifz=bool(), offScreen=bool(),
              os=bool(), offScreenViewportUpdate=bool(), osv=bool(), options=bool(), o=bool(), percent=int(), p=int(),
              quality=int(), qlt=int(), rawFrameNumbers=bool(), rfn=bool(), replaceAudioOnly=bool(), rao=bool(),
              replaceEndTime=float(), ret=float(), replaceFilename=str(), rf=str(), replaceStartTime=float(),
              rst=float(), sequenceTime=bool(), sqt=bool(), showOrnaments=bool(), orn=bool(), sound=str(), s=str(),
              startTime=float(), st=float(), throwOnError=bool(), toe=bool(), useTraxSounds=bool(), uts=bool(),
              viewer=bool(), v=bool(), width=int(), w=int(), widthHeight=list, wh=list, *args, **kwargs):
    pass


def pluginDisplayFilter(classification=str(), cls=str(), deregister=bool(), dr=bool(), exists=bool(), ex=bool(),
                        label=str(), l=str(), listFilters=bool(), lf=bool(), register=bool(), r=bool(), *args,
                        **kwargs):
    pass


def pluginInfo(activeFile=bool(), af=bool(), allEvaluators=bool(), ae=bool(), animCurveInterp=str(), aci=str(),
               apiVersion=bool(), av=bool(), autoload=bool(), a=bool(), cacheFormat=bool(), cf=bool(),
               changedCommand=str(), cc=str(), command=str(), c=str(), constraintCommand=bool(), cnc=bool(),
               controlCommand=bool(), ctc=bool(), data=list, d=list, dependNode=bool(), dn=bool(),
               dependNodeByType=str(), dnt=str(), dependNodeId=str(), dni=str(), device=bool(), dv=bool(),
               dragAndDropBehavior=bool(), ddb=bool(), evaluator=bool(), e=bool(), iksolver=bool(), ik=bool(),
               listPlugins=bool(), ls=bool(), listPluginsPath=bool(), lsp=bool(), loadPluginPrefs=bool(), lpp=bool(),
               loaded=bool(), l=bool(), modelEditorCommand=bool(), mec=bool(), name=str(), n=str(), path=str(), p=str(),
               pluginsInUse=bool(), pu=bool(), referenceTranslators=bool(), rtr=bool(), registered=bool(), r=bool(),
               remove=bool(), rm=bool(), renderer=bool(), rdr=bool(), savePluginPrefs=bool(), spp=bool(),
               serviceDescriptions=bool(), sd=bool(), settings=bool(), set=bool(), tool=str(), t=str(),
               translator=bool(), tr=bool(), unloadOk=bool(), uo=bool(), userNamed=bool(), u=bool(), vendor=str(),
               vd=str(), version=bool(), v=bool(), writeRequires=bool(), wr=bool(), *args, **kwargs):
    pass


def pointConstraint(layer=str(), l=str(), maintainOffset=bool(), mo=bool(), name=str(), n=str(), offset=list, o=list,
                    remove=bool(), rm=bool(), skip=str(), sk=str(), targetList=bool(), tl=bool(), weight=float(),
                    w=float(), weightAliasList=bool(), wal=bool(), *args, **kwargs):
    pass


def pointCurveConstraint(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                         nodeState=int(), nds=int(), object=bool(), o=bool(), pointConstraintUVW=list, puv=list,
                         pointWeight=float(), pw=float(), position=list, p=list, replaceOriginal=bool(), rpo=bool(),
                         weight=float(), w=float(), *args, **kwargs):
    pass


def pointLight(decayRate=int(), d=int(), discRadius=float(), drs=float(), exclusive=bool(), exc=bool(),
               intensity=float(), i=float(), name=str(), n=str(), position=list, pos=list, rgb=list, rotation=list,
               rot=list, shadowColor=list, sc=list, shadowDither=float(), sd=float(), shadowSamples=int(), sh=int(),
               softShadow=bool(), ss=bool(), useRayTraceShadows=bool(), rs=bool(), *args, **kwargs):
    pass


def pointOnCurve(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), curvatureCenter=bool(), cc=bool(),
                 curvatureRadius=bool(), cr=bool(), nodeState=int(), nds=int(), normal=bool(), no=bool(),
                 normalizedNormal=bool(), nn=bool(), normalizedTangent=bool(), nt=bool(), parameter=float(), pr=float(),
                 position=bool(), p=bool(), tangent=bool(), t=bool(), turnOnPercentage=bool(), top=bool(), *args,
                 **kwargs):
    pass


def pointOnPolyConstraint(layer=str(), l=str(), maintainOffset=bool(), mo=bool(), name=str(), n=str(), offset=list,
                          o=list, remove=bool(), rm=bool(), skip=str(), sk=str(), targetList=bool(), tl=bool(),
                          weight=float(), w=float(), weightAliasList=bool(), wal=bool(), *args, **kwargs):
    pass


def pointOnSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), nodeState=int(), nds=int(),
                   normal=bool(), no=bool(), normalizedNormal=bool(), nn=bool(), normalizedTangentU=bool(), ntu=bool(),
                   normalizedTangentV=bool(), ntv=bool(), parameterU=float(), u=float(), parameterV=float(), v=float(),
                   position=bool(), p=bool(), tangentU=bool(), tu=bool(), tangentV=bool(), tv=bool(),
                   turnOnPercentage=bool(), top=bool(), *args, **kwargs):
    pass


def pointPosition(local=bool(), l=bool(), world=bool(), w=bool(), *args, **kwargs):
    pass


def poleVectorConstraint(layer=str(), l=str(), name=str(), n=str(), remove=bool(), rm=bool(), targetList=bool(),
                         tl=bool(), weight=float(), w=float(), weightAliasList=bool(), wal=bool(), *args, **kwargs):
    pass


def polyAppend(append=list, a=list, constructionHistory=bool(), ch=bool(), edge=int(), ed=int(), hole=bool(), hl=bool(),
               name=str(), n=str(), point=list, p=list, subdivision=int(), s=int(), texture=int(), tx=int(), *args,
               **kwargs):
    pass


def polyAppendFacetCtx(append=bool(), ap=bool(), exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(),
                       i2=str(), image3=str(), i3=str(), isRotateAvailable=bool(), isr=bool(),
                       maximumNumberOfPoints=int(), mp=int(), planarConstraint=bool(), pc=bool(), rotate=float(),
                       r=float(), subdivision=int(), s=int(), texture=int(), tx=int(), *args, **kwargs):
    pass


def polyAppendVertex(append=list, a=list, constructionHistory=bool(), ch=bool(), hole=bool(), h=bool(), name=str(),
                     n=str(), point=list, p=list, texture=int(), tx=int(), vertex=int(), v=int(), *args, **kwargs):
    pass


def polyAutoProjection(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createNewMap=bool(),
                       cm=bool(), insertBeforeDeformers=bool(), ibd=bool(), layout=int(), l=int(), layoutMethod=int(),
                       lm=int(), name=str(), n=str(), nodeState=int(), nds=int(), optimize=int(), o=int(),
                       percentageSpace=float(), ps=float(), pivot=list, pvt=list, pivotX=float(), pvx=float(),
                       pivotY=float(), pvy=float(), pivotZ=float(), pvz=float(), planes=int(), p=int(),
                       projectBothDirections=bool(), pb=bool(), rotate=list, ro=list, rotateX=float(), rx=float(),
                       rotateY=float(), ry=float(), rotateZ=float(), rz=float(), scale=list, s=list, scaleMode=int(),
                       sc=int(), scaleX=float(), sx=float(), scaleY=float(), sy=float(), scaleZ=float(), sz=float(),
                       skipIntersect=bool(), si=bool(), translate=list, t=list, translateX=float(), tx=float(),
                       translateY=float(), ty=float(), translateZ=float(), tz=float(), uvSetName=str(), uvs=str(),
                       worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyAverageNormal(allowZeroNormal=bool(), azn=bool(), distance=float(), d=float(), postnormalize=bool(), pon=bool(),
                      prenormalize=bool(), prn=bool(), replaceNormalXYZ=list, xyz=list, *args, **kwargs):
    pass


def polyAverageVertex(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), iterations=int(), i=int(),
                      name=str(), n=str(), nodeState=int(), nds=int(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyBevel(angleTolerance=float(), at=float(), autoFit=bool(), af=bool(), caching=bool(), cch=bool(),
              constructionHistory=bool(), ch=bool(), mergeVertexTolerance=float(), mvt=float(), mergeVertices=bool(),
              mv=bool(), miteringAngle=float(), ma=float(), name=str(), n=str(), nodeState=int(), nds=int(),
              offset=float(), o=float(), offsetAsFraction=bool(), oaf=bool(), roundness=float(), r=float(),
              segments=int(), sg=int(), smoothingAngle=float(), sa=float(), subdivideNgons=bool(), sn=bool(),
              useLegacyBevelAlgorithm=bool(), com=bool(), uvAssignment=int(), ua=int(), worldSpace=bool(), ws=bool(),
              *args, **kwargs):
    pass


def polyBevel3(angleTolerance=float(), at=float(), autoFit=bool(), af=bool(), caching=bool(), cch=bool(),
               chamfer=bool(), c=bool(), constructionHistory=bool(), ch=bool(), depth=float(), d=float(),
               fillNgons=bool(), fn=bool(), mergeVertexTolerance=float(), mvt=float(), mergeVertices=bool(), mv=bool(),
               miterAlong=int(), mia=int(), mitering=int(), m=int(), miteringAngle=float(), ma=float(), name=str(),
               n=str(), nodeState=int(), nds=int(), offset=float(), o=float(), offsetAsFraction=bool(), oaf=bool(),
               roundness=float(), r=float(), segments=int(), sg=int(), smoothingAngle=float(), sa=float(),
               uvAssignment=int(), ua=int(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyBlendColor(baseColorName=str(), bcn=str(), blendFunc=int(), bfn=int(), blendWeightA=float(), bwa=float(),
                   blendWeightB=float(), bwb=float(), blendWeightC=float(), bwc=float(), blendWeightD=float(),
                   bwd=float(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), dstColorName=str(),
                   dst=str(), name=str(), n=str(), nodeState=int(), nds=int(), srcColorName=str(), src=str(), *args,
                   **kwargs):
    pass


def polyBlindData(associationType=str(), at=str(), binaryData=str(), bnd=str(), booleanData=bool(), bd=bool(),
                  delete=bool(), doubleData=float(), dbd=float(), int64Data=int(), lid=int(), intData=int(), ind=int(),
                  longDataName=str(), ldn=str(), rescan=bool(), res=bool(), reset=bool(), rst=bool(), shape=bool(),
                  sh=bool(), shortDataName=str(), sdn=str(), stringData=str(), sd=str(), typeId=int(), id=int(), *args,
                  **kwargs):
    pass


def polyBoolOp(caching=bool(), cch=bool(), faceAreaThreshold=float(), fat=float(), mergeUVSets=int(), muv=int(),
               nodeState=int(), nds=int(), operation=int(), op=int(), preserveColor=bool(), pcr=bool(),
               useThresholds=bool(), uth=bool(), vertexDistanceThreshold=float(), vdt=float(), *args, **kwargs):
    pass


def polyBridgeEdge(bridgeOffset=int(), bo=int(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                   curveType=int(), ctp=int(), divisions=int(), dv=int(), inputCurve=str(), inc=str(), name=str(),
                   n=str(), nodeState=int(), nds=int(), smoothingAngle=float(), sma=float(), startVert1=int(),
                   sv1=int(), startVert2=int(), sv2=int(), taper=float(), tp=float(), taperCurve_FloatValue=float(),
                   cfv=float(), taperCurve_Interp=int(), ci=int(), taperCurve_Position=float(), cp=float(),
                   twist=float(), twt=float(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyCacheMonitor(cacheValue=bool(), chv=bool(), nodeName=str(), nm=str(), *args, **kwargs):
    pass


def polyCanBridgeEdge(*args, **kwargs):
    pass


def polyCBoolOp(caching=bool(), cch=bool(), classification=int(), cls=int(), faceAreaThreshold=float(), fat=float(),
                mergeUVSets=int(), muv=int(), nodeState=int(), nds=int(), operation=int(), op=int(),
                preserveColor=bool(), pcr=bool(), useCarveBooleans=bool(), ucb=bool(), useThresholds=bool(), uth=bool(),
                vertexDistanceThreshold=float(), vdt=float(), *args, **kwargs):
    pass


def polyCheck(edge=bool(), e=bool(), face=bool(), f=bool(), faceOffset=bool(), fo=bool(), openFile=str(), of=str(),
              *args, **kwargs):
    pass


def polyChipOff(attraction=float(), att=float(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                duplicate=bool(), dup=bool(), gain=float(), ga=float(), gravity=list, g=list, gravityX=float(),
                gx=float(), gravityY=float(), gy=float(), gravityZ=float(), gz=float(), keepFacesTogether=bool(),
                kft=bool(), keepFacetTogether=bool(), xft=bool(), localCenter=int(), lc=int(), localDirection=list,
                ld=list, localDirectionX=float(), ldx=float(), localDirectionY=float(), ldy=float(),
                localDirectionZ=float(), ldz=float(), localRotate=list, lr=list, localRotateX=float(), lrx=float(),
                localRotateY=float(), lry=float(), localRotateZ=float(), lrz=float(), localScale=list, ls=list,
                localScaleX=float(), lsx=float(), localScaleY=float(), lsy=float(), localScaleZ=float(), lsz=float(),
                localTranslate=list, lt=list, localTranslateX=float(), ltx=float(), localTranslateY=float(),
                lty=float(), localTranslateZ=float(), ltz=float(), magnX=float(), mx=float(), magnY=float(), my=float(),
                magnZ=float(), mz=float(), magnet=list, m=list, name=str(), n=str(), nodeState=int(), nds=int(),
                offset=float(), off=float(), pivot=list, pvt=list, pivotX=float(), pvx=float(), pivotY=float(),
                pvy=float(), pivotZ=float(), pvz=float(), random=float(), ran=float(), scale=list, s=list,
                scaleX=float(), sx=float(), scaleY=float(), sy=float(), scaleZ=float(), sz=float(), translate=list,
                t=list, translateX=float(), tx=float(), translateY=float(), ty=float(), translateZ=float(), tz=float(),
                weight=float(), w=float(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyCircularize(alignment=int(), al=int(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                    createCurve=bool(), cc=bool(), evenlyDistribute=bool(), ed=bool(), inputCurve=str(), inc=str(),
                    name=str(), n=str(), nodeState=int(), nds=int(), normalOrientation=int(), nor=int(),
                    radialOffset=float(), ro=float(), smoothingAngle=float(), sa=float(), worldSpace=bool(), ws=bool(),
                    *args, **kwargs):
    pass


def polyCircularizeEdge(alignment=int(), al=int(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                        createCurve=bool(), cc=bool(), evenlyDistribute=bool(), ed=bool(), inputCurve=str(), inc=str(),
                        name=str(), n=str(), nodeState=int(), nds=int(), normalOrientation=int(), nor=int(),
                        radialOffset=float(), ro=float(), smoothingAngle=float(), sa=float(), worldSpace=bool(),
                        ws=bool(), *args, **kwargs):
    pass


def polyCircularizeFace(alignment=int(), al=int(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                        createCurve=bool(), cc=bool(), evenlyDistribute=bool(), ed=bool(), inputCurve=str(), inc=str(),
                        name=str(), n=str(), nodeState=int(), nds=int(), normalOrientation=int(), nor=int(),
                        radialOffset=float(), ro=float(), smoothingAngle=float(), sa=float(), worldSpace=bool(),
                        ws=bool(), *args, **kwargs):
    pass


def polyClean(caching=bool(), cch=bool(), cleanEdges=bool(), ce=bool(), cleanPartialUVMapping=bool(), cpm=bool(),
              cleanUVs=bool(), cuv=bool(), cleanVertices=bool(), cv=bool(), constructionHistory=bool(), ch=bool(),
              frozen=bool(), fzn=bool(), name=str(), n=str(), nodeState=int(), nds=int(), *args, **kwargs):
    pass


def polyClipboard(clear=bool(), cl=bool(), color=bool(), clr=bool(), copy=bool(), cp=bool(), paste=bool(), ps=bool(),
                  shader=bool(), sh=bool(), uvCoordinates=bool(), uv=bool(), *args, **kwargs):
    pass


def polyCloseBorder(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                    nodeState=int(), nds=int(), *args, **kwargs):
    pass


def polyCollapseEdge(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                     nodeState=int(), nds=int(), *args, **kwargs):
    pass


def polyCollapseFacet(areaThreshold=float(), at=float(), caching=bool(), cch=bool(), constructionHistory=bool(),
                      ch=bool(), name=str(), n=str(), nodeState=int(), nds=int(), useAreaThreshold=bool(), uat=bool(),
                      *args, **kwargs):
    pass


def polyCollapseTweaks(hasVertexTweaks=bool(), hvt=bool(), *args, **kwargs):
    pass


def polyColorBlindData(aboveMaxColorBlue=float(), amb=float(), aboveMaxColorGreen=float(), amg=float(),
                       aboveMaxColorRed=float(), amr=float(), attrName=str(), n=str(), belowMinColorBlue=float(),
                       bmb=float(), belowMinColorGreen=float(), bmg=float(), belowMinColorRed=float(), bmr=float(),
                       clashColorBlue=float(), ccb=float(), clashColorGreen=float(), ccg=float(), clashColorRed=float(),
                       ccr=float(), colorBlue=float(), cb=float(), colorGreen=float(), cg=float(), colorRed=float(),
                       cr=float(), dataType=str(), dt=str(), enableFalseColor=bool(), efc=bool(), maxColorBlue=float(),
                       mxb=float(), maxColorGreen=float(), mxg=float(), maxColorRed=float(), mxr=float(),
                       maxValue=float(), mxv=float(), minColorBlue=float(), mnb=float(), minColorGreen=float(),
                       mng=float(), minColorRed=float(), mnr=float(), minValue=float(), mnv=float(), mode=int(),
                       m=int(), noColorBlue=float(), ncb=float(), noColorGreen=float(), ncg=float(), noColorRed=float(),
                       ncr=float(), numIdTypes=int(), num=int(), queryMode=bool(), q=bool(), typeId=int(), id=int(),
                       useMax=bool(), umx=bool(), useMin=bool(), umn=bool(), value=str(), v=str(), *args, **kwargs):
    pass


def polyColorDel(caching=bool(), cch=bool(), colorSetName=str(), cls=str(), constructionHistory=bool(), ch=bool(),
                 name=str(), n=str(), nodeState=int(), nds=int(), *args, **kwargs):
    pass


def polyColorMod(alphaScale_FloatValue=float(), afv=float(), alphaScale_Interp=int(), ai=int(),
                 alphaScale_Position=float(), ap=float(), baseColorName=str(), bcn=str(), blueScale_FloatValue=float(),
                 bfv=float(), blueScale_Interp=int(), bi=int(), blueScale_Position=float(), bp=float(), caching=bool(),
                 cch=bool(), constructionHistory=bool(), ch=bool(), greenScale_FloatValue=float(), gfv=float(),
                 greenScale_Interp=int(), gi=int(), greenScale_Position=float(), gp=float(), huev=float(), h=float(),
                 intensityScale_FloatValue=float(), nfv=float(), intensityScale_Interp=int(), ni=int(),
                 intensityScale_Position=float(), np=float(), name=str(), n=str(), nodeState=int(), nds=int(),
                 redScale_FloatValue=float(), rfv=float(), redScale_Interp=int(), ri=int(), redScale_Position=float(),
                 rp=float(), satv=float(), s=float(), value=float(), v=float(), *args, **kwargs):
    pass


def polyColorPerVertex(alpha=float(), a=float(), clamped=bool(), cla=bool(), colorB=float(), b=float(),
                       colorDisplayOption=bool(), cdo=bool(), colorG=float(), g=float(), colorR=float(), r=float(),
                       colorRGB=list, rgb=list, notUndoable=bool(), nun=bool(), relative=bool(), rel=bool(),
                       remove=bool(), rem=bool(), representation=int(), rpt=int(), *args, **kwargs):
    pass


def polyColorSet(allColorSets=bool(), acs=bool(), clamped=bool(), cla=bool(), colorSet=str(), cs=str(), copy=bool(),
                 cp=bool(), create=bool(), cr=bool(), currentColorSet=bool(), ccs=bool(), currentPerInstanceSet=bool(),
                 cpi=bool(), delete=bool(), d=bool(), newColorSet=str(), nc=str(), perInstance=bool(), pi=bool(),
                 rename=bool(), rn=bool(), representation=str(), rpt=str(), shareInstances=bool(), si=bool(),
                 unshared=bool(), us=bool(), *args, **kwargs):
    pass


def polyCompare(colorSetIndices=bool(), ic=bool(), colorSets=bool(), c=bool(), edges=bool(), e=bool(), faceDesc=bool(),
                fd=bool(), userNormals=bool(), un=bool(), uvSetIndices=bool(), iuv=bool(), uvSets=bool(), uv=bool(),
                vertices=bool(), v=bool(), *args, **kwargs):
    pass


def polyCone(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createUVs=int(),
             cuv=int(), height=float(), h=float(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(),
             o=bool(), radius=float(), r=float(), roundCap=bool(), rcp=bool(), subdivisionsAxis=int(), sa=int(),
             subdivisionsCap=int(), sc=int(), subdivisionsHeight=int(), sh=int(), subdivisionsX=int(), sx=int(),
             subdivisionsY=int(), sy=int(), subdivisionsZ=int(), sz=int(), texture=bool(), tx=bool(), *args, **kwargs):
    pass


def polyConnectComponents(adjustEdgeFlow=float(), aef=float(), caching=bool(), cch=bool(), constructionHistory=bool(),
                          ch=bool(), insertWithEdgeFlow=bool(), ief=bool(), name=str(), n=str(), nodeState=int(),
                          nds=int(), *args, **kwargs):
    pass


def polyContourProjection(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createNewMap=bool(),
                          cm=bool(), flipRails=bool(), fr=bool(), insertBeforeDeformers=bool(), ibd=bool(),
                          method=int(), m=int(), name=str(), n=str(), nodeState=int(), nds=int(), offset0=float(),
                          o0=float(), offset1=float(), o1=float(), offset2=float(), o2=float(), offset3=float(),
                          o3=float(), reduceShear=float(), rs=float(), smoothness0=float(), s0=float(),
                          smoothness1=float(), s1=float(), smoothness2=float(), s2=float(), smoothness3=float(),
                          s3=float(), userDefinedCorners=bool(), udc=bool(), uvSetName=str(), uvs=str(),
                          worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyCopyUV(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createNewMap=bool(), cm=bool(),
               name=str(), n=str(), nodeState=int(), nds=int(), uvSetName=str(), uvs=str(), uvSetNameInput=str(),
               uvi=str(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyCrease(createHistory=bool(), ch=bool(), operation=int(), op=int(), relativeValue=float(), rv=float(),
               value=float(), v=float(), vertexValue=float(), vv=float(), *args, **kwargs):
    pass


def polyCreaseCtx(createSet=str(), cs=str(), exists=bool(), ex=bool(), extendSelection=bool(), es=bool(), image1=str(),
                  i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), relative=bool(), r=bool(), *args, **kwargs):
    pass


def polyCreateFacet(constructionHistory=bool(), ch=bool(), hole=bool(), hl=bool(), name=str(), n=str(), point=list,
                    p=list, subdivision=int(), s=int(), texture=int(), tx=int(), *args, **kwargs):
    pass


def polyCreateFacetCtx(append=bool(), ap=bool(), exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(),
                       i2=str(), image3=str(), i3=str(), maximumNumberOfPoints=int(), mp=int(), planarConstraint=bool(),
                       pc=bool(), subdivision=int(), s=int(), texture=int(), tx=int(), *args, **kwargs):
    pass


def polyCube(*obj_name, axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createUVs=int(),
             cuv=int(), depth=float(), d=float(), height=float(), h=float(), name=str(), n=str(), nodeState=int(),
             nds=int(), object=bool(), o=bool(), subdivisionsDepth=int(), sd=int(), subdivisionsHeight=int(), sh=int(),
             subdivisionsWidth=int(), sw=int(), subdivisionsX=int(), sx=int(), subdivisionsY=int(), sy=int(),
             subdivisionsZ=int(), sz=int(), texture=int(), tx=int(), width=float(), w=float(), **kwargs):

    trn = om.MFnDependencyNode().create('transform', name)
    shape = om.MFnDependencyNode().create('mesh', name + 'Shape')
    builder = om.MFnDependencyNode().create('polyCube', 'polyCube1')
    
    trn._children.append(shape)
    shape._parent = weakref.proxy(trn)
    shape._buider = builder
    return trn._name, shape._name

def polyCut(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), cutPlaneCenter=list, pc=list,
            cutPlaneCenterX=float(), pcx=float(), cutPlaneCenterY=float(), pcy=float(), cutPlaneCenterZ=float(),
            pcz=float(), cutPlaneHeight=float(), ph=float(), cutPlaneRotate=list, ro=list, cutPlaneRotateX=float(),
            rx=float(), cutPlaneRotateY=float(), ry=float(), cutPlaneRotateZ=float(), rz=float(), cutPlaneSize=list,
            ps=list, cutPlaneWidth=float(), pw=float(), cuttingDirection=str(), cd=str(), deleteFaces=bool(), df=bool(),
            extractFaces=bool(), ef=bool(), extractOffset=list, eo=list, extractOffsetX=float(), eox=float(),
            extractOffsetY=float(), eoy=float(), extractOffsetZ=float(), eoz=float(), name=str(), n=str(),
            nodeState=int(), nds=int(), onObject=bool(), oo=bool(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyCutCtx(deleteFaces=bool(), df=bool(), exists=bool(), ex=bool(), extractFaces=bool(), ef=bool(),
               extractOffset=list, eo=list, image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
               *args, **kwargs):
    pass


def polyCutUVCtx(loopSpeed=int(), ls=int(), mapBordersColor=list, mbc=list, showCheckerMap=bool(), scm=bool(),
                 showTextureBorders=bool(), stb=bool(), showUVShellColoring=bool(), ssc=bool(), steadyStroke=bool(),
                 ss=bool(), steadyStrokeDistance=float(), ssd=float(), symmetry=int(), sym=int(), *args, **kwargs):
    pass


def polyCylinder(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createUVs=int(),
                 cuv=int(), height=float(), h=float(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(),
                 o=bool(), radius=float(), r=float(), roundCap=bool(), rcp=bool(), subdivisionsAxis=int(), sa=int(),
                 subdivisionsCaps=int(), sc=int(), subdivisionsHeight=int(), sh=int(), subdivisionsX=int(), sx=int(),
                 subdivisionsY=int(), sy=int(), subdivisionsZ=int(), sz=int(), texture=int(), tx=int(), *args,
                 **kwargs):
    pass


def polyCylindricalProjection(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createNewMap=bool(),
                              cm=bool(), imageCenter=list, ic=list, imageCenterX=float(), icx=float(),
                              imageCenterY=float(), icy=float(), imageScale=list, imageScaleU=float(), isu=float(),
                              imageScaleV=float(), isv=float(), insertBeforeDeformers=bool(), ibd=bool(),
                              keepImageRatio=bool(), kir=bool(), mapDirection=str(), md=str(), name=str(), n=str(),
                              nodeState=int(), nds=int(), perInstance=bool(), pi=bool(), projectionCenter=list, pc=list,
                              projectionCenterX=float(), pcx=float(), projectionCenterY=float(), pcy=float(),
                              projectionCenterZ=float(), pcz=float(), projectionHeight=float(), ph=float(),
                              projectionHorizontalSweep=float(), phs=float(), projectionScale=list, ps=list,
                              projectionScaleU=float(), psu=float(), projectionScaleV=float(), psv=float(),
                              radius=float(), r=float(), rotationAngle=float(), ra=float(), seamCorrect=bool(),
                              sc=bool(), smartFit=bool(), sf=bool(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyDelEdge(caching=bool(), cch=bool(), cleanVertices=bool(), cv=bool(), constructionHistory=bool(), ch=bool(),
                name=str(), n=str(), nodeState=int(), nds=int(), *args, **kwargs):
    pass


def polyDelFacet(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                 nodeState=int(), nds=int(), *args, **kwargs):
    pass


def polyDelVertex(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                  nodeState=int(), nds=int(), *args, **kwargs):
    pass


def polyDuplicateAndConnect(removeOriginalFromShaders=bool(), ros=bool(), renameChildren=bool(), rc=bool(), *args,
                            **kwargs):
    pass


def polyDuplicateEdge(adjustEdgeFlow=float(), aef=float(), caching=bool(), cch=bool(), constructionHistory=bool(),
                      ch=bool(), deleteEdge=bool(), de=bool(), endVertexOffset=float(), evo=float(),
                      insertWithEdgeFlow=bool(), ief=bool(), name=str(), n=str(), nodeState=int(), nds=int(),
                      offset=float(), of=float(), smoothingAngle=float(), sma=float(), splitType=int(), stp=int(),
                      startVertexOffset=float(), svo=float(), *args, **kwargs):
    pass


def polyEditEdgeFlow(adjustEdgeFlow=float(), aef=float(), caching=bool(), cch=bool(), constructionHistory=bool(),
                     ch=bool(), edgeFlow=bool(), ef=bool(), name=str(), n=str(), nodeState=int(), nds=int(), *args,
                     **kwargs):
    pass


def polyEditUV(angle=float(), a=float(), pivotU=float(), pu=float(), pivotV=float(), pv=float(), relative=bool(),
               r=bool(), rotateRatio=float(), rr=float(), rotation=bool(), rot=bool(), scale=bool(), s=bool(),
               scaleU=float(), su=float(), scaleV=float(), sv=float(), uValue=float(), u=float(), uvSetName=str(),
               uvs=str(), vValue=float(), v=float(), *args, **kwargs):
    pass


def polyEditUVShell(angle=float(), a=float(), pivotU=float(), pu=float(), pivotV=float(), pv=float(), relative=bool(),
                    r=bool(), rotateRatio=float(), rr=float(), rotation=bool(), rot=bool(), scale=bool(), s=bool(),
                    scaleU=float(), su=float(), scaleV=float(), sv=float(), uValue=float(), u=float(), uvSetName=str(),
                    uvs=str(), vValue=float(), v=float(), *args, **kwargs):
    pass


def polyEvaluate(accurateEvaluation=bool(), ae=bool(), activeShells=bool(), activeUVShells=bool(), aus=bool(),
                 area=bool(), a=bool(), boundingBox=bool(), b=bool(), boundingBox2d=bool(), b2=bool(),
                 boundingBoxComponent=bool(), bc=bool(), boundingBoxComponent2d=bool(), bc2=bool(), displayStats=bool(),
                 ds=bool(), edge=bool(), e=bool(), edgeComponent=bool(), ec=bool(), face=bool(), f=bool(),
                 faceArea=bool(), fa=bool(), faceComponent=bool(), fc=bool(), format=bool(), fmt=bool(), shell=bool(),
                 s=bool(), triangle=bool(), t=bool(), triangleComponent=bool(), tc=bool(), uvArea=bool(), uva=bool(),
                 uvComponent=bool(), uvc=bool(), uvEdgePairs=bool(), uep=bool(), uvFaceArea=bool(), ufa=bool(),
                 uvSetName=str(), uvs=str(), uvShell=bool(), us=bool(), uvShellIds=bool(), usi=bool(), uvcoord=bool(),
                 uv=bool(), uvsInShell=int(), uis=int(), vertex=bool(), v=bool(), vertexComponent=bool(), vc=bool(),
                 worldArea=bool(), wa=bool(), worldFaceArea=bool(), wfa=bool(), *args, **kwargs):
    pass


def polyExtrudeEdge(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createCurve=bool(), cc=bool(),
                    divisions=int(), d=int(), gain=float(), ga=float(), inputCurve=str(), inc=str(),
                    keepFacesTogether=bool(), kft=bool(), localCenter=int(), lc=int(), localDirection=list, ld=list,
                    localDirectionX=float(), ldx=float(), localDirectionY=float(), ldy=float(), localDirectionZ=float(),
                    ldz=float(), localRotate=list, lr=list, localRotateX=float(), lrx=float(), localRotateY=float(),
                    lry=float(), localRotateZ=float(), lrz=float(), localScale=list, ls=list, localScaleX=float(),
                    lsx=float(), localScaleY=float(), lsy=float(), localScaleZ=float(), lsz=float(),
                    localTranslate=list, lt=list, localTranslateX=float(), ltx=float(), localTranslateY=float(),
                    lty=float(), localTranslateZ=float(), ltz=float(), name=str(), n=str(), nodeState=int(), nds=int(),
                    offset=float(), off=float(), pivot=list, pvt=list, pivotX=float(), pvx=float(), pivotY=float(),
                    pvy=float(), pivotZ=float(), pvz=float(), random=float(), ran=float(), rotate=list, ro=list,
                    rotateX=float(), rx=float(), rotateY=float(), ry=float(), rotateZ=float(), rz=float(), scale=list,
                    s=list, scaleX=float(), sx=float(), scaleY=float(), sy=float(), scaleZ=float(), sz=float(),
                    smoothingAngle=float(), sma=float(), taper=float(), tp=float(), taperCurve_FloatValue=float(),
                    cfv=float(), taperCurve_Interp=int(), ci=int(), taperCurve_Position=float(), cp=float(),
                    thickness=float(), tk=float(), translate=list, t=list, translateX=float(), tx=float(),
                    translateY=float(), ty=float(), translateZ=float(), tz=float(), twist=float(), twt=float(),
                    worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyExtrudeFacet(attraction=float(), att=float(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                     createCurve=bool(), cc=bool(), divisions=int(), d=int(), gain=float(), ga=float(), gravity=list,
                     g=list, gravityX=float(), gx=float(), gravityY=float(), gy=float(), gravityZ=float(), gz=float(),
                     inputCurve=str(), inc=str(), keepFacesTogether=bool(), kft=bool(), keepFacetTogether=bool(),
                     xft=bool(), localCenter=int(), lc=int(), localDirection=list, ld=list, localDirectionX=float(),
                     ldx=float(), localDirectionY=float(), ldy=float(), localDirectionZ=float(), ldz=float(),
                     localRotate=list, lr=list, localRotateX=float(), lrx=float(), localRotateY=float(), lry=float(),
                     localRotateZ=float(), lrz=float(), localScale=list, ls=list, localScaleX=float(), lsx=float(),
                     localScaleY=float(), lsy=float(), localScaleZ=float(), lsz=float(), localTranslate=list, lt=list,
                     localTranslateX=float(), ltx=float(), localTranslateY=float(), lty=float(),
                     localTranslateZ=float(), ltz=float(), magnX=float(), mx=float(), magnY=float(), my=float(),
                     magnZ=float(), mz=float(), magnet=list, m=list, name=str(), n=str(), nodeState=int(), nds=int(),
                     offset=float(), off=float(), pivot=list, pvt=list, pivotX=float(), pvx=float(), pivotY=float(),
                     pvy=float(), pivotZ=float(), pvz=float(), random=float(), ran=float(), reverseAllFaces=bool(),
                     raf=bool(), rotate=list, ro=list, rotateX=float(), rx=float(), rotateY=float(), ry=float(),
                     rotateZ=float(), rz=float(), scale=list, s=list, scaleX=float(), sx=float(), scaleY=float(),
                     sy=float(), scaleZ=float(), sz=float(), smoothingAngle=float(), sma=float(), taper=float(),
                     tp=float(), taperCurve_FloatValue=float(), cfv=float(), taperCurve_Interp=int(), ci=int(),
                     taperCurve_Position=float(), cp=float(), thickness=float(), tk=float(), translate=list, t=list,
                     translateX=float(), tx=float(), translateY=float(), ty=float(), translateZ=float(), tz=float(),
                     twist=float(), twt=float(), weight=float(), w=float(), worldSpace=bool(), ws=bool(), *args,
                     **kwargs):
    pass


def polyExtrudeVertex(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), divisions=int(), d=int(),
                      length=float(), l=float(), name=str(), n=str(), nodeState=int(), nds=int(), width=float(),
                      w=float(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyFlipEdge(*args, **kwargs):
    pass


def polyFlipUV(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createNewMap=bool(), cm=bool(),
               cutUV=bool(), cut=bool(), flipType=int(), ft=int(), insertBeforeDeformers=bool(), ibd=bool(),
               local=bool(), l=bool(), name=str(), n=str(), nodeState=int(), nds=int(), pivotU=float(), pu=float(),
               pivotV=float(), pv=float(), usePivot=bool(), up=bool(), uvSetName=str(), uvs=str(), worldSpace=bool(),
               ws=bool(), *args, **kwargs):
    pass


def polyForceUV(cameraProjection=bool(), cp=bool(), createNewMap=bool(), cm=bool(), flipHorizontal=bool(), fh=bool(),
                flipVertical=bool(), fv=bool(), g=bool(), local=bool(), l=bool(), normalize=str(), nor=str(),
                numItems=int(), ni=int(), preserveAspectRatio=bool(), par=bool(), unitize=bool(), uni=bool(),
                unshare=bool(), u=bool(), uvSetName=str(), uvs=str(), *args, **kwargs):
    pass


def polyGeoSampler(alphaBlend=str(), abl=str(), averageColor=bool(), ac=bool(), clampAlphaMax=float(), amx=float(),
                   clampAlphaMin=float(), amn=float(), clampRGBMax=list, cmx=list, clampRGBMin=list, cmn=list,
                   colorBlend=str(), cbl=str(), colorDisplayOption=bool(), cdo=bool(), computeShadows=bool(), cs=bool(),
                   displaceGeometry=bool(), dg=bool(), flatShading=bool(), fs=bool(), ignoreDoubleSided=bool(),
                   ids=bool(), lightingOnly=bool(), lo=bool(), reuseShadows=bool(), rs=bool(), sampleByFace=bool(),
                   bf=bool(), scaleFactor=float(), sf=float(), shareUV=bool(), su=bool(), useLightShadows=bool(),
                   ul=bool(), *args, **kwargs):
    pass


def polyHelix(caching=bool(), cch=bool(), coils=float(), c=float(), constructionHistory=bool(), ch=bool(),
              createUVs=int(), cuv=int(), direction=int(), d=int(), height=float(), h=float(), name=str(), n=str(),
              nodeState=int(), nds=int(), object=bool(), o=bool(), radius=float(), r=float(), roundCap=bool(),
              rcp=bool(), subdivisionsAxis=int(), sa=int(), subdivisionsCaps=int(), sc=int(), subdivisionsCoil=int(),
              sco=int(), texture=int(), tx=int(), useOldInitBehaviour=bool(), oib=bool(), width=float(), w=float(),
              *args, **kwargs):
    pass


def polyHole(assignHole=bool(), ah=bool(), createHistory=bool(), ch=bool(), *args, **kwargs):
    pass


def polyInfo(edgeToFace=bool(), ef=bool(), edgeToVertex=bool(), ev=bool(), faceNormals=bool(), fn=bool(),
             faceToEdge=bool(), fe=bool(), faceToVertex=bool(), fv=bool(), invalidEdges=bool(), ie=bool(),
             invalidVertices=bool(), iv=bool(), laminaFaces=bool(), lf=bool(), nonManifoldEdges=bool(), nme=bool(),
             nonManifoldUVEdges=bool(), nue=bool(), nonManifoldUVs=bool(), nuv=bool(), nonManifoldVertices=bool(),
             nmv=bool(), vertexToEdge=bool(), ve=bool(), vertexToFace=bool(), vf=bool(), *args, **kwargs):
    pass


def polyInstallAction(commandName=bool(), cn=bool(), convertSelection=bool(), cs=bool(), installConstraint=bool(),
                      ic=bool(), installDisplay=bool(), id=bool(), keepInstances=bool(), ki=bool(),
                      uninstallConstraint=bool(), uc=bool(), uninstallDisplay=bool(), ud=bool(), *args, **kwargs):
    pass


def polyLayoutUV(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), flipReversed=bool(), fr=bool(),
                 layout=int(), l=int(), layoutMethod=int(), lm=int(), name=str(), n=str(), nodeState=int(), nds=int(),
                 percentageSpace=float(), ps=float(), rotateForBestFit=int(), rbf=int(), scale=int(), sc=int(),
                 separate=int(), se=int(), uvSetName=str(), uvs=str(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyListComponentConversion(border=bool(), bo=bool(), fromEdge=bool(), fe=bool(), fromFace=bool(), ff=bool(),
                                fromUV=bool(), fuv=bool(), fromVertex=bool(), fv=bool(), fromVertexFace=bool(),
                                fvf=bool(), internal=bool(), toEdge=bool(), te=bool(), toFace=bool(), tf=bool(),
                                toUV=bool(), tuv=bool(), toVertex=bool(), tv=bool(), toVertexFace=bool(), tvf=bool(),
                                uvShell=bool(), uvs=bool(), vertexFaceAllEdges=bool(), vfa=bool(), *args, **kwargs):
    pass


def polyMapCut(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), moveratio=float(), mvr=float(),
               name=str(), n=str(), nodeState=int(), nds=int(), *args, **kwargs):
    pass


def polyMapDel(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(), nodeState=int(),
               nds=int(), *args, **kwargs):
    pass


def polyMapSew(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(), nodeState=int(),
               nds=int(), *args, **kwargs):
    pass


def polyMapSewMove(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), limitPieceSize=bool(), lps=bool(),
                   name=str(), n=str(), nodeState=int(), nds=int(), numberFaces=int(), nf=int(), uvSetName=str(),
                   uvs=str(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyMergeEdge(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), firstEdge=int(), fe=int(),
                  mergeMode=int(), mm=int(), mergeTexture=bool(), mt=bool(), name=str(), n=str(), nodeState=int(),
                  nds=int(), secondEdge=int(), se=int(), *args, **kwargs):
    pass


def polyMergeEdgeCtx(activeNodes=bool(), anq=bool(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                     exists=bool(), ex=bool(), firstEdge=int(), fe=int(), image1=str(), i1=str(), image2=str(),
                     i2=str(), image3=str(), i3=str(), immediate=bool(), im=bool(), mergeMode=int(), mm=int(),
                     mergeTexture=bool(), mt=bool(), name=str(), n=str(), nodeState=int(), nds=int(), previous=bool(),
                     pv=bool(), reset=bool(), rs=bool(), secondEdge=int(), se=int(), toolNode=bool(), tnq=bool(), *args,
                     **kwargs):
    pass


def polyMergeFacet(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), firstFacet=int(), ff=int(),
                   mergeMode=int(), mm=int(), name=str(), n=str(), nodeState=int(), nds=int(), secondFacet=int(),
                   sf=int(), *args, **kwargs):
    pass


def polyMergeFacetCtx(activeNodes=bool(), anq=bool(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                      exists=bool(), ex=bool(), firstFacet=int(), ff=int(), image1=str(), i1=str(), image2=str(),
                      i2=str(), image3=str(), i3=str(), immediate=bool(), im=bool(), mergeMode=int(), mm=int(),
                      name=str(), n=str(), nodeState=int(), nds=int(), previous=bool(), pv=bool(), reset=bool(),
                      rs=bool(), secondFacet=int(), sf=int(), toolNode=bool(), tnq=bool(), *args, **kwargs):
    pass


def polyMergeUV(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), distance=float(), d=float(),
                name=str(), n=str(), nodeState=int(), nds=int(), uvSetName=str(), uvs=str(), worldSpace=bool(),
                ws=bool(), *args, **kwargs):
    pass


def polyMergeVertex(alwaysMergeTwoVertices=bool(), am=bool(), caching=bool(), cch=bool(), constructionHistory=bool(),
                    ch=bool(), distance=float(), d=float(), mergeToComponents=str(), mtc=str(), name=str(), n=str(),
                    nodeState=int(), nds=int(), texture=bool(), tx=bool(), worldSpace=bool(), ws=bool(), *args,
                    **kwargs):
    pass


def polyMirrorFace(axis=int(), a=int(), axisDirection=int(), ad=int(), caching=bool(), cch=bool(),
                   constructionHistory=bool(), ch=bool(), direction=int(), d=int(), mergeMode=int(), mm=int(),
                   mergeThreshold=float(), mt=float(), mergeThresholdType=int(), mtt=int(), mirrorAxis=int(), ma=int(),
                   mirrorPosition=float(), mps=float(), name=str(), n=str(), nodeState=int(), nds=int(), pivot=list,
                   p=list, pivotX=float(), px=float(), pivotY=float(), py=float(), pivotZ=float(), pz=float(),
                   worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyMoveEdge(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), gain=float(), ga=float(),
                 localCenter=int(), lc=int(), localDirection=list, ld=list, localDirectionX=float(), ldx=float(),
                 localDirectionY=float(), ldy=float(), localDirectionZ=float(), ldz=float(), localRotate=list, lr=list,
                 localRotateX=float(), lrx=float(), localRotateY=float(), lry=float(), localRotateZ=float(),
                 lrz=float(), localScale=list, ls=list, localScaleX=float(), lsx=float(), localScaleY=float(),
                 lsy=float(), localScaleZ=float(), lsz=float(), localTranslate=list, lt=list, localTranslateX=float(),
                 ltx=float(), localTranslateY=float(), lty=float(), localTranslateZ=float(), ltz=float(), name=str(),
                 n=str(), nodeState=int(), nds=int(), pivot=list, pvt=list, pivotX=float(), pvx=float(), pivotY=float(),
                 pvy=float(), pivotZ=float(), pvz=float(), random=float(), ran=float(), rotate=list, ro=list,
                 rotateX=float(), rx=float(), rotateY=float(), ry=float(), rotateZ=float(), rz=float(), scale=list,
                 s=list, scaleX=float(), sx=float(), scaleY=float(), sy=float(), scaleZ=float(), sz=float(),
                 translate=list, t=list, translateX=float(), tx=float(), translateY=float(), ty=float(),
                 translateZ=float(), tz=float(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyMoveFacet(attraction=float(), att=float(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                  gain=float(), ga=float(), gravity=list, g=list, gravityX=float(), gx=float(), gravityY=float(),
                  gy=float(), gravityZ=float(), gz=float(), localCenter=int(), lc=int(), localDirection=list, ld=list,
                  localDirectionX=float(), ldx=float(), localDirectionY=float(), ldy=float(), localDirectionZ=float(),
                  ldz=float(), localRotate=list, lr=list, localRotateX=float(), lrx=float(), localRotateY=float(),
                  lry=float(), localRotateZ=float(), lrz=float(), localScale=list, ls=list, localScaleX=float(),
                  lsx=float(), localScaleY=float(), lsy=float(), localScaleZ=float(), lsz=float(), localTranslate=list,
                  lt=list, localTranslateX=float(), ltx=float(), localTranslateY=float(), lty=float(),
                  localTranslateZ=float(), ltz=float(), magnX=float(), mx=float(), magnY=float(), my=float(),
                  magnZ=float(), mz=float(), magnet=list, m=list, name=str(), n=str(), nodeState=int(), nds=int(),
                  offset=float(), off=float(), pivot=list, pvt=list, pivotX=float(), pvx=float(), pivotY=float(),
                  pvy=float(), pivotZ=float(), pvz=float(), random=float(), ran=float(), rotate=list, ro=list,
                  rotateX=float(), rx=float(), rotateY=float(), ry=float(), rotateZ=float(), rz=float(), scale=list,
                  s=list, scaleX=float(), sx=float(), scaleY=float(), sy=float(), scaleZ=float(), sz=float(),
                  translate=list, t=list, translateX=float(), tx=float(), translateY=float(), ty=float(),
                  translateZ=float(), tz=float(), weight=float(), w=float(), worldSpace=bool(), ws=bool(), *args,
                  **kwargs):
    pass


def polyMoveFacetUV(axisLen=list, l=list, axisLenX=float(), lx=float(), axisLenY=float(), ly=float(), caching=bool(),
                    cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(), nodeState=int(), nds=int(),
                    pivot=list, pvt=list, pivotU=float(), pvu=float(), pivotV=float(), pvv=float(), random=float(),
                    ran=float(), rotationAngle=float(), ra=float(), scale=list, s=list, scaleU=float(), su=float(),
                    scaleV=float(), sv=float(), translate=list, t=list, translateU=float(), tu=float(),
                    translateV=float(), tv=float(), *args, **kwargs):
    pass


def polyMoveUV(axisLen=list, l=list, axisLenX=float(), lx=float(), axisLenY=float(), ly=float(), caching=bool(),
               cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(), nodeState=int(), nds=int(),
               pivot=list, pvt=list, pivotU=float(), pvu=float(), pivotV=float(), pvv=float(), random=float(),
               ran=float(), rotationAngle=float(), ra=float(), scale=list, s=list, scaleU=float(), su=float(),
               scaleV=float(), sv=float(), translate=list, t=list, translateU=float(), tu=float(), translateV=float(),
               tv=float(), *args, **kwargs):
    pass


def polyMoveVertex(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), gain=float(), ga=float(),
                   localDirection=list, ld=list, localDirectionX=float(), ldx=float(), localDirectionY=float(),
                   ldy=float(), localDirectionZ=float(), ldz=float(), localTranslate=list, lt=list,
                   localTranslateX=float(), ltx=float(), localTranslateY=float(), lty=float(), localTranslateZ=float(),
                   ltz=float(), name=str(), n=str(), nodeState=int(), nds=int(), pivot=list, pvt=list, pivotX=float(),
                   pvx=float(), pivotY=float(), pvy=float(), pivotZ=float(), pvz=float(), random=float(), ran=float(),
                   rotate=list, ro=list, rotateX=float(), rx=float(), rotateY=float(), ry=float(), rotateZ=float(),
                   rz=float(), scale=list, s=list, scaleX=float(), sx=float(), scaleY=float(), sy=float(),
                   scaleZ=float(), sz=float(), translate=list, t=list, translateX=float(), tx=float(),
                   translateY=float(), ty=float(), translateZ=float(), tz=float(), worldSpace=bool(), ws=bool(), *args,
                   **kwargs):
    pass


def polyMultiLayoutUV(flipReversed=bool(), fr=bool(), gridU=int(), gu=int(), gridV=int(), gv=int(), layout=int(),
                      l=int(), layoutMethod=int(), lm=int(), offsetU=float(), ou=float(), offsetV=float(), ov=float(),
                      percentageSpace=float(), ps=float(), prescale=int(), psc=int(), rotateForBestFit=int(), rbf=int(),
                      scale=int(), sc=int(), sizeU=float(), su=float(), sizeV=float(), sv=float(), uvSetName=str(),
                      uvs=str(), *args, **kwargs):
    pass


def polyNormal(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(), nodeState=int(),
               nds=int(), normalMode=int(), nm=int(), userNormalMode=bool(), unm=bool(), *args, **kwargs):
    pass


def polyNormalizeUV(caching=bool(), cch=bool(), centerOnTile=bool(), cot=bool(), constructionHistory=bool(), ch=bool(),
                    createNewMap=bool(), cm=bool(), insertBeforeDeformers=bool(), ibd=bool(), name=str(), n=str(),
                    nodeState=int(), nds=int(), normalizeDirection=int(), nd=int(), normalizeType=int(), nt=int(),
                    preserveAspectRatio=bool(), pa=bool(), uvSetName=str(), uvs=str(), worldSpace=bool(), ws=bool(),
                    *args, **kwargs):
    pass


def polyNormalPerVertex(allLocked=bool(), al=bool(), deformable=bool(), freezeNormal=bool(), fn=bool(), normalX=float(),
                        x=float(), normalXYZ=list, xyz=list, normalY=float(), y=float(), normalZ=float(), z=float(),
                        relative=bool(), rel=bool(), unFreezeNormal=bool(), ufn=bool(), *args, **kwargs):
    pass


def polyOptions(activeObjects=bool(), ao=bool(), allEdges=bool(), ae=bool(), backCullVertex=bool(), bcv=bool(),
                backCulling=bool(), bc=bool(), colorMaterialChannel=str(), cm=str(), colorShadedDisplay=bool(),
                cs=bool(), displayAlphaAsGreyScale=bool(), dal=bool(), displayBlueChannel=bool(), dbc=bool(),
                displayBorder=bool(), db=bool(), displayCenter=bool(), dc=bool(), displayCreaseEdge=bool(), dce=bool(),
                displayCreaseVertex=bool(), dcv=bool(), displayGeometry=bool(), dg=bool(), displayGreenChannel=bool(),
                dgc=bool(), displayInvisibleFaces=bool(), dif=bool(), displayItemNumbers=list, din=list,
                displayMapBorder=bool(), dmb=bool(), displayMetadata=list, dmt=list, displayNormal=bool(), dn=bool(),
                displayRedChannel=bool(), drc=bool(), displaySubdComps=bool(), dsc=bool(), displayTangent=bool(),
                dtn=bool(), displayTriangle=bool(), dt=bool(), displayUVTopology=bool(), uvt=bool(), displayUVs=bool(),
                duv=bool(), displayVertex=bool(), dv=bool(), displayWarp=bool(), dw=bool(), facet=bool(), f=bool(),
                fullBack=bool(), fb=bool(), gl=bool(), hardBack=bool(), hb=bool(), hardEdge=bool(), he=bool(),
                hardEdgeColor=bool(), hec=bool(), materialBlend=str(), mb=str(), newPolymesh=bool(), np=bool(),
                point=bool(), pt=bool(), pointFacet=bool(), pf=bool(), relative=bool(), r=bool(), reuseTriangles=bool(),
                rt=bool(), sizeBorder=float(), sb=float(), sizeNormal=float(), sn=float(), sizeUV=float(), suv=float(),
                sizeVertex=float(), sv=float(), smoothDrawType=int(), sdt=int(), softEdge=bool(), se=bool(),
                vertexNormalMethod=int(), vnm=int(), wireBackCulling=bool(), wbc=bool(), *args, **kwargs):
    pass


def polyOptUvs(applyToShell=bool(), areaWeight=float(), aw=float(), caching=bool(), cch=bool(),
               constructionHistory=bool(), ch=bool(), globalBlend=float(), gb=float(), globalMethodBlend=float(),
               gmb=float(), iterations=int(), i=int(), name=str(), n=str(), nodeState=int(), nds=int(),
               optimizeAxis=int(), oa=int(), pinSelected=bool(), ps=bool(), pinUvBorder=bool(), pub=bool(),
               scale=float(), s=float(), stoppingThreshold=float(), ss=float(), useScale=bool(), us=bool(),
               uvSetName=str(), uvs=str(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyOutput(allValues=bool(), a=bool(), color=bool(), c=bool(), colorDesc=bool(), cd=bool(), edge=bool(), e=bool(),
               edgeFace=bool(), ef=bool(), face=bool(), f=bool(), faceNorm=bool(), fn=bool(), force=bool(), fo=bool(),
               group=bool(), g=bool(), noOutput=bool(), no=bool(), normDesc=bool(), nd=bool(), outputFile=str(),
               of=str(), triangle=bool(), t=bool(), uvDesc=bool(), uvd=bool(), uvValue=bool(), uv=bool(), vert=bool(),
               v=bool(), vertEdge=bool(), ve=bool(), vertNorm=bool(), vn=bool(), *args, **kwargs):
    pass


def polyPinUV(createHistory=bool(), ch=bool(), operation=int(), op=int(), unpinned=bool(), unp=bool(), uvSetName=str(),
              uvs=str(), value=float(), v=float(), *args, **kwargs):
    pass


def polyPipe(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createUVs=bool(),
             cuv=bool(), height=float(), h=float(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(),
             o=bool(), radius=float(), r=float(), roundCap=bool(), rcp=bool(), subdivisionsAxis=int(), sa=int(),
             subdivisionsCaps=int(), sc=int(), subdivisionsHeight=int(), sh=int(), texture=bool(), tx=bool(),
             thickness=float(), t=float(), *args, **kwargs):
    pass


def polyPlanarProjection(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createNewMap=bool(),
                         cm=bool(), imageCenter=list, ic=list, imageCenterX=float(), icx=float(), imageCenterY=float(),
                         icy=float(), imageScale=list, imageScaleU=float(), isu=float(), imageScaleV=float(),
                         isv=float(), insertBeforeDeformers=bool(), ibd=bool(), keepImageRatio=bool(), kir=bool(),
                         mapDirection=str(), md=str(), name=str(), n=str(), nodeState=int(), nds=int(),
                         perInstance=bool(), pi=bool(), projectionCenter=list, pc=list, projectionCenterX=float(),
                         pcx=float(), projectionCenterY=float(), pcy=float(), projectionCenterZ=float(), pcz=float(),
                         projectionHeight=float(), ph=float(), projectionHorizontalSweep=float(), phs=float(),
                         projectionScale=list, ps=list, rotate=list, ro=list, rotateX=float(), rx=float(),
                         rotateY=float(), ry=float(), rotateZ=float(), rz=float(), rotationAngle=float(), ra=float(),
                         seamCorrect=bool(), sc=bool(), smartFit=bool(), sf=bool(), worldSpace=bool(), ws=bool(), *args,
                         **kwargs):
    pass


def polyPlane(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createUVs=int(),
              cuv=int(), height=float(), h=float(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(),
              o=bool(), subdivisionsHeight=int(), sh=int(), subdivisionsWidth=int(), sw=int(), subdivisionsX=int(),
              sx=int(), subdivisionsY=int(), sy=int(), texture=int(), tx=int(), width=float(), w=float(), *args,
              **kwargs):
    pass


def polyPlatonicSolid(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                      createUVs=int(), cuv=int(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(),
                      o=bool(), radius=float(), r=float(), sideLength=float(), l=float(), solidType=int(), st=int(),
                      texture=int(), tx=int(), *args, **kwargs):
    pass


def polyPoke(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), localTranslate=list, lt=list,
             localTranslateX=float(), ltx=float(), localTranslateY=float(), lty=float(), localTranslateZ=float(),
             ltz=float(), name=str(), n=str(), nodeState=int(), nds=int(), translate=list, t=list, translateX=float(),
             tx=float(), translateY=float(), ty=float(), translateZ=float(), tz=float(), worldSpace=bool(), ws=bool(),
             *args, **kwargs):
    pass


def polyPrimitive(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                  createUVs=int(), cuv=int(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(),
                  polyType=int(), pt=int(), radius=float(), r=float(), sideLength=float(), l=float(), texture=int(),
                  tx=int(), *args, **kwargs):
    pass


def polyPrism(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createUVs=int(),
              cuv=int(), length=float(), l=float(), name=str(), n=str(), nodeState=int(), nds=int(),
              numberOfSides=int(), ns=int(), numderOfSides=int(), nsi=int(), object=bool(), o=bool(),
              sideLength=float(), w=float(), subdivisionsCaps=int(), sc=int(), subdivisionsHeight=int(), sh=int(),
              texture=int(), tx=int(), *args, **kwargs):
    pass


def polyProjectCurve(addUnderTransform=bool(), aut=bool(), caching=bool(), cch=bool(), direction=list, d=list,
                     directionX=float(), dx=float(), directionY=float(), dy=float(), directionZ=float(), dz=float(),
                     nodeState=int(), nds=int(), tolerance=float(), tol=float(), *args, **kwargs):
    pass


def polyProjection(constructionHistory=bool(), ch=bool(), createNewMap=bool(), cm=bool(), imageCenterX=float(),
                   icx=float(), imageCenterY=float(), icy=float(), imageScaleU=float(), isu=float(),
                   imageScaleV=float(), isv=float(), insertBeforeDeformers=bool(), ibd=bool(), keepImageRatio=bool(),
                   kir=bool(), mapDirection=str(), md=str(), projectionCenterX=float(), pcx=float(),
                   projectionCenterY=float(), pcy=float(), projectionCenterZ=float(), pcz=float(),
                   projectionScaleU=float(), psu=float(), projectionScaleV=float(), psv=float(), rotateX=float(),
                   rx=float(), rotateY=float(), ry=float(), rotateZ=float(), rz=float(), rotationAngle=float(),
                   ra=float(), seamCorrect=bool(), sc=bool(), smartFit=bool(), sf=bool(), type=str(), t=str(),
                   uvSetName=str(), uvs=str(), *args, **kwargs):
    pass


def polyPyramid(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createUVs=int(),
                cuv=int(), name=str(), n=str(), nodeState=int(), nds=int(), numberOfSides=int(), ns=int(),
                numderOfSides=int(), nsi=int(), object=bool(), o=bool(), sideLength=float(), w=float(),
                subdivisionsCaps=int(), sc=int(), subdivisionsHeight=int(), sh=int(), texture=bool(), tx=bool(), *args,
                **kwargs):
    pass


def polyQuad(angle=float(), a=float(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
             keepGroupBorder=bool(), kgb=bool(), keepHardEdges=bool(), khe=bool(), keepTextureBorders=bool(),
             ktb=bool(), name=str(), n=str(), nodeState=int(), nds=int(), worldSpace=bool(), ws=bool(), *args,
             **kwargs):
    pass


def polyQueryBlindData(associationType=str(), at=str(), binaryData=str(), bnd=str(), booleanData=bool(), bd=bool(),
                       doubleData=float(), dbd=float(), intData=int(), ind=int(), longDataName=str(), ldn=str(),
                       maxValue=float(), max=float(), minValue=float(), min=float(), shortDataName=str(), sdn=str(),
                       showComp=bool(), sc=bool(), stringData=str(), sd=str(), subString=str(), ss=str(), typeId=int(),
                       id=int(), *args, **kwargs):
    pass


def polyReduce(caching=bool(), cch=bool(), cachingReduce=bool(), cr=bool(), colorWeights=float(), cwt=float(),
               compactness=float(), com=float(), constructionHistory=bool(), ch=bool(), geomWeights=float(),
               gwt=float(), invertVertexWeights=bool(), iwt=bool(), keepBorder=bool(), kb=bool(),
               keepBorderWeight=float(), kbw=float(), keepColorBorder=bool(), kcb=bool(), keepColorBorderWeight=float(),
               kcw=float(), keepCreaseEdge=bool(), kce=bool(), keepCreaseEdgeWeight=float(), cew=float(),
               keepFaceGroupBorder=bool(), kfb=bool(), keepFaceGroupBorderWeight=float(), kfw=float(),
               keepHardEdge=bool(), khe=bool(), keepHardEdgeWeight=float(), khw=float(), keepMapBorder=bool(),
               kmb=bool(), keepMapBorderWeight=float(), kmw=float(), keepOriginalVertices=bool(), kev=bool(),
               keepQuadsWeight=float(), kqw=float(), name=str(), n=str(), nodeState=int(), nds=int(),
               percentage=float(), p=float(), preserveLocation=bool(), pl=bool(), preserveTopology=bool(), top=bool(),
               replaceOriginal=bool(), rpo=bool(), sharpness=float(), shp=float(), symmetryPlaneW=float(), sw=float(),
               symmetryPlaneX=float(), sx=float(), symmetryPlaneY=float(), sy=float(), symmetryPlaneZ=float(),
               sz=float(), symmetryTolerance=float(), stl=float(), termination=int(), trm=int(), triangleCount=int(),
               tct=int(), triangulate=bool(), t=bool(), useVirtualSymmetry=int(), uvs=int(), uvWeights=float(),
               uwt=float(), version=int(), ver=int(), vertexCount=int(), vct=int(), vertexMapName=str(), vmp=str(),
               vertexWeightCoefficient=float(), vwc=float(), weightCoefficient=float(), wc=float(), *args, **kwargs):
    pass


def polyRemesh(caching=bool(), cch=bool(), collapseThreshold=float(), cot=float(), constructionHistory=bool(),
               ch=bool(), interpolationType=int(), ipt=int(), maxEdgeLength=float(), mel=float(), name=str(), n=str(),
               nodeState=int(), nds=int(), smoothStrength=float(), smt=float(), tessellateBorders=bool(), tsb=bool(),
               useRelativeValues=bool(), urv=bool(), *args, **kwargs):
    pass


def polyRetopo(*args, **kwargs):
    pass


def polySelect(add=bool(), addFirst=bool(), af=bool(), asSelectString=bool(), ass=bool(), deselect=bool(), d=bool(),
               edgeBorder=int(), eb=int(), edgeBorderPath=list, ebp=list, edgeBorderPattern=list, bpt=list,
               edgeLoop=int(), el=int(), edgeLoopOrBorder=int(), elb=int(), edgeLoopOrBorderPattern=list, lbp=list,
               edgeLoopPath=list, elp=list, edgeLoopPattern=list, lpt=list, edgeRing=int(), er=int(), edgeRingPath=list,
               erp=list, edgeRingPattern=list, rpt=list, edgeUVLoopOrBorder=int(), euv=int(), everyN=int(), en=int(),
               extendToShell=int(), ets=int(), noSelection=bool(), ns=bool(), replace=bool(), r=bool(),
               shortestEdgePath=list, sep=list, shortestEdgePathUV=list, spu=list, shortestFacePath=list, sfp=list,
               toggle=bool(), tgl=bool(), *args, **kwargs):
    pass


def polySelectConstraint(angle=int(), a=int(), anglePropagation=bool(), ap=bool(), angleTolerance=float(), at=float(),
                         anglebound=list, ab=list, border=bool(), bo=bool(), borderPropagation=bool(), bp=bool(),
                         convexity=int(), c=int(), crease=bool(), cr=bool(), disable=bool(), dis=bool(), dist=int(),
                         d=int(), distaxis=list, da=list, distbound=list, db=list, distpoint=list, dp=list,
                         edgeDistance=int(), ed=int(), geometricarea=int(), ga=int(), geometricareabound=list, gab=list,
                         holes=int(), h=int(), length=int(), l=int(), lengthbound=list, lb=list, loopPropagation=bool(),
                         lp=bool(), max2dAngle=float(), m2a=float(), max3dAngle=float(), m3a=float(), mode=int(),
                         m=int(), nonmanifold=int(), nm=int(), oppositeEdges=bool(), oe=bool(), order=int(),
                         orderbound=list, orb=list, orient=int(), o=int(), orientaxis=list, oa=list, orientbound=list,
                         ob=list, planarity=int(), p=int(), propagate=int(), pp=int(), random=int(), r=int(),
                         randomratio=float(), rr=float(), returnSelection=bool(), rs=bool(), ringPropagation=bool(),
                         rp=bool(), shell=bool(), sh=bool(), size=int(), sz=int(), smoothness=int(), sm=int(),
                         stateString=bool(), sts=bool(), textured=int(), tx=int(), texturedarea=int(), ta=int(),
                         texturedareabound=list, tab=list, textureshared=int(), ts=int(), topology=int(), tp=int(),
                         type=int(), t=int(), uvBorderSelection=bool(), ubs=bool(), uvConstraint=bool(), uvc=bool(),
                         uvEdgeLoopPropagation=bool(), ulp=bool(), uvEdgeRingPropagation=bool(), urp=bool(),
                         uvFaceOrientation=int(), ufo=int(), uvShell=bool(), uv=bool(), visibility=int(), v=int(),
                         visibilityangle=float(), va=float(), visibilitypoint=list, vp=list, where=int(), w=int(),
                         wholeSensitive=bool(), ws=bool(), *args, **kwargs):
    pass


def polySelectConstraintMonitor(changeCommand=list, cc=list, create=bool(), c=bool(), delete=bool(), d=bool(), *args,
                                **kwargs):
    pass


def polySelectCtx(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                  mode=int(), m=int(), *args, **kwargs):
    pass


def polySelectEditCtx(absoluteOffset=bool(), abo=bool(), adjustEdgeFlow=float(), aef=float(), autoComplete=bool(),
                      ac=bool(), deleteEdge=bool(), de=bool(), divisions=int(), div=int(), endVertexOffset=float(),
                      evo=float(), exists=bool(), ex=bool(), fixQuads=bool(), fq=bool(), image1=str(), i1=str(),
                      image2=str(), i2=str(), image3=str(), i3=str(), insertWithEdgeFlow=bool(), ief=bool(), mode=int(),
                      m=int(), smoothingAngle=float(), sma=float(), splitType=int(), stp=int(),
                      startVertexOffset=float(), svo=float(), useEqualMultiplier=bool(), uem=bool(), *args, **kwargs):
    pass


def polySeparate(caching=bool(), cch=bool(), nodeState=int(), nds=int(), removeShells=bool(), rs=bool(),
                 separateSpecificShell=int(), sss=int(), *args, **kwargs):
    pass


def polySetToFaceNormal(setUserNormal=bool(), su=bool(), *args, **kwargs):
    pass


def polySewEdge(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(), nodeState=int(),
                nds=int(), texture=bool(), tx=bool(), tolerance=float(), t=float(), worldSpace=bool(), ws=bool(), *args,
                **kwargs):
    pass


def polyShortestPathCtx(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(),
                        i3=str(), *args, **kwargs):
    pass


def polySlideEdge(absolute=bool(), a=bool(), direction=int(), d=int(), edgeDirection=float(), ed=float(),
                  symmetry=bool(), sym=bool(), *args, **kwargs):
    pass


def polySmooth(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), continuity=float(), c=float(),
               degree=int(), deg=int(), divisions=int(), dv=int(), divisionsPerEdge=int(), dpe=int(), keepBorder=bool(),
               kb=bool(), keepHardEdge=bool(), khe=bool(), keepMapBorders=int(), kmb=int(), keepSelectionBorder=bool(),
               ksb=bool(), keepTesselation=bool(), xkt=bool(), keepTessellation=bool(), kt=bool(), method=int(),
               mth=int(), name=str(), n=str(), nodeState=int(), nds=int(), osdCreaseMethod=int(), ocr=int(),
               osdFvarBoundary=int(), ofb=int(), osdFvarPropagateCorners=bool(), ofc=bool(), osdSmoothTriangles=bool(),
               ost=bool(), osdVertBoundary=int(), ovb=int(), propagateEdgeHardness=bool(), peh=bool(),
               pushStrength=float(), ps=float(), roundness=float(), ro=float(), smoothUVs=bool(), suv=bool(),
               subdivisionLevels=int(), sl=int(), subdivisionType=int(), sdt=int(), *args, **kwargs):
    pass


def polySoftEdge(angle=float(), a=float(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                 name=str(), n=str(), nodeState=int(), nds=int(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polySphere(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createUVs=int(),
               cuv=int(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), radius=float(),
               r=float(), subdivisionsAxis=int(), sa=int(), subdivisionsHeight=int(), sh=int(), subdivisionsX=int(),
               sx=int(), subdivisionsY=int(), sy=int(), texture=int(), tx=int(), *args, **kwargs):
    pass


def polySphericalProjection(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createNewMap=bool(),
                            cm=bool(), imageCenter=list, ic=list, imageCenterX=float(), icx=float(),
                            imageCenterY=float(), icy=float(), imageScale=list, imageScaleU=float(), isu=float(),
                            imageScaleV=float(), isv=float(), insertBeforeDeformers=bool(), ibd=bool(),
                            keepImageRatio=bool(), kir=bool(), mapDirection=str(), md=str(), name=str(), n=str(),
                            nodeState=int(), nds=int(), perInstance=bool(), pi=bool(), projectionCenter=list, pc=list,
                            projectionCenterX=float(), pcx=float(), projectionCenterY=float(), pcy=float(),
                            projectionCenterZ=float(), pcz=float(), projectionHorizontalSweep=float(), phs=float(),
                            projectionScale=list, ps=list, projectionScaleU=float(), psu=float(),
                            projectionScaleV=float(), psv=float(), radius=float(), r=float(), rotate=list, ro=list,
                            rotateX=float(), rx=float(), rotateY=float(), ry=float(), rotateZ=float(), rz=float(),
                            rotationAngle=float(), ra=float(), seamCorrect=bool(), sc=bool(), smartFit=bool(),
                            sf=bool(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polySplit(adjustEdgeFlow=float(), aef=float(), constructionHistory=bool(), ch=bool(), detachEdges=bool(), de=bool(),
              edgepoint=list, ep=list, facepoint=list, fp=list, insertWithEdgeFlow=bool(), ief=bool(), insertpoint=list,
              ip=list, name=str(), n=str(), projectedCurve=str(), pc=str(), projectedCurveTolerance=float(),
              pct=float(), smoothingangle=float(), sma=float(), subdivision=int(), s=int(), *args, **kwargs):
    pass


def polySplitCtx(enablesnap=bool(), es=bool(), exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                 image3=str(), i3=str(), magnetsnap=int(), ms=int(), precsnap=float(), ps=float(),
                 smoothingangle=float(), sma=float(), snaptoedge=bool(), ste=bool(), subdivision=int(), s=int(), *args,
                 **kwargs):
    pass


def polySplitCtx2(adjustEdgeFlow=float(), aef=float(), constrainToEdges=bool(), cte=bool(), edgeMagnets=int(), em=int(),
                  exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                  insertWithEdgeFlow=bool(), ief=bool(), snapTolerance=float(), st=float(), snappedToEdgeColor=list,
                  sec=list, snappedToFaceColor=list, sfc=list, snappedToMagnetColor=list, smc=list,
                  snappedToVertexColor=list, svc=list, *args, **kwargs):
    pass


def polySplitEdge(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                  nodeState=int(), nds=int(), operation=int(), op=int(), *args, **kwargs):
    pass


def polySplitRing(adjustEdgeFlow=float(), aef=float(), caching=bool(), cch=bool(), constructionHistory=bool(),
                  ch=bool(), direction=bool(), dr=bool(), divisions=int(), div=int(), enableProfileCurve=bool(),
                  epc=bool(), fixQuads=bool(), fq=bool(), insertWithEdgeFlow=bool(), ief=bool(), name=str(), n=str(),
                  nodeState=int(), nds=int(), profileCurveInputOffset=float(), pio=float(),
                  profileCurveInputScale=float(), pis=float(), profileCurve_FloatValue=float(), pfv=float(),
                  profileCurve_Interp=int(), pi=int(), profileCurve_Position=float(), pp=float(), rootEdge=int(),
                  re=int(), smoothingAngle=float(), sma=float(), splitType=int(), stp=int(), useEqualMultiplier=bool(),
                  uem=bool(), useFaceNormalsAtEnds=bool(), fne=bool(), weight=float(), wt=float(), worldSpace=bool(),
                  ws=bool(), *args, **kwargs):
    pass


def polySplitVertex(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                    nodeState=int(), nds=int(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polyStraightenUVBorder(blendOriginal=float(), bo=float(), caching=bool(), cch=bool(), constructionHistory=bool(),
                           ch=bool(), curvature=float(), c=float(), gapTolerance=int(), gt=int(), name=str(), n=str(),
                           nodeState=int(), nds=int(), preserveLength=float(), pl=float(), uvSetName=str(), uvs=str(),
                           worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def polySubdivideEdge(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), divisions=int(), dv=int(),
                      name=str(), n=str(), nodeState=int(), nds=int(), size=float(), s=float(), worldSpace=bool(),
                      ws=bool(), *args, **kwargs):
    pass


def polySubdivideFacet(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), divisions=int(), dv=int(),
                       divisionsU=int(), duv=int(), divisionsV=int(), dvv=int(), mode=int(), m=int(), name=str(),
                       n=str(), nodeState=int(), nds=int(), subdMethod=int(), sbm=int(), *args, **kwargs):
    pass


def polyTorus(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createUVs=bool(),
              cuv=bool(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), radius=float(),
              r=float(), sectionRadius=float(), sr=float(), subdivisionsAxis=int(), sa=int(), subdivisionsHeight=int(),
              sh=int(), subdivisionsX=int(), sx=int(), subdivisionsY=int(), sy=int(), texture=bool(), tx=bool(),
              twist=float(), tw=float(), *args, **kwargs):
    pass


def polyToSubdiv(absolutePosition=bool(), ap=bool(), addUnderTransform=bool(), aut=bool(), applyMatrixToResult=bool(),
                 amr=bool(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), maxEdgesPerVert=int(),
                 me=int(), maxPolyCount=int(), mpc=int(), name=str(), n=str(), nodeState=int(), nds=int(),
                 object=bool(), o=bool(), preserveVertexOrdering=bool(), pvo=bool(), quickConvert=bool(), qc=bool(),
                 uvPoints=list, uvp=list, uvPointsU=float(), uvu=float(), uvPointsV=float(), uvv=float(),
                 uvTreatment=int(), uvt=int(), *args, **kwargs):
    pass


def polyTransfer(alternateObject=str(), ao=str(), caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(),
                 name=str(), n=str(), nodeState=int(), nds=int(), uvSets=bool(), uv=bool(), vertexColor=bool(),
                 vc=bool(), vertices=bool(), v=bool(), *args, **kwargs):
    pass


def polyTriangulate(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                    nodeState=int(), nds=int(), *args, **kwargs):
    pass


def polyUnite(caching=bool(), cch=bool(), centerPivot=bool(), cp=bool(), mergeUVSets=int(), muv=int(), nodeState=int(),
              nds=int(), objectPivot=bool(), op=bool(), *args, **kwargs):
    pass


def polyUniteSkinned(centerPivot=bool(), cp=bool(), constructionHistory=bool(), ch=bool(), mergeUVSets=int(), muv=int(),
                     objectPivot=bool(), op=bool(), *args, **kwargs):
    pass


def polyUVCoverage(uvRange=list, ur=list, *args, **kwargs):
    pass


def polyUVOverlap(nonOverlappingComponents=bool(), noc=bool(), overlappingComponents=bool(), oc=bool(), *args,
                  **kwargs):
    pass


def polyUVRectangle(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                    nodeState=int(), nds=int(), *args, **kwargs):
    pass


def polyUVSet(allUVSets=bool(), auv=bool(), allUVSetsIndices=bool(), uvn=bool(), allUVSetsWithCount=bool(), awc=bool(),
              copy=bool(), cp=bool(), create=bool(), cr=bool(), currentLastUVSet=bool(), luv=bool(),
              currentPerInstanceUVSet=bool(), cpi=bool(), currentUVSet=bool(), cuv=bool(), delete=bool(), d=bool(),
              genNewUVSet=bool(), gen=bool(), newUVSet=str(), nuv=str(), perInstance=bool(), pi=bool(),
              projections=bool(), pr=bool(), rename=bool(), rn=bool(), reorder=bool(), ro=bool(), shareInstances=bool(),
              si=bool(), unshared=bool(), us=bool(), uvSet=str(), uvs=str(), *args, **kwargs):
    pass


def polyUVStackSimilarShells(onlyMatch=bool(), om=bool(), tolerance=float(), to=float(), *args, **kwargs):
    pass


def polyWedgeFace(axis=list, ax=list, caching=bool(), cch=bool(), center=list, cen=list, constructionHistory=bool(),
                  ch=bool(), divisions=int(), d=int(), edge=int(), ed=int(), name=str(), n=str(), nodeState=int(),
                  nds=int(), wedgeAngle=float(), wa=float(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def popupMenu(allowOptionBoxes=bool(), aob=bool(), altModifier=bool(), alt=bool(), button=int(), b=int(),
              ctrlModifier=bool(), ctl=bool(), defineTemplate=str(), dt=str(), deleteAllItems=bool(), dai=bool(),
              exists=bool(), ex=bool(), itemArray=bool(), ia=bool(), markingMenu=bool(), mm=bool(),
              numberOfItems=bool(), ni=bool(), parent=str(), p=str(), postMenuCommand=str(), pmc=str(),
              postMenuCommandOnce=bool(), pmo=bool(), shiftModifier=bool(), sh=bool(), useTemplate=str(), ut=str(),
              *args, **kwargs):
    pass


def pose(allPoses=bool(), ap=bool(), apply=bool(), a=bool(), name=str(), n=str(), *args, **kwargs):
    pass


def poseEditor(control=bool(), ctl=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), exists=bool(),
               ex=bool(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(), highlightConnection=str(),
               hlc=str(), lockMainConnection=bool(), lck=bool(), mainListConnection=str(), mlc=str(), panel=str(),
               pnl=str(), parent=str(), p=str(), selectionConnection=str(), slc=str(), stateString=bool(), sts=bool(),
               unParent=bool(), up=bool(), unlockMainConnection=bool(), ulk=bool(), updateMainConnection=bool(),
               upd=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def posePanel(control=bool(), ctl=bool(), copy=str(), cp=str(), createString=bool(), cs=bool(), defineTemplate=str(),
              dt=str(), docTag=str(), dtg=str(), editString=bool(), es=bool(), exists=bool(), ex=bool(), init=bool(),
              isUnique=bool(), iu=bool(), label=str(), l=str(), menuBarRepeatLast=bool(), mrl=bool(),
              menuBarVisible=bool(), mbv=bool(), needsInit=bool(), ni=bool(), parent=str(), p=str(),
              popupMenuProcedure=str(), pmp=str(), poseEditor=bool(), pe=bool(), replacePanel=str(), rp=str(),
              tearOff=bool(), to=bool(), tearOffCopy=str(), toc=str(), tearOffRestore=bool(), tor=bool(),
              unParent=bool(), up=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def preferredRenderer(fallback=str(), f=str(), makeCurrent=bool(), mc=bool(), *args, **kwargs):
    pass


def preloadRefEd(control=bool(), ctl=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), exists=bool(),
                 ex=bool(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(), highlightConnection=str(),
                 hlc=str(), lockMainConnection=bool(), lck=bool(), mainListConnection=str(), mlc=str(), panel=str(),
                 pnl=str(), parent=str(), p=str(), selectCommand=str(), sc=str(), selectFileNode=bool(), sf=bool(),
                 selectionConnection=str(), slc=str(), stateString=bool(), sts=bool(), unParent=bool(), up=bool(),
                 unlockMainConnection=bool(), ulk=bool(), updateMainConnection=bool(), upd=bool(), useTemplate=str(),
                 ut=str(), *args, **kwargs):
    pass


def prepareRender(defaultTraversalSet=str(), dt=str(), deregister=str(), d=str(), invokePostRender=bool(), ior=bool(),
                  invokePostRenderFrame=bool(), iof=bool(), invokePostRenderLayer=bool(), iol=bool(),
                  invokePreRender=bool(), irr=bool(), invokePreRenderFrame=bool(), irf=bool(),
                  invokePreRenderLayer=bool(), irl=bool(), invokeSettingsUI=bool(), isu=bool(), label=str(), lbl=str(),
                  listTraversalSets=bool(), lt=bool(), postRender=str(), por=str(), postRenderFrame=str(), pof=str(),
                  postRenderLayer=str(), pol=str(), preRender=str(), prr=str(), preRenderFrame=str(), prf=str(),
                  preRenderLayer=str(), prl=str(), restore=bool(), rtr=bool(), saveAssemblyConfig=bool(), sac=bool(),
                  settingsUI=str(), sui=str(), setup=bool(), stp=bool(), traversalSet=str(), ts=str(),
                  traversalSetInit=str(), tsi=str(), *args, **kwargs):
    pass


def profiler(addCategory=str(), a=str(), allCategories=bool(), ac=bool(), bufferSize=int(), b=int(),
             categoryIndex=int(), ci=int(), categoryIndexToName=int(), cin=int(), categoryInfo=str(), cf=str(),
             categoryName=str(), cn=str(), categoryNameToIndex=str(), cni=str(), categoryRecording=bool(), cr=bool(),
             clearAllMelInstrumentation=bool(), cam=bool(), colorIndex=int(), coi=int(), eventCPUId=bool(), eci=bool(),
             eventCategory=bool(), eca=bool(), eventColor=bool(), eco=bool(), eventCount=bool(), ec=bool(),
             eventDescription=bool(), ed=bool(), eventDuration=bool(), edu=bool(), eventIndex=int(), ei=int(),
             eventName=bool(), en=bool(), eventStartTime=bool(), et=bool(), eventThreadId=bool(), eti=bool(),
             instrumentMel=bool(), load=str(), l=str(), output=str(), o=str(), procedureDescription=str(), pd=str(),
             procedureName=str(), pn=str(), removeCategory=str(), rc=str(), reset=bool(), r=bool(), sampling=bool(),
             s=bool(), signalEvent=bool(), sig=bool(), signalMelEvent=bool(), sim=bool(), *args, **kwargs):
    pass


def profilerTool(categoryView=bool(), cat=bool(), collapseSelectedEvents=bool(), cs=bool(),
                 collapseSelectedEventsRepetition=bool(), csr=bool(), cpuView=bool(), cpu=bool(), destroy=bool(),
                 dtr=bool(), eventTypes=bool(), et=bool(), exists=bool(), ex=bool(), expandSelectedEvents=bool(),
                 es=bool(), expandSelectedEventsRepetition=bool(), esr=bool(), findNext=bool(), fn=bool(),
                 findPrevious=bool(), fp=bool(), frameAll=bool(), fa=bool(), frameSelected=bool(), fs=bool(),
                 isolateSegment=int(), make=bool(), mk=bool(), matchWholeWord=bool(), mww=bool(), searchEvent=str(),
                 se=str(), segmentCount=bool(), sc=bool(), showAllEvent=bool(), sa=bool(), showCriticalPath=bool(),
                 scp=bool(), showHotspot=bool(), sh=bool(), showSelectedEvents=bool(), ss=bool(),
                 showSelectedEventsRepetition=bool(), ssr=bool(), threadView=bool(), thd=bool(),
                 unisolateSegment=bool(), uis=bool(), *args, **kwargs):
    pass


def progressBar(annotation=str(), ann=str(), backgroundColor=list, bgc=list, beginProgress=bool(), bp=bool(),
                defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                enableKeyboardFocus=bool(), ekf=bool(), endProgress=bool(), ep=bool(), exists=bool(), ex=bool(),
                fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                isCancelled=bool(), ic=bool(), isInterruptable=bool(), ii=bool(), isMainProgressBar=bool(), imp=bool(),
                isObscured=bool(), io=bool(), manage=bool(), m=bool(), maxValue=int(), max=int(), minValue=int(),
                min=int(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(),
                p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), progress=int(), pr=int(),
                status=str(), st=str(), statusBarMessage=str(), sbm=str(), step=int(), s=int(), useTemplate=str(),
                ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
                *args, **kwargs):
    pass


def progressWindow(endProgress=bool(), ep=bool(), isCancelled=bool(), ic=bool(), isInterruptable=bool(), ii=bool(),
                   maxValue=int(), max=int(), minValue=int(), min=int(), progress=int(), pr=int(), status=str(),
                   st=str(), step=int(), s=int(), title=str(), t=str(), *args, **kwargs):
    pass


def projectCurve(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), direction=list, d=list,
                 directionX=float(), dx=float(), directionY=float(), dy=float(), directionZ=float(), dz=float(),
                 name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), range=bool(), rn=bool(),
                 tolerance=float(), tol=float(), useNormal=bool(), un=bool(), *args, **kwargs):
    pass


def projectionContext(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                      i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def projectionManip(fitBBox=bool(), fb=bool(), projType=int(), pt=int(), switchType=bool(), st=bool(), *args, **kwargs):
    pass


def projectTangent(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), curvature=bool(), c=bool(),
                   curvatureScale=float(), cs=float(), ignoreEdges=bool(), ie=bool(), name=str(), n=str(),
                   nodeState=int(), nds=int(), object=bool(), o=bool(), replaceOriginal=bool(), rpo=bool(),
                   reverseTangent=bool(), rt=bool(), rotate=float(), ro=float(), tangentDirection=int(), td=int(),
                   tangentScale=float(), ts=float(), *args, **kwargs):
    pass


def promptDialog(backgroundColor=list, bgc=list, button=str(), b=str(), cancelButton=str(), cb=str(),
                 defaultButton=str(), db=str(), dismissString=str(), ds=str(), message=str(), m=str(),
                 messageAlign=str(), ma=str(), parent=str(), p=str(), scrollableField=bool(), sf=bool(), style=str(),
                 st=str(), text=str(), tx=str(), title=str(), t=str(), *args, **kwargs):
    pass


def propModCtx(animCurve=str(), ac=str(), animCurveFalloff=list, acf=list, animCurveParam=str(), acp=str(),
               direction=list, d=list, exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
               image3=str(), i3=str(), linear=float(), l=float(), linearParam=list, lp=list, nurbsCurve=str(), nc=str(),
               powerCutoff=float(), pc=float(), powerCutoffParam=list, pcp=list, powerDegree=float(), pd=float(),
               powerDegreeParam=float(), pdp=float(), script=str(), s=str(), scriptParam=str(), sp=str(), type=int(),
               t=int(), worldspace=bool(), ws=bool(), *args, **kwargs):
    pass


def propMove(percent=float(), p=float(), percentX=float(), px=float(), percentY=float(), py=float(), percentZ=float(),
             pz=float(), pivot=list, pi=list, rotate=list, r=list, scale=list, s=list, translate=list, t=list,
             worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def psdChannelOutliner(addChild=list, ach=list, allItems=bool(), all=bool(), annotation=str(), ann=str(),
                       backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                       doubleClickCommand=str(), dcc=str(), dragCallback=str(), dgc=str(), dropCallback=str(),
                       dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                       enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(),
                       fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(),
                       manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), numberOfItems=bool(), ni=bool(),
                       numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                       preventOverride=bool(), po=bool(), psdParent=str(), ppa=str(), removeAll=bool(), ra=bool(),
                       removeChild=str(), rc=str(), select=str(), sel=str(), selectCommand=str(), sc=str(),
                       selectItem=bool(), si=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
                       visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                       **kwargs):
    pass


def psdEditTextureFile(addChannel=str(), adc=str(), addChannelColor=list, acc=list, addChannelImage=list, aci=list,
                       deleteChannel=str(), psdFileName=str(), psf=str(), snapShotImage=str(), ssi=str(),
                       uvSnapPostionTop=bool(), uvt=bool(), *args, **kwargs):
    pass


def psdExport(alphaChannelIdx=int(), aci=int(), bytesPerChannel=int(), bpc=int(), emptyLayerSet=bool(), els=bool(),
              format=str(), layerName=str(), lyn=str(), layerSetName=str(), lsn=str(), outFileName=str(), ofn=str(),
              preMultiplyAlpha=bool(), pma=bool(), psdFileName=str(), ifn=str(), *args, **kwargs):
    pass


def psdTextureFile(channelRGB=list, chc=list, channels=list, chs=list, imageFileName=list, ifn=list, psdFileName=str(),
                   psf=str(), snapShotImageName=str(), ssi=str(), uvSnapPostionTop=bool(), uvt=bool(),
                   xResolution=int(), xr=int(), yResolution=int(), yr=int(), *args, **kwargs):
    pass


def querySubdiv(action=int(), a=int(), level=int(), l=int(), relative=bool(), r=bool(), *args, **kwargs):
    pass


def quit(abort=bool(), a=bool(), exitCode=int(), ec=int(), force=bool(), f=bool(), *args, **kwargs):
    pass


def radial(attenuation=float(), att=float(), magnitude=float(), m=float(), maxDistance=float(), mxd=float(), name=str(),
           n=str(), perVertex=bool(), pv=bool(), position=list, pos=list, torusSectionRadius=float(), tsr=float(),
           type=float(), typ=float(), volumeExclusion=bool(), vex=bool(), volumeOffset=list, vof=list,
           volumeShape=str(), vsh=str(), volumeSweep=float(), vsw=float(), *args, **kwargs):
    pass


def radioButton(align=str(), al=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(),
                cc=str(), collection=str(), cl=str(), data=int(), da=int(), defineTemplate=str(), dt=str(),
                docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), editable=bool(),
                ed=bool(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                highlightColor=list, hlc=list, isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(),
                m=bool(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), offCommand=str(),
                ofc=str(), onCommand=str(), onc=str(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                preventOverride=bool(), po=bool(), recomputeSize=bool(), rs=bool(), select=bool(), sl=bool(),
                statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def radioButtonGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                   ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                   adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), annotation1=str(), an1=str(),
                   annotation2=str(), an2=str(), annotation3=str(), an3=str(), annotation4=str(), an4=str(),
                   backgroundColor=list, bgc=list, changeCommand=str(), cc=str(), changeCommand1=str(), cc1=str(),
                   changeCommand2=str(), cc2=str(), changeCommand3=str(), cc3=str(), changeCommand4=str(), cc4=str(),
                   columnAlign=list, cal=list, columnAlign2=list, cl2=list, columnAlign3=list, cl3=list,
                   columnAlign4=list, cl4=list, columnAlign5=list, cl5=list, columnAlign6=list, cl6=list,
                   columnAttach=list, cat=list, columnAttach2=list, ct2=list, columnAttach3=list, ct3=list,
                   columnAttach4=list, ct4=list, columnAttach5=list, ct5=list, columnAttach6=list, ct6=list,
                   columnOffset2=list, co2=list, columnOffset3=list, co3=list, columnOffset4=list, co4=list,
                   columnOffset5=list, co5=list, columnOffset6=list, co6=list, columnWidth=list, cw=list,
                   columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list, columnWidth3=list, cw3=list,
                   columnWidth4=list, cw4=list, columnWidth5=list, cw5=list, columnWidth6=list, cw6=list, data1=int(),
                   da1=int(), data2=int(), da2=int(), data3=int(), da3=int(), data4=int(), da4=int(),
                   defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                   dropCallback=str(), dpc=str(), editable=bool(), ed=bool(), enable=bool(), en=bool(), enable1=bool(),
                   en1=bool(), enable2=bool(), en2=bool(), enable3=bool(), en3=bool(), enable4=bool(), en4=bool(),
                   enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                   ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                   isObscured=bool(), io=bool(), label=str(), l=str(), label1=str(), l1=str(), label2=str(), l2=str(),
                   label3=str(), l3=str(), label4=str(), l4=str(), labelAnnotation=str(), la=str(), labelArray2=list,
                   la2=list, labelArray3=list, la3=list, labelArray4=list, la4=list, manage=bool(), m=bool(),
                   noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), numberOfRadioButtons=int(),
                   nrb=int(), offCommand=str(), ofc=str(), offCommand1=str(), of1=str(), offCommand2=str(), of2=str(),
                   offCommand3=str(), of3=str(), offCommand4=str(), of4=str(), onCommand=str(), onc=str(),
                   onCommand1=str(), on1=str(), onCommand2=str(), on2=str(), onCommand3=str(), on3=str(),
                   onCommand4=str(), on4=str(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                   preventOverride=bool(), po=bool(), rowAttach=list, rat=list, select=int(), sl=int(),
                   shareCollection=str(), scl=str(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
                   vertical=bool(), vr=bool(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                   width=int(), w=int(), *args, **kwargs):
    pass


def radioCollection(collectionItemArray=bool(), cia=bool(), defineTemplate=str(), dt=str(), exists=bool(), ex=bool(),
                    gl=bool(), numberOfCollectionItems=bool(), nci=bool(), parent=str(), p=str(), select=str(),
                    sl=str(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def radioMenuItemCollection(defineTemplate=str(), dt=str(), exists=bool(), ex=bool(), gl=bool(), parent=str(), p=str(),
                            useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def rampColorPort(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(),
                  docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
                  en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                  ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                  isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), node=str(),
                  n=str(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(),
                  pma=bool(), preventOverride=bool(), po=bool(), selectedColorControl=str(), sc=str(),
                  selectedInterpControl=str(), si=str(), selectedPositionControl=str(), sp=str(),
                  statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), verticalLayout=bool(), vl=bool(),
                  visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
                  **kwargs):
    pass


def rangeControl(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changedCommand=str(), cc=str(),
                 defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                 dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                 enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(),
                 height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(), manage=bool(),
                 m=bool(), maxRange=float(), max=float(), minRange=float(), min=float(), noBackground=bool(),
                 nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(),
                 pma=bool(), preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(),
                 ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
                 widthHeight=list, wh=list, *args, **kwargs):
    pass


def readTake(angle=str(), a=str(), device=str(), d=str(), frequency=float(), f=float(), linear=str(), l=str(),
             noTime=bool(), nt=bool(), take=str(), t=str(), *args, **kwargs):
    pass


def rebuildCurve(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), degree=int(), d=int(),
                 endKnots=int(), end=int(), fitRebuild=bool(), fr=bool(), keepControlPoints=bool(), kcp=bool(),
                 keepEndPoints=bool(), kep=bool(), keepRange=int(), kr=int(), keepTangents=bool(), kt=bool(),
                 name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), range=bool(), rn=bool(),
                 rebuildType=int(), rt=int(), replaceOriginal=bool(), rpo=bool(), smartSurfaceCurveRebuild=bool(),
                 scr=bool(), spans=int(), s=int(), tolerance=float(), tol=float(), *args, **kwargs):
    pass


def rebuildSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), degreeU=int(), du=int(),
                   degreeV=int(), dv=int(), direction=int(), dir=int(), endKnots=int(), end=int(), fitRebuild=int(),
                   fr=int(), keepControlPoints=bool(), kcp=bool(), keepCorners=bool(), kc=bool(), keepRange=int(),
                   kr=int(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), polygon=int(),
                   po=int(), rebuildType=int(), rt=int(), replaceOriginal=bool(), rpo=bool(), spansU=int(), su=int(),
                   spansV=int(), sv=int(), tolerance=float(), tol=float(), *args, **kwargs):
    pass


def recordAttr(attribute=str(), at=str(), delete=bool(), d=bool(), *args, **kwargs):
    pass


def recordDevice(cleanup=bool(), c=bool(), data=bool(), da=bool(), device=str(), d=str(), duration=int(), dr=int(),
                 playback=bool(), p=bool(), state=bool(), st=bool(), wait=bool(), w=bool(), *args, **kwargs):
    pass


def redo(*args, **kwargs):
    pass


def referenceEdit(applyFailedEdits=bool(), afe=bool(), changeEditTarget=list, cet=list, editCommand=str(), ec=str(),
                  failedEdits=bool(), fld=bool(), onReferenceNode=str(), orn=str(), removeEdits=bool(), r=bool(),
                  successfulEdits=bool(), scs=bool(), *args, **kwargs):
    pass


def referenceQuery(child=bool(), ch=bool(), dagPath=bool(), dp=bool(), editAttrs=bool(), ea=bool(), editCommand=str(),
                   ec=str(), editNodes=bool(), en=bool(), editStrings=bool(), es=bool(), failedEdits=bool(), fld=bool(),
                   filename=bool(), f=bool(), isExportEdits=bool(), iee=bool(), isLoaded=bool(), il=bool(),
                   isNodeReferenced=bool(), inr=bool(), isPreviewOnly=bool(), ipo=bool(), liveEdits=bool(), le=bool(),
                   namespace=bool(), ns=bool(), nodes=bool(), n=bool(), onReferenceNode=str(), orn=str(), parent=bool(),
                   p=bool(), parentNamespace=bool(), pns=bool(), referenceNode=bool(), rfn=bool(), shortName=bool(),
                   shn=bool(), showDagPath=bool(), sdp=bool(), showNamespace=bool(), sns=bool(), successfulEdits=bool(),
                   scs=bool(), topReference=bool(), tr=bool(), unresolvedName=bool(), un=bool(),
                   withoutCopyNumber=bool(), wcn=bool(), *args, **kwargs):
    pass


def refineSubdivSelectionList(*args, **kwargs):
    pass


def refresh(currentView=bool(), cv=bool(), fileExtension=str(), fe=str(), filename=str(), fn=str(), force=bool(),
            f=bool(), suspend=bool(), su=bool(), *args, **kwargs):
    pass


def refreshEditorTemplates(*args, **kwargs):
    pass


def regionSelectKeyCtx(bottomManip=float(), bot=float(), exists=bool(), ex=bool(), history=bool(), ch=bool(),
                       image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), leftManip=float(),
                       lft=float(), name=str(), n=str(), rightManip=float(), rgt=float(), topManip=float(), top=float(),
                       *args, **kwargs):
    pass


def relationship(b=bool(), relationshipData=str(), rd=str(), *args, **kwargs):
    pass


def reloadImage(*args, **kwargs):
    pass


def removeJoint(*args, **kwargs):
    pass


def removeMultiInstance(allChildren=bool(), all=bool(), b=bool(), *args, **kwargs):
    pass


def rename(ignoreShape=bool(), uuid=bool(), uid=bool(), *args, **kwargs):
    pass


def renameAttr(*args, **kwargs):
    pass


def renameUI(*args, **kwargs):
    pass


def render(abortMissingTexture=bool(), amt=bool(), batch=bool(), b=bool(), keepPreImage=bool(), kpi=bool(), layer=str(),
           l=str(), nglowpass=bool(), ngl=bool(), nshadows=bool(), nsh=bool(), replace=bool(), rep=bool(),
           xresolution=int(), x=int(), yresolution=int(), y=int(), *args, **kwargs):
    pass


def renderer(addGlobalsNode=str(), agn=str(), addGlobalsTab=list, agt=list, batchRenderOptionsProcedure=str(),
             bro=str(), batchRenderOptionsStringProcedure=str(), bso=str(), batchRenderProcedure=str(), br=str(),
             cancelBatchRenderProcedure=str(), cbr=str(), changeIprRegionProcedure=str(), cir=str(),
             commandRenderProcedure=str(), cr=str(), exists=bool(), ex=bool(), globalsNodes=bool(), gn=bool(),
             globalsTabCreateProcNames=bool(), gtc=bool(), globalsTabLabels=bool(), gtl=bool(),
             globalsTabUpdateProcNames=bool(), gtu=bool(), iprOptionsMenuLabel=str(), ipm=str(),
             iprOptionsProcedure=str(), io=str(), iprOptionsSubMenuProcedure=str(), ips=str(), iprRenderProcedure=str(),
             ipr=str(), iprRenderSubMenuProcedure=str(), irs=str(), isRunningIprProcedure=str(), isr=str(),
             logoCallbackProcedure=str(), lgc=str(), logoImageName=str(), log=str(), materialViewRendererList=bool(),
             mvl=bool(), materialViewRendererPause=bool(), mvp=bool(), materialViewRendererSuspend=bool(), mvs=bool(),
             namesOfAvailableRenderers=bool(), ava=bool(), pauseIprRenderProcedure=str(), psi=str(),
             polyPrelightProcedure=str(), pp=str(), refreshIprRenderProcedure=str(), rfi=str(),
             renderDiagnosticsProcedure=str(), rd=str(), renderGlobalsProcedure=str(), rg=str(),
             renderMenuProcedure=str(), rm=str(), renderOptionsProcedure=str(), ro=str(), renderProcedure=str(),
             r=str(), renderRegionProcedure=str(), rr=str(), renderSequenceProcedure=str(), rs=str(),
             rendererUIName=str(), ui=str(), renderingEditorsSubMenuProcedure=str(), res=str(),
             showBatchRenderLogProcedure=str(), brl=str(), showBatchRenderProcedure=str(), sbr=str(),
             showRenderLogProcedure=str(), srl=str(), startIprRenderProcedure=str(), sti=str(),
             stopIprRenderProcedure=str(), spi=str(), supportColorManagement=bool(), scm=bool(),
             textureBakingProcedure=str(), tb=str(), unregisterRenderer=bool(), unr=bool(), *args, **kwargs):
    pass


def renderGlobalsNode(name=str(), n=str(), parent=str(), p=str(), renderQuality=str(), rq=str(), renderResolution=str(),
                      rr=str(), shared=bool(), s=bool(), skipSelect=bool(), ss=bool(), *args, **kwargs):
    pass


def renderInfo(castShadows=bool(), cs=bool(), chordHeight=float(), ch=float(), chordHeightRatio=float(), chr=float(),
               doubleSided=bool(), ds=bool(), edgeSwap=bool(), es=bool(), minScreen=float(), ms=float(), name=str(),
               n=str(), opposite=bool(), o=bool(), smoothShading=bool(), ss=bool(), unum=int(), un=int(),
               useChordHeight=bool(), uch=bool(), useChordHeightRatio=bool(), ucr=bool(), useDefaultLights=bool(),
               udl=bool(), useMinScreen=bool(), ums=bool(), utype=int(), ut=int(), vnum=int(), vn=int(), vtype=int(),
               vt=int(), *args, **kwargs):
    pass


def renderLayerPostProcess(keepImages=bool(), ki=bool(), sceneName=str(), sn=str(), *args, **kwargs):
    pass


def renderManip(camera=list, cam=list, light=list, lt=list, spotLight=list, slt=list, state=bool(), st=bool(), *args,
                **kwargs):
    pass


def renderPartition(*args, **kwargs):
    pass


def renderPassRegistry(channels=int(), ch=int(), isPassSupported=bool(), ips=bool(), passID=str(), pi=str(),
                       passName=bool(), pn=bool(), renderer=str(), r=str(), supportedChannelCounts=bool(), scc=bool(),
                       supportedDataTypes=bool(), sdt=bool(), supportedPassSemantics=bool(), ps=bool(),
                       supportedRenderPassNames=bool(), spn=bool(), supportedRenderPasses=bool(), srp=bool(), *args,
                       **kwargs):
    pass


def renderQualityNode(name=str(), n=str(), parent=str(), p=str(), shared=bool(), s=bool(), skipSelect=bool(), ss=bool(),
                      *args, **kwargs):
    pass


def renderSettings(camera=str(), cam=str(), customTokenString=str(), cts=str(), firstImageName=bool(), fin=bool(),
                   fullPath=bool(), fp=bool(), fullPathTemp=bool(), fpt=bool(), genericFrameImageName=str(), gin=str(),
                   imageGenericName=bool(), ign=bool(), lastImageName=bool(), lin=bool(), layer=str(), lyr=str(),
                   leaveUnmatchedTokens=bool(), lut=bool(), *args, **kwargs):
    pass


def renderThumbnailUpdate(forceUpdate=str(), fu=str(), *args, **kwargs):
    pass


def renderWindowEditor(autoResize=bool(), ar=bool(), blendMode=int(), blm=int(), caption=str(), cap=str(),
                       changeCommand=list, cc=list, clear=list, cl=list, cmEnabled=bool(), cme=bool(),
                       colorManage=bool(), com=bool(), compDisplay=int(), cd=int(), compImageFile=str(), cif=str(),
                       control=bool(), ctl=bool(), currentCamera=str(), crc=str(), currentCameraRig=str(), crg=str(),
                       defineTemplate=str(), dt=str(), displayImage=int(), di=int(), displayImageViewCount=int(),
                       dvc=int(), displayStyle=str(), dst=str(), docTag=str(), dtg=str(), doubleBuffer=bool(),
                       dbf=bool(), drawAxis=bool(), da=bool(), editorName=bool(), en=bool(), exists=bool(), ex=bool(),
                       exposure=float(), exp=float(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(),
                       frameImage=bool(), fi=bool(), frameRegion=bool(), fr=bool(), gamma=float(), ga=float(),
                       highlightConnection=str(), hlc=str(), loadImage=str(), li=str(), lockMainConnection=bool(),
                       lck=bool(), mainListConnection=str(), mlc=str(), marquee=list, mq=list, nbImages=bool(),
                       nim=bool(), nextViewImage=bool(), nvi=bool(), outputColorManage=bool(), ocm=bool(), panel=str(),
                       pnl=str(), parent=str(), p=str(), pcaption=str(), pca=str(), realSize=bool(), rs=bool(),
                       refresh=bool(), ref=bool(), removeAllImages=bool(), ra=bool(), removeImage=bool(), ri=bool(),
                       resetRegion=bool(), rr=bool(), resetViewImage=bool(), rvi=bool(), saveImage=bool(), si=bool(),
                       scaleBlue=float(), sb=float(), scaleGreen=float(), sg=float(), scaleRed=float(), sr=float(),
                       selectionConnection=str(), slc=str(), showRegion=list, srg=list, singleBuffer=bool(), sbf=bool(),
                       snapshot=list, snp=list, snapshotMode=bool(), snm=bool(), stateString=bool(), sts=bool(),
                       stereo=int(), s=int(), stereoImageOrientation=list, sio=list, stereoMode=str(), sm=str(),
                       toggle=bool(), tgl=bool(), unParent=bool(), up=bool(), unlockMainConnection=bool(), ulk=bool(),
                       updateMainConnection=bool(), upd=bool(), useTemplate=str(), ut=str(), viewImageCount=int(),
                       vic=int(), viewTransformName=str(), vtn=str(), writeImage=str(), wi=str(), *args, **kwargs):
    pass


def renderWindowSelectContext(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(),
                              i3=str(), *args, **kwargs):
    pass


def reorder(back=bool(), b=bool(), front=bool(), f=bool(), relative=int(), r=int(), *args, **kwargs):
    pass


def reorderContainer(back=bool(), b=bool(), front=bool(), f=bool(), relative=int(), r=int(), *args, **kwargs):
    pass


def reorderDeformers(name=str(), n=str(), *args, **kwargs):
    pass


def requires(dataType=str(), dt=str(), nodeType=str(), nt=str(), *args, **kwargs):
    pass


def reroot(*args, **kwargs):
    pass


def resampleFluid(resampleDepth=int(), rd=int(), resampleHeight=int(), rh=int(), resampleWidth=int(), rw=int(), *args,
                  **kwargs):
    pass


def resetTool(*args, **kwargs):
    pass


def resolutionNode(name=str(), n=str(), parent=str(), p=str(), shared=bool(), s=bool(), skipSelect=bool(), ss=bool(),
                   *args, **kwargs):
    pass


def resourceManager(nameFilter=str(), nf=str(), saveAs=list, s=list, *args, **kwargs):
    pass


def retimeKeyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                 image3=str(), i3=str(), moveByFrame=int(), mbf=int(), name=str(), n=str(), snapOnFrame=bool(),
                 sof=bool(), *args, **kwargs):
    pass


def reverseCurve(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), curveOnSurface=bool(), cos=bool(),
                 name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), range=bool(), rn=bool(),
                 replaceOriginal=bool(), rpo=bool(), *args, **kwargs):
    pass


def reverseSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), direction=int(), d=int(),
                   name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), replaceOriginal=bool(),
                   rpo=bool(), *args, **kwargs):
    pass


def revolve(autoCorrectNormal=bool(), acn=bool(), axis=list, ax=list, axisChoice=int(), aco=int(), axisX=float(),
            axx=float(), axisY=float(), axy=float(), axisZ=float(), axz=float(), bridge=bool(), br=bool(),
            caching=bool(), cch=bool(), computePivotAndAxis=int(), cpa=int(), constructionHistory=bool(), ch=bool(),
            degree=int(), d=int(), endSweep=float(), esw=float(), name=str(), n=str(), nodeState=int(), nds=int(),
            object=bool(), o=bool(), pivot=list, p=list, pivotX=float(), px=float(), pivotY=float(), py=float(),
            pivotZ=float(), pz=float(), polygon=int(), po=int(), radius=float(), r=float(), radiusAnchor=float(),
            ra=float(), range=bool(), rn=bool(), rebuild=bool(), rb=bool(), sections=int(), s=int(), startSweep=float(),
            ssw=float(), tolerance=float(), tol=float(), useLocalPivot=bool(), ulp=bool(), useTolerance=bool(),
            ut=bool(), *args, **kwargs):
    pass


def rigidBody(active=bool(), act=bool(), angularVelocity=bool(), av=bool(), applyForceAt=str(), afa=str(),
              bounciness=float(), b=float(), cache=bool(), c=bool(), centerOfMass=list, com=list, collisions=bool(),
              cl=bool(), contactCount=bool(), cc=bool(), contactName=bool(), cn=bool(), contactPosition=bool(),
              cp=bool(), damping=float(), dp=float(), deleteCache=bool(), dc=bool(), dynamicFriction=float(),
              df=float(), force=bool(), f=bool(), ignore=bool(), ig=bool(), impulse=list, i=list, impulsePosition=list,
              imp=list, initialAngularVelocity=list, iav=list, initialVelocity=list, iv=list, layer=int(), l=int(),
              lockCenterOfMass=bool(), lcm=bool(), mass=float(), m=float(), name=str(), n=str(), orientation=list,
              o=list, particleCollision=bool(), pc=bool(), passive=bool(), pas=bool(), position=list, p=list,
              removeShape=str(), rs=str(), solver=str(), slv=str(), spinImpulse=list, si=list, standInObject=str(),
              sio=str(), staticFriction=float(), sf=float(), tesselationFactor=int(), tf=int(), velocity=bool(),
              vel=bool(), *args, **kwargs):
    pass


def rigidSolver(autoTolerances=bool(), at=bool(), bounciness=bool(), b=bool(), cacheData=bool(), cd=bool(),
                collide=bool(), c=bool(), collisionTolerance=float(), ct=float(), contactData=bool(), ctd=bool(),
                create=bool(), cr=bool(), current=bool(), cu=bool(), deleteCache=bool(), displayCenterOfMass=bool(),
                dcm=bool(), displayConstraint=bool(), dc=bool(), displayVelocity=bool(), dv=bool(), dynamics=bool(),
                d=bool(), friction=bool(), f=bool(), interpenetrate=bool(), i=bool(), interpenetrationCheck=bool(),
                ic=bool(), name=str(), n=str(), rigidBodies=bool(), rb=bool(), rigidBodyCount=bool(), rbc=bool(),
                showCollision=bool(), sc=bool(), showInterpenetration=bool(), si=bool(), solverMethod=int(), sm=int(),
                startTime=float(), stt=float(), state=bool(), st=bool(), statistics=bool(), sta=bool(),
                stepSize=float(), s=float(), velocityVectorScale=float(), vs=float(), *args, **kwargs):
    pass


def roll(absolute=bool(), abs=bool(), degree=float(), d=float(), relative=bool(), rel=bool(), *args, **kwargs):
    pass


def rollCtx(alternateContext=bool(), ac=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
            i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), rollScale=float(),
            rs=float(), toolName=str(), tn=str(), *args, **kwargs):
    pass


def rotate(absolute=bool(), a=bool(), centerPivot=bool(), cp=bool(), componentSpace=bool(), cs=bool(),
           constrainAlongNormal=bool(), xn=bool(), deletePriorHistory=bool(), dph=bool(), euler=bool(), eu=bool(),
           forceOrderXYZ=bool(), fo=bool(), objectCenterPivot=bool(), ocp=bool(), objectSpace=bool(), os=bool(),
           orientAxes=list, oa=list, pivot=list, p=list, preserveChildPosition=bool(), pcp=bool(),
           preserveGeometryPosition=bool(), pgp=bool(), preserveUV=bool(), puv=bool(), reflection=bool(), rfl=bool(),
           reflectionAboutBBox=bool(), rab=bool(), reflectionAboutOrigin=bool(), rao=bool(), reflectionAboutX=bool(),
           rax=bool(), reflectionAboutY=bool(), ray=bool(), reflectionAboutZ=bool(), raz=bool(),
           reflectionTolerance=float(), rft=float(), relative=bool(), r=bool(), rotateX=bool(), x=bool(),
           rotateXY=bool(), xy=bool(), rotateXYZ=bool(), xyz=bool(), rotateXZ=bool(), xz=bool(), rotateY=bool(),
           y=bool(), rotateYZ=bool(), yz=bool(), rotateZ=bool(), z=bool(), symNegative=bool(), smn=bool(),
           translate=bool(), t=bool(), worldSpace=bool(), ws=bool(), xformConstraint=str(), xc=str(), *args, **kwargs):
    pass


def rotationInterpolation(convert=str(), c=str(), *args, **kwargs):
    pass


def roundConstantRadius(append=bool(), a=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                        object=bool(), o=bool(), radiuss=float(), rad=float(), side=list, s=list, sidea=int(), sa=int(),
                        sideb=int(), sb=int(), *args, **kwargs):
    pass


def rowColumnLayout(adjustableColumn=int(), adj=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                    childArray=bool(), ca=bool(), columnAlign=list, cal=list, columnAttach=list, cat=list,
                    columnOffset=list, co=list, columnSpacing=list, cs=list, columnWidth=list, cw=list,
                    defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                    dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                    enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(),
                    height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(), io=bool(), manage=bool(),
                    m=bool(), noBackground=bool(), nbg=bool(), numberOfChildren=bool(), nch=bool(),
                    numberOfColumns=int(), nc=int(), numberOfPopupMenus=bool(), npm=bool(), numberOfRows=int(),
                    nr=int(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(),
                    po=bool(), rowAlign=list, ral=list, rowAttach=list, rat=list, rowHeight=list, rh=list,
                    rowOffset=list, ro=list, rowSpacing=list, rs=list, statusBarMessage=str(), sbm=str(),
                    useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                    width=int(), w=int(), *args, **kwargs):
    pass


def rowLayout(adjustableColumn=int(), adj=int(), adjustableColumn1=int(), ad1=int(), adjustableColumn2=int(), ad2=int(),
              adjustableColumn3=int(), ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(),
              ad5=int(), adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list,
              bgc=list, childArray=bool(), ca=bool(), columnAlign=list, cal=list, columnAlign1=str(), cl1=str(),
              columnAlign2=list, cl2=list, columnAlign3=list, cl3=list, columnAlign4=list, cl4=list, columnAlign5=list,
              cl5=list, columnAlign6=list, cl6=list, columnAttach=list, cat=list, columnAttach1=str(), ct1=str(),
              columnAttach2=list, ct2=list, columnAttach3=list, ct3=list, columnAttach4=list, ct4=list,
              columnAttach5=list, ct5=list, columnAttach6=list, ct6=list, columnOffset1=int(), co1=int(),
              columnOffset2=list, co2=list, columnOffset3=list, co3=list, columnOffset4=list, co4=list,
              columnOffset5=list, co5=list, columnOffset6=list, co6=list, columnWidth=list, cw=list, columnWidth1=int(),
              cw1=int(), columnWidth2=list, cw2=list, columnWidth3=list, cw3=list, columnWidth4=list, cw4=list,
              columnWidth5=list, cw5=list, columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(),
              dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
              enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
              fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(),
              io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), numberOfChildren=bool(), nch=bool(),
              numberOfColumns=int(), nc=int(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
              popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rowAttach=list, rat=list,
              statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
              visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def runTimeCommand(addKeyword=str(), ak=str(), addTag=str(), at=str(), annotation=str(), ann=str(), category=str(),
                   cat=str(), categoryArray=bool(), caa=bool(), command=str(), c=str(), commandArray=bool(), ca=bool(),
                   commandLanguage=str(), cl=str(), default=bool(), d=bool(), defaultCommandArray=bool(), dca=bool(),
                   delete=bool(), exists=bool(), ex=bool(), helpUrl=str(), url=str(), hotkeyCtx=str(), hc=str(),
                   image=str(), i=str(), keywords=str(), k=str(), label=str(), l=str(), longAnnotation=str(), la=str(),
                   numberOfCommands=bool(), nc=bool(), numberOfDefaultCommands=bool(), ndc=bool(),
                   numberOfUserCommands=bool(), nuc=bool(), plugin=str(), p=str(), save=bool(), s=bool(),
                   showInHotkeyEditor=bool(), she=bool(), tags=str(), t=str(), userCommandArray=bool(), uca=bool(),
                   *args, **kwargs):
    pass


def runup(cache=bool(), cch=bool(), fromPreviousFrame=bool(), fpf=bool(), fromStartFrame=bool(), fsf=bool(),
          maxFrame=float(), mxf=float(), state=bool(), st=bool(), *args, **kwargs):
    pass


def sampleImage(fastSample=bool(), f=bool(), resolution=list, r=list, *args, **kwargs):
    pass


def saveAllShelves(*args, **kwargs):
    pass


def saveFluid(currentTime=int(), ct=int(), endTime=int(), et=int(), startTime=int(), st=int(), *args, **kwargs):
    pass


def saveImage(annotation=str(), ann=str(), backgroundColor=list, bgc=list, currentView=bool(), cv=bool(),
              defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
              dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
              enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(),
              height=int(), h=int(), highlightColor=list, hlc=list, image=str(), i=str(), isObscured=bool(), io=bool(),
              manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(),
              objectThumbnail=str(), ot=str(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
              preventOverride=bool(), po=bool(), sceneFile=str(), sf=str(), statusBarMessage=str(), sbm=str(),
              useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
              width=int(), w=int(), *args, **kwargs):
    pass


def saveInitialState(attribute=str(), atr=str(), saveall=bool(), all=bool(), *args, **kwargs):
    pass


def saveMenu(*args, **kwargs):
    pass


def savePrefObjects(*args, **kwargs):
    pass


def savePrefs(colors=bool(), c=bool(), general=bool(), g=bool(), hotkeys=bool(), hk=bool(), menuSets=bool(), ms=bool(),
              plugins=bool(), pl=bool(), uiLayout=bool(), ui=bool(), *args, **kwargs):
    pass


def saveShelf(*args, **kwargs):
    pass


def saveToolSettings(*args, **kwargs):
    pass


def saveViewportSettings(*args, **kwargs):
    pass


def scale(absolute=bool(), a=bool(), centerPivot=bool(), cp=bool(), componentSpace=bool(), cs=bool(),
          constrainAlongNormal=bool(), xn=bool(), deletePriorHistory=bool(), dph=bool(), distanceOnly=bool(),
          dso=bool(), localSpace=bool(), ls=bool(), objectCenterPivot=bool(), ocp=bool(), objectSpace=bool(), os=bool(),
          orientAxes=list, oa=list, pivot=list, p=list, preserveChildPosition=bool(), pcp=bool(),
          preserveGeometryPosition=bool(), pgp=bool(), preserveUV=bool(), puv=bool(), reflection=bool(), rfl=bool(),
          reflectionAboutBBox=bool(), rab=bool(), reflectionAboutOrigin=bool(), rao=bool(), reflectionAboutX=bool(),
          rax=bool(), reflectionAboutY=bool(), ray=bool(), reflectionAboutZ=bool(), raz=bool(),
          reflectionTolerance=float(), rft=float(), relative=bool(), r=bool(), scaleX=bool(), x=bool(), scaleXY=bool(),
          xy=bool(), scaleXYZ=bool(), xyz=bool(), scaleXZ=bool(), xz=bool(), scaleY=bool(), y=bool(), scaleYZ=bool(),
          yz=bool(), scaleZ=bool(), z=bool(), symNegative=bool(), smn=bool(), worldSpace=bool(), ws=bool(),
          xformConstraint=str(), xc=str(), *args, **kwargs):
    pass


def scaleComponents(pivot=list, p=list, rotation=list, ro=list, *args, **kwargs):
    pass


def scaleConstraint(layer=str(), l=str(), maintainOffset=bool(), mo=bool(), name=str(), n=str(), offset=list, o=list,
                    remove=bool(), rm=bool(), scaleCompensate=bool(), sc=bool(), skip=str(), sk=str(),
                    targetList=bool(), tl=bool(), weight=float(), w=float(), weightAliasList=bool(), wal=bool(), *args,
                    **kwargs):
    pass


def scaleKey(animation=str(), an=str(), attribute=str(), at=str(), autoSnap=bool(), asp=bool(), controlPoints=bool(),
             cp=bool(), float=tuple(), f=tuple(), floatPivot=float(), fp=float(), floatScale=float(), fs=float(),
             hierarchy=str(), hi=str(), includeUpperBound=bool(), iub=bool(), index=int(), newEndFloat=float(),
             nef=float(), newEndTime=float(), net=float(), newStartFloat=float(), nsf=float(), newStartTime=float(),
             nst=float(), scaleSpecifiedKeys=bool(), ssk=bool(), shape=bool(), s=bool(), time=tuple(), t=tuple(),
             timePivot=float(), tp=float(), timeScale=float(), ts=float(), valuePivot=float(), vp=float(),
             valueScale=float(), vs=float(), *args, **kwargs):
    pass


def scaleKeyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                image3=str(), i3=str(), name=str(), n=str(), scaleSpecifiedKeys=bool(), ssk=bool(), type=str(),
                typ=str(), *args, **kwargs):
    pass


def sceneEditor(control=bool(), ctl=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), exists=bool(),
                ex=bool(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(), highlightConnection=str(),
                hlc=str(), lockMainConnection=bool(), lck=bool(), mainListConnection=str(), mlc=str(),
                onlyParents=bool(), op=bool(), panel=str(), pnl=str(), parent=str(), p=str(), refreshReferences=bool(),
                rr=bool(), selectCommand=str(), sc=str(), selectItem=int(), si=int(), selectReference=str(), sr=str(),
                selectionConnection=str(), slc=str(), shortName=bool(), shn=bool(), stateString=bool(), sts=bool(),
                unParent=bool(), up=bool(), unlockMainConnection=bool(), ulk=bool(), unresolvedName=bool(), un=bool(),
                updateMainConnection=bool(), upd=bool(), useTemplate=str(), ut=str(), withoutCopyNumber=bool(),
                wcn=bool(), *args, **kwargs):
    pass


def sceneLint(issueType=str(), i=str(), verbose=bool(), v=bool(), *args, **kwargs):
    pass


def sceneUIReplacement(clear=bool(), cl=bool(), deleteRemaining=bool(), dr=bool(), getNextFilter=list, gf=list,
                       getNextPanel=list, gp=list, getNextScriptedPanel=list, gsp=list, update=str(), u=str(), *args,
                       **kwargs):
    pass


def scmh(absolute=bool(), a=bool(), ignore=int(), i=int(), quiet=bool(), q=bool(), relative=bool(), r=bool(), *args,
         **kwargs):
    pass


def scriptCtx(allComponents=bool(), alc=bool(), allObjects=bool(), alo=bool(), animBreakdown=bool(), abd=bool(),
              animCurve=bool(), ac=bool(), animInTangent=bool(), ait=bool(), animKeyframe=bool(), ak=bool(),
              animOutTangent=bool(), aot=bool(), baseClassName=str(), bcn=str(), camera=bool(), ca=bool(),
              cluster=bool(), cl=bool(), collisionModel=bool(), clm=bool(), controlVertex=bool(), cv=bool(),
              cumulativeLists=bool(), cls=bool(), curve=bool(), c=bool(), curveKnot=bool(), ck=bool(),
              curveOnSurface=bool(), cos=bool(), curveParameterPoint=bool(), cpp=bool(), dimension=bool(), dim=bool(),
              dynamicConstraint=bool(), dc=bool(), edge=bool(), eg=bool(), editPoint=bool(), ep=bool(), emitter=bool(),
              em=bool(), enableRootSelection=bool(), ers=bool(), escToQuit=bool(), esc=bool(), exists=bool(), ex=bool(),
              exitUponCompletion=bool(), euc=bool(), expandSelectionList=bool(), esl=bool(), facet=bool(), fc=bool(),
              field=bool(), fi=bool(), finalCommandScript=str(), fcs=str(), fluid=bool(), fl=bool(), follicle=bool(),
              fo=bool(), forceAddSelect=bool(), fas=bool(), hairSystem=bool(), hs=bool(), handle=bool(), ha=bool(),
              history=bool(), ch=bool(), hull=bool(), hl=bool(), ignoreInvalidItems=bool(), iii=bool(),
              ikEndEffector=bool(), iee=bool(), ikHandle=bool(), ikh=bool(), image1=str(), i1=str(), image2=str(),
              i2=str(), image3=str(), i3=str(), imagePlane=bool(), ip=bool(), implicitGeometry=bool(), ig=bool(),
              isoparm=bool(), iso=bool(), joint=bool(), j=bool(), jointPivot=bool(), jp=bool(), lastAutoComplete=bool(),
              lac=bool(), lattice=bool(), la=bool(), latticePoint=bool(), lp=bool(), light=bool(), lt=bool(),
              localRotationAxis=bool(), ra=bool(), locator=bool(), lc=bool(), locatorUV=bool(), luv=bool(),
              locatorXYZ=bool(), xyz=bool(), nCloth=bool(), ncl=bool(), nParticle=bool(), npr=bool(),
              nParticleShape=bool(), nps=bool(), nRigid=bool(), nr=bool(), name=str(), n=str(), nonlinear=bool(),
              nl=bool(), nurbsCurve=bool(), nc=bool(), nurbsSurface=bool(), ns=bool(), objectComponent=bool(),
              ocm=bool(), orientationLocator=bool(), ol=bool(), particle=bool(), pr=bool(), particleShape=bool(),
              ps=bool(), plane=bool(), pl=bool(), polymesh=bool(), p=bool(), polymeshEdge=bool(), pe=bool(),
              polymeshFace=bool(), pf=bool(), polymeshFreeEdge=bool(), pfe=bool(), polymeshUV=bool(), puv=bool(),
              polymeshVertex=bool(), pv=bool(), polymeshVtxFace=bool(), pvf=bool(), rigidBody=bool(), rb=bool(),
              rigidConstraint=bool(), rc=bool(), rotatePivot=bool(), rp=bool(), scalePivot=bool(), sp=bool(),
              sculpt=bool(), sc=bool(), selectHandle=bool(), sh=bool(), setAllowExcessCount=bool(), sae=bool(),
              setAutoComplete=bool(), sac=bool(), setAutoToggleSelection=bool(), sat=bool(),
              setDoneSelectionPrompt=str(), dsp=str(), setNoSelectionHeadsUp=str(), snh=str(),
              setNoSelectionPrompt=str(), snp=str(), setSelectionCount=int(), ssc=int(), setSelectionHeadsUp=str(),
              ssh=str(), setSelectionPrompt=str(), ssp=str(), showManipulators=bool(), sm=bool(), spring=bool(),
              spr=bool(), springComponent=bool(), spc=bool(), stroke=bool(), str=bool(), subdiv=bool(), sd=bool(),
              subdivMeshEdge=bool(), sme=bool(), subdivMeshFace=bool(), smf=bool(), subdivMeshPoint=bool(), smp=bool(),
              subdivMeshUV=bool(), smu=bool(), surfaceEdge=bool(), se=bool(), surfaceFace=bool(), sf=bool(),
              surfaceKnot=bool(), sk=bool(), surfaceParameterPoint=bool(), spp=bool(), surfaceRange=bool(), sr=bool(),
              surfaceUV=bool(), suv=bool(), texture=bool(), tx=bool(), title=str(), t=str(), toolCursorType=str(),
              tct=str(), toolFinish=str(), tf=str(), toolStart=str(), ts=str(), totalSelectionSets=int(), tss=int(),
              vertex=bool(), v=bool(), *args, **kwargs):
    pass


def scriptEditorInfo(clearHistory=bool(), ch=bool(), clearHistoryFile=bool(), chf=bool(), historyFilename=str(),
                     hfn=str(), input=str(), i=str(), suppressErrors=bool(), se=bool(), suppressInfo=bool(), si=bool(),
                     suppressResults=bool(), sr=bool(), suppressStackWindow=bool(), ssw=bool(), suppressWarnings=bool(),
                     sw=bool(), writeHistory=bool(), wh=bool(), *args, **kwargs):
    pass


def scriptedPanel(control=bool(), ctl=bool(), copy=str(), cp=str(), createString=bool(), cs=bool(),
                  defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), editString=bool(), es=bool(), exists=bool(),
                  ex=bool(), init=bool(), isUnique=bool(), iu=bool(), label=str(), l=str(), menuBarRepeatLast=bool(),
                  mrl=bool(), menuBarVisible=bool(), mbv=bool(), needsInit=bool(), ni=bool(), parent=str(), p=str(),
                  popupMenuProcedure=str(), pmp=str(), replacePanel=str(), rp=str(), tearOff=bool(), to=bool(),
                  tearOffCopy=str(), toc=str(), tearOffRestore=bool(), tor=bool(), type=str(), typ=str(),
                  unParent=bool(), up=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def scriptedPanelType(addCallback=str(), acb=str(), copyStateCallback=str(), ocb=str(), createCallback=str(), ccb=str(),
                      customView=bool(), cv=bool(), defineTemplate=str(), dt=str(), deleteCallback=str(), dcb=str(),
                      exists=bool(), ex=bool(), hotkeyCtxClient=str(), hkc=str(), initCallback=str(), icb=str(),
                      label=str(), l=str(), obsolete=bool(), o=bool(), removeCallback=str(), rcb=str(),
                      retainOnFileOpen=bool(), rfo=bool(), saveStateCallback=str(), scb=str(), unique=bool(), u=bool(),
                      useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def scriptJob(allChildren=bool(), alc=bool(), attributeAdded=list, aa=list, attributeChange=list, ac=list,
              attributeDeleted=list, ad=list, compressUndo=bool(), cu=bool(), conditionChange=list, cc=list,
              conditionFalse=list, cf=list, conditionTrue=list, ct=list, connectionChange=list, con=list,
              disregardIndex=bool(), dri=bool(), event=list, e=list, exists=int(), ex=int(), force=bool(), f=bool(),
              idleEvent=str(), ie=str(), kill=int(), k=int(), killAll=bool(), ka=bool(), killWithScene=bool(),
              kws=bool(), listConditions=bool(), lc=bool(), listEvents=bool(), le=bool(), listJobs=bool(), lj=bool(),
              nodeDeleted=list, nd=list, nodeNameChanged=list, nnc=list, optionVarChanged=list, ovc=list, parent=str(),
              p=str(), permanent=bool(), per=bool(), protected=bool(), pro=bool(), replacePrevious=bool(), rp=bool(),
              runOnce=bool(), ro=bool(), timeChange=str(), tc=str(), uiDeleted=list, uid=list, *args, **kwargs):
    pass


def scriptNode(afterScript=str(), beforeScript=str(), bs=str(), executeAfter=bool(), ea=bool(), executeBefore=bool(),
               eb=bool(), ignoreReferenceEdits=bool(), ire=bool(), name=str(), n=str(), scriptType=int(), st=int(),
               sourceType=str(), stp=str(), *args, **kwargs):
    pass


def scriptTable(afterCellChangedCmd=str(), acc=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                cellBackgroundColorCommand=str(), cbc=str(), cellChangedCmd=str(), ccc=str(),
                cellForegroundColorCommand=str(), cfc=str(), cellIndex=list, ci=list, cellValue=str(), cv=str(),
                clearRow=int(), cr=int(), clearTable=bool(), ct=bool(), columnFilter=list, cf=list, columnWidth=list,
                cw=list, columns=int(), c=int(), defineTemplate=str(), dt=str(), deleteRow=int(), dr=int(),
                docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), editable=bool(),
                ed=bool(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                ekf=bool(), excludingHeaders=bool(), eh=bool(), exists=bool(), ex=bool(), fullPathName=bool(),
                fpn=bool(), getCellCmd=str(), gcc=str(), height=int(), h=int(), highlightColor=list, hlc=list,
                insertRow=int(), ir=int(), isObscured=bool(), io=bool(), label=list, l=list, manage=bool(), m=bool(),
                multiEditEnabled=bool(), mee=bool(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(),
                npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
                rowHeight=int(), rh=int(), rows=int(), r=int(), rowsRemovedCmd=str(), rrc=str(),
                rowsToBeRemovedCmd=str(), rtc=str(), selectedCells=list, sc=list, selectedColumns=list, scs=list,
                selectedRow=bool(), sr=bool(), selectedRows=list, srs=list, selectionBehavior=int(), sb=int(),
                selectionChangedCmd=str(), scc=str(), selectionMode=int(), sm=int(), sortEnabled=bool(), se=bool(),
                statusBarMessage=str(), sbm=str(), underPointerColumn=bool(), upc=bool(), underPointerRow=bool(),
                upr=bool(), useDoubleClickEdit=bool(), udc=bool(), useTemplate=str(), ut=str(), visible=bool(),
                vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def scrollField(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(),
                clear=bool(), cl=bool(), command=str(), c=str(), defineTemplate=str(), dt=str(), docTag=str(),
                dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), editable=bool(), ed=bool(),
                enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(),
                enterCommand=str(), ec=str(), exists=bool(), ex=bool(), font=str(), fn=str(), fontPointSize=int(),
                fns=int(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                insertText=str(), it=str(), insertionPosition=int(), ip=int(), isObscured=bool(), io=bool(),
                keyPressCommand=str(), kpc=str(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                numberOfLines=int(), nl=int(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), qtFont=str(), qfn=str(),
                selection=bool(), sl=bool(), statusBarMessage=str(), sbm=str(), text=str(), tx=str(), useTemplate=str(),
                ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
                wordWrap=bool(), ww=bool(), *args, **kwargs):
    pass


def scrollLayout(annotation=str(), ann=str(), backgroundColor=list, bgc=list, borderVisible=bool(), bv=bool(),
                 childArray=bool(), ca=bool(), childResizable=bool(), cr=bool(), defineTemplate=str(), dt=str(),
                 docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
                 en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                 ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                 horizontalScrollBarThickness=int(), hst=int(), isObscured=bool(), io=bool(), manage=bool(), m=bool(),
                 minChildWidth=int(), mcw=int(), noBackground=bool(), nbg=bool(), numberOfChildren=bool(), nch=bool(),
                 numberOfPopupMenus=bool(), npm=bool(), panEnabled=bool(), pe=bool(), parent=str(), p=str(),
                 popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), resizeCommand=str(), rc=str(),
                 scrollAreaHeight=bool(), sah=bool(), scrollAreaValue=bool(), sav=bool(), scrollAreaWidth=bool(),
                 saw=bool(), scrollByPixel=list, sbp=list, scrollPage=str(), sp=str(), statusBarMessage=str(),
                 sbm=str(), useTemplate=str(), ut=str(), verticalScrollBarAlwaysVisible=bool(), vsb=bool(),
                 verticalScrollBarThickness=int(), vst=int(), visible=bool(), vis=bool(), visibleChangeCommand=str(),
                 vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def sculpt(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(), deformerTools=bool(),
           dt=bool(), dropoffDistance=float(), dds=float(), dropoffType=str(), drt=str(), exclusive=str(), ex=str(),
           frontOfChain=bool(), foc=bool(), geometry=str(), g=str(), geometryIndices=bool(), gi=bool(),
           groupWithLocator=bool(), gwl=bool(), ignoreSelected=bool(), includeHiddenSelections=bool(), ihs=bool(),
           insideMode=str(), im=str(), maxDisplacement=float(), mxd=float(), mode=str(), m=str(), name=str(), n=str(),
           objectCentered=bool(), oc=bool(), parallel=bool(), par=bool(), prune=bool(), pr=bool(), remove=bool(),
           rm=bool(), sculptTool=str(), st=str(), split=bool(), sp=bool(), useComponentTags=bool(), uct=bool(), *args,
           **kwargs):
    pass


def sculptMeshCacheChangeCloneSource(blendShape=str(), bs=str(), target=str(), t=str(), *args, **kwargs):
    pass


def sculptMeshCacheCtx(adjustSize=bool(), asz=bool(), adjustStrength=bool(), ast=bool(), affectAllLayers=bool(),
                       aal=bool(), brushDirection=int(), bd=int(), brushSize=float(), bsz=float(),
                       brushStrength=float(), bst=float(), buildUpRate=float(), bur=float(), cloneHideSource=bool(),
                       chs=bool(), cloneMethod=int(), cm=int(), cloneShapeSource=str(), css=str(),
                       cloneTargetSource=str(), cas=str(), constrainToSurface=bool(), cts=bool(), direction=int(),
                       d=int(), displayFrozen=bool(), df=bool(), displayMask=bool(), dm=bool(), displayWireframe=bool(),
                       dw=bool(), falloffType=int(), ft=int(), flood=float(), fl=float(), floodFreeze=float(),
                       ff=float(), frame=bool(), frm=bool(), freezeSelection=bool(), fsl=bool(), grabFollowPath=bool(),
                       gfp=bool(), grabSilhouette=bool(), gs=bool(), grabTwist=bool(), gtw=bool(), inverted=bool(),
                       inv=bool(), lastMode=str(), lm=str(), lockShellBorder=bool(), lsb=bool(), makeStroke=list,
                       mt=list, minSize=float(), msz=float(), minStrength=float(), mst=float(), mirror=int(), mr=int(),
                       mode=str(), m=str(), orientToSurface=bool(), ots=bool(), recordStroke=bool(), rcs=bool(),
                       sculptFalloffCurve=str(), sfc=str(), size=float(), sz=float(), stampDistance=float(), s=float(),
                       stampFile=str(), stp=str(), stampFlipX=bool(), sfx=bool(), stampFlipY=bool(), sfy=bool(),
                       stampOrientToStroke=bool(), sos=bool(), stampPlacement=int(), sp=int(),
                       stampRandomization=bool(), srd=bool(), stampRandomizationSeed=int(), sre=int(),
                       stampRandomizeFlipX=bool(), srx=bool(), stampRandomizeFlipY=bool(), sry=bool(),
                       stampRandomizePosX=float(), spx=float(), stampRandomizePosY=float(), spy=float(),
                       stampRandomizeRotation=float(), srr=float(), stampRandomizeScale=float(), src=float(),
                       stampRandomizeStrength=float(), srs=float(), stampRotation=float(), sr=float(),
                       steadyStrokeDistance=float(), ssd=float(), strength=float(), st=float(), updatePlane=bool(),
                       upl=bool(), useGlobalSize=bool(), ugs=bool(), useScreenSpace=bool(), ssp=bool(),
                       useStampDistance=bool(), usd=bool(), useStampImage=bool(), usi=bool(), useSteadyStroke=bool(),
                       uss=bool(), wholeStroke=bool(), wst=bool(), wireframeAlpha=float(), wa=float(),
                       wireframeColor=list, wc=list, *args, **kwargs):
    pass


def sculptTarget(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(),
                 deformerTools=bool(), dt=bool(), exclusive=str(), ex=str(), frontOfChain=bool(), foc=bool(),
                 geometry=str(), g=str(), geometryIndices=bool(), gi=bool(), ignoreSelected=bool(),
                 inbetweenWeight=float(), ibw=float(), includeHiddenSelections=bool(), ihs=bool(), name=str(), n=str(),
                 parallel=bool(), par=bool(), prune=bool(), pr=bool(), regenerate=bool(), r=bool(), remove=bool(),
                 rm=bool(), snapshot=int(), s=int(), split=bool(), sp=bool(), target=int(), t=int(),
                 useComponentTags=bool(), uct=bool(), *args, **kwargs):
    pass


def select(*args, names=None, add=bool(), addFirst=bool(), af=bool(), all:bool=None, allDagObjects=bool(), ado=bool(),
           allDependencyNodes=bool(), adn=bool(), clear=bool(), cl=bool(), containerCentric=bool(), cc=bool(),
           deselect=bool(), d=bool(), hierarchy=bool(), hi=bool(), noExpand=bool(), ne=bool(), replace=True, r=True,
           symmetry=bool(), sym=bool(), symmetrySide=int(), sys=int(), toggle=bool(), tgl=bool(), visible=bool(),
           vis=bool()):

    from builtins import all as _all

    if clear == True or cl == True:
        ACTIVE_SELECTION.clear()
        return

    elif deselect == True or d == True:
        for nd in args:
            item = _hierarchy.NodePool.from_name(nd)
            if item in ACTIVE_SELECTION:
                ACTIVE_SELECTION.remove(item)
                
    if all is True or names is None or names is None and all is None:
        items = list(_hierarchy.NodePool.all_nodes())

    if names and isinstance(names, str):
        names = [names]
        items = [_hierarchy.NodePool.from_name(i) for i in names]
    
    if toggle == True or tgl == True:
        for item in [x for x in items if x in ACTIVE_SELECTION]:
            ACTIVE_SELECTION.remove(item)

    if hierarchy == True or hi == True:
        descendants = []
        for item in items:
            dag_path = om.MDagPath()
            dag_path._node = item
            descendants.extend(dag_path._iter_descendants())
        items.extend(descendants)

    elif add == True:
        ACTIVE_SELECTION.extend(items)

    elif addFirst == True or af == True:
        sel = items.extend(ACTIVE_SELECTION.as_list)
        ACTIVE_SELECTION.replace_all(sel)

    elif _all((replace, r)):
        ACTIVE_SELECTION.replace_all(items)
        

def selectContext(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                  image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def selectionConnection(activeCacheList=bool(), atc=bool(), activeCharacterList=bool(), acl=bool(), activeList=bool(),
                        act=bool(), addScript=str(), addTo=str(), add=str(), characterList=bool(), cl=bool(),
                        clear=bool(), clr=bool(), connectionList=bool(), lst=bool(), defineTemplate=str(), dt=str(),
                        deselect=str(), d=str(), editor=str(), ed=str(), exists=bool(), ex=bool(), filter=str(),
                        f=str(), findObject=str(), fo=str(), g=bool(), highlightList=bool(), hl=bool(), identify=bool(),
                        id=bool(), keyframeList=bool(), key=bool(), lock=bool(), lck=bool(), modelList=bool(),
                        mdl=bool(), object=str(), obj=str(), parent=str(), p=str(), remove=str(), rm=str(),
                        removeScript=str(), rs=str(), select=str(), s=str(), setList=bool(), sl=bool(), switch=bool(),
                        sw=bool(), useTemplate=str(), ut=str(), worldList=bool(), wl=bool(), *args, **kwargs):
    pass


def selectKey(addTo=bool(), add=bool(), animation=str(), an=str(), attribute=str(), at=str(), clear=bool(), cl=bool(),
              controlPoints=bool(), cp=bool(), float=tuple(), f=tuple(), hierarchy=str(), hi=str(), inTangent=bool(),
              it=bool(), includeUpperBound=bool(), iub=bool(), index=int(), keyframe=bool(), k=bool(),
              outTangent=bool(), ot=bool(), remove=bool(), rm=bool(), replace=bool(), r=bool(), shape=bool(), s=bool(),
              time=tuple(), t=tuple(), toggle=bool(), tgl=bool(), unsnappedKeys=float(), uk=float(), *args, **kwargs):
    pass


def selectKeyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                 image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def selectKeyframeRegionCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                            i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def selectMode(component=bool(), co=bool(), hierarchical=bool(), h=bool(), leaf=bool(), l=bool(), object=bool(),
               o=bool(), preset=bool(), p=bool(), root=bool(), r=bool(), template=bool(), t=bool(), *args, **kwargs):
    pass


def selectPref(affectsActive=bool(), aa=bool(), allowHiliteSelection=bool(), ahs=bool(), autoSelectContainer=bool(),
               asc=bool(), autoSelectOutlinerSetMembers=bool(), asm=bool(), autoUseDepth=bool(), aud=bool(),
               clickBoxSize=int(), cbs=int(), clickDrag=bool(), cld=bool(), containerCentricSelection=bool(),
               ccs=bool(), disableComponentPopups=bool(), dcp=bool(), expandPopupList=bool(), epl=bool(),
               ignoreSelectionPriority=bool(), isp=bool(), manipClickBoxSize=int(), mcb=int(), paintSelect=bool(),
               ps=bool(), paintSelectWithDepth=bool(), psd=bool(), popupMenuSelection=bool(), pms=bool(),
               preSelectBackfacing=bool(), psb=bool(), preSelectClosest=bool(), psc=bool(), preSelectDeadSpace=int(),
               pds=int(), preSelectHilite=bool(), psh=bool(), preSelectHiliteSize=float(), phs=float(),
               preSelectTweakDeadSpace=int(), pdt=int(), selectTypeChangeAffectsActive=bool(), stc=bool(),
               selectionChildHighlightMode=int(), sch=int(), singleBoxSelection=bool(), sbs=bool(),
               straightLineDistance=bool(), sld=bool(), trackSelectionOrder=bool(), tso=bool(), useDepth=bool(),
               ud=bool(), xformNoSelect=bool(), xns=bool(), *args, **kwargs):
    pass


def selectPriority(allComponents=int(), alc=int(), allObjects=int(), alo=int(), animBreakdown=int(), abd=int(),
                   animCurve=int(), ac=int(), animInTangent=int(), ait=int(), animKeyframe=int(), ak=int(),
                   animOutTangent=int(), aot=int(), byName=list, bn=list, camera=int(), ca=int(), cluster=int(),
                   cl=int(), collisionModel=int(), clm=int(), controlVertex=int(), cv=int(), curve=int(), c=int(),
                   curveKnot=int(), ck=int(), curveOnSurface=int(), cos=int(), curveParameterPoint=int(), cpp=int(),
                   dimension=int(), dim=int(), dynamicConstraint=int(), dc=int(), edge=int(), eg=int(), editPoint=int(),
                   ep=int(), emitter=int(), em=int(), facet=int(), fc=int(), field=int(), fi=int(), fluid=int(),
                   fl=int(), follicle=int(), fo=int(), hairSystem=int(), hs=int(), handle=int(), ha=int(), hull=int(),
                   hl=int(), ikEndEffector=int(), iee=int(), ikHandle=int(), ikh=int(), imagePlane=int(), ip=int(),
                   implicitGeometry=int(), ig=int(), isoparm=int(), iso=int(), joint=int(), j=int(), jointPivot=int(),
                   jp=int(), lattice=int(), la=int(), latticePoint=int(), lp=int(), light=int(), lt=int(),
                   localRotationAxis=int(), ra=int(), locator=int(), lc=int(), locatorUV=int(), luv=int(),
                   locatorXYZ=int(), xyz=int(), meshUVShell=int(), msh=int(), motionTrailPoint=int(), mtp=int(),
                   motionTrailTangent=int(), mtt=int(), nCloth=int(), ncl=int(), nParticle=int(), npr=int(),
                   nParticleShape=int(), nps=int(), nRigid=int(), nr=int(), nonlinear=int(), nl=int(), nurbsCurve=int(),
                   nc=int(), nurbsSurface=int(), ns=int(), orientationLocator=int(), ol=int(), particle=int(), pr=int(),
                   particleShape=int(), ps=int(), plane=int(), pl=int(), polymesh=int(), p=int(), polymeshEdge=int(),
                   pe=int(), polymeshFace=int(), pf=int(), polymeshFreeEdge=int(), pfe=int(), polymeshUV=int(),
                   puv=int(), polymeshVertex=int(), pv=int(), polymeshVtxFace=int(), pvf=int(), queryByName=str(),
                   qbn=str(), rigidBody=int(), rb=int(), rigidConstraint=int(), rc=int(), rotatePivot=int(), rp=int(),
                   scalePivot=int(), sp=int(), sculpt=int(), sc=int(), selectHandle=int(), sh=int(), spring=int(),
                   spr=int(), springComponent=int(), spc=int(), stroke=int(), str=int(), subdiv=int(), sd=int(),
                   subdivMeshEdge=int(), sme=int(), subdivMeshFace=int(), smf=int(), subdivMeshPoint=int(), smp=int(),
                   subdivMeshUV=int(), smu=int(), surfaceEdge=int(), se=int(), surfaceFace=int(), sf=int(),
                   surfaceKnot=int(), sk=int(), surfaceParameterPoint=int(), spp=int(), surfaceRange=int(), sr=int(),
                   texture=int(), tx=int(), vertex=int(), v=int(), *args, **kwargs):
    pass


def selectType(allComponents=bool(), alc=bool(), allObjects=bool(), alo=bool(), animBreakdown=bool(), abd=bool(),
               animCurve=bool(), ac=bool(), animInTangent=bool(), ait=bool(), animKeyframe=bool(), ak=bool(),
               animOutTangent=bool(), aot=bool(), byName=list, bn=list, camera=bool(), ca=bool(), cluster=bool(),
               cl=bool(), collisionModel=bool(), clm=bool(), controlVertex=bool(), cv=bool(), curve=bool(), c=bool(),
               curveKnot=bool(), ck=bool(), curveOnSurface=bool(), cos=bool(), curveParameterPoint=bool(), cpp=bool(),
               dimension=bool(), dim=bool(), dynamicConstraint=bool(), dc=bool(), edge=bool(), eg=bool(),
               editPoint=bool(), ep=bool(), emitter=bool(), em=bool(), facet=bool(), fc=bool(), field=bool(), fi=bool(),
               fluid=bool(), fl=bool(), follicle=bool(), fo=bool(), hairSystem=bool(), hs=bool(), handle=bool(),
               ha=bool(), hull=bool(), hl=bool(), ikEndEffector=bool(), iee=bool(), ikHandle=bool(), ikh=bool(),
               imagePlane=bool(), ip=bool(), implicitGeometry=bool(), ig=bool(), isoparm=bool(), iso=bool(),
               joint=bool(), j=bool(), jointPivot=bool(), jp=bool(), lattice=bool(), la=bool(), latticePoint=bool(),
               lp=bool(), light=bool(), lt=bool(), localRotationAxis=bool(), ra=bool(), locator=bool(), lc=bool(),
               locatorUV=bool(), luv=bool(), locatorXYZ=bool(), xyz=bool(), meshUVShell=bool(), msh=bool(),
               motionTrailPoint=bool(), mtp=bool(), motionTrailTangent=bool(), mtt=bool(), nCloth=bool(), ncl=bool(),
               nParticle=bool(), npr=bool(), nParticleShape=bool(), nps=bool(), nRigid=bool(), nr=bool(),
               nonlinear=bool(), nl=bool(), nurbsCurve=bool(), nc=bool(), nurbsSurface=bool(), ns=bool(),
               objectComponent=bool(), ocm=bool(), orientationLocator=bool(), ol=bool(), particle=bool(), pr=bool(),
               particleShape=bool(), ps=bool(), plane=bool(), pl=bool(), polymesh=bool(), p=bool(), polymeshEdge=bool(),
               pe=bool(), polymeshFace=bool(), pf=bool(), polymeshFreeEdge=bool(), pfe=bool(), polymeshUV=bool(),
               puv=bool(), polymeshVertex=bool(), pv=bool(), polymeshVtxFace=bool(), pvf=bool(), queryByName=str(),
               qbn=str(), rigidBody=bool(), rb=bool(), rigidConstraint=bool(), rc=bool(), rotatePivot=bool(), rp=bool(),
               scalePivot=bool(), sp=bool(), sculpt=bool(), sc=bool(), selectHandle=bool(), sh=bool(), spring=bool(),
               spr=bool(), springComponent=bool(), spc=bool(), stroke=bool(), str=bool(), subdiv=bool(), sd=bool(),
               subdivMeshEdge=bool(), sme=bool(), subdivMeshFace=bool(), smf=bool(), subdivMeshPoint=bool(), smp=bool(),
               subdivMeshUV=bool(), smu=bool(), surfaceEdge=bool(), se=bool(), surfaceFace=bool(), sf=bool(),
               surfaceKnot=bool(), sk=bool(), surfaceParameterPoint=bool(), spp=bool(), surfaceRange=bool(), sr=bool(),
               surfaceUV=bool(), suv=bool(), texture=bool(), tx=bool(), vertex=bool(), v=bool(), *args, **kwargs):
    pass


def selLoadSettings(activeProxy=str(), ap=str(), deferReference=bool(), dr=bool(), fileName=str(), fn=str(),
                    numSettings=int(), ns=int(), proxyManager=str(), pm=str(), proxySetFiles=str(), psf=str(),
                    proxySetTags=str(), pst=str(), proxyTag=str(), pt=str(), referenceNode=str(), rfn=str(),
                    shortName=bool(), shn=bool(), unresolvedName=bool(), un=bool(), *args, **kwargs):
    pass


def separator(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(), docTag=str(),
              dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
              enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
              fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, horizontal=bool(),
              hr=bool(), isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
              numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
              preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(), style=str(), st=str(),
              useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
              width=int(), w=int(), *args, **kwargs):
    pass


def sequenceManager(addSequencerAudio=str(), asa=str(), attachSequencerAudio=str(), ata=str(), currentShot=str(),
                    cs=str(), currentTime=float(), ct=float(), listSequencerAudio=str(), lsa=str(), listShots=bool(),
                    lsh=bool(), modelPanel=str(), mp=str(), node=str(), nd=str(), writableSequencer=str(), ws=str(),
                    *args, **kwargs):
    pass


def setAttr(*args, alteredValue: bool = None, av: bool = None, caching: bool = None, ca: bool = None,
            capacityHint: int = None, ch: int = None, channelBox: bool = None, cb: bool = None, clamp: bool = None,
            c: bool = None, keyable: bool = None, k: bool = None, lock: bool = None, l: bool = None, size: int = None, 
            s: int = None, type=str(), typ=str(), **kwargs):

    if args:
        full_name: str = args[0]
        node_name, attr_name = full_name.split('.')
        new_value = None
        if len(args) == 2:
            new_value = args[1]
        node_mobject = _hierarchy.NodePool.from_name(node_name)
        if not node_mobject:
            raise RuntimeError(f"Node {node_name} not found")
        
        plug = om.MFnDependencyNode(node_mobject).findPlug(attr_name, False)
        if new_value is not None:
            plug.attribute()._value = new_value
            return

        if keyable or k:
            plug.isKeyable = keyable or k
        
        if lock or l:
            plug.isLocked = lock or l

        if channelBox or cb:
            plug.isChannelBox = channelBox or cb


def setAttrMapping(absolute=bool(), a=bool(), attribute=str(), at=str(), axis=str(), ax=str(), clutch=str(), c=str(),
                   device=str(), d=str(), offset=float(), o=float(), relative=bool(), r=bool(), scale=float(),
                   s=float(), selection=bool(), sl=bool(), *args, **kwargs):
    pass


def setDefaultShadingGroup(*args, **kwargs):
    pass


def setDrivenKeyframe(attribute=str(), at=str(), controlPoints=bool(), cp=bool(), count=bool(), cnt=bool(),
                      currentDriver=str(), cd=str(), driven=bool(), dn=bool(), driver=bool(), dr=bool(),
                      driverValue=float(), dv=float(), hierarchy=str(), hi=str(), inTangentType=str(), itt=str(),
                      insert=bool(), i=bool(), insertBlend=bool(), ib=bool(), outTangentType=str(), ott=str(),
                      shape=bool(), s=bool(), value=float(), v=float(), *args, **kwargs):
    pass


def setDynamic(allOnWhenRun=bool(), awr=bool(), disableAllOnWhenRun=bool(), dwr=bool(), setAll=bool(), all=bool(),
               setOff=bool(), off=bool(), setOn=bool(), on=bool(), *args, **kwargs):
    pass


def setEditCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
               image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def setFluidAttr(addValue=bool(), ad=bool(), attribute=str(), at=str(), clear=bool(), cl=bool(), floatRandom=float(),
                 fr=float(), floatValue=float(), fv=float(), lowerFace=bool(), lf=bool(), reset=bool(), re=bool(),
                 vectorRandom=list, vr=list, vectorValue=list, vv=list, xIndex=int(), xi=int(), xvalue=bool(), x=bool(),
                 yIndex=int(), yi=int(), yvalue=bool(), y=bool(), zIndex=int(), zi=int(), zvalue=bool(), z=bool(),
                 *args, **kwargs):
    pass


def setFocus(*args, **kwargs):
    pass


def setInfinity(attribute=str(), at=str(), controlPoints=bool(), cp=bool(), hierarchy=str(), hi=str(),
                postInfinite=str(), poi=str(), preInfinite=str(), pri=str(), shape=bool(), s=bool(), *args, **kwargs):
    pass


def setInputDeviceMapping(absolute=bool(), a=bool(), axis=str(), ax=str(), device=str(), d=str(), offset=float(),
                          o=float(), relative=bool(), r=bool(), scale=float(), s=float(), view=bool(), v=bool(),
                          world=bool(), w=bool(), *args, **kwargs):
    pass


def setKeyCtx(breakdown=bool(), bd=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(),
              image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), preserveTangent=bool(), pt=bool(),
              *args, **kwargs):
    pass


def setKeyframe(adjustTangent=bool(), adt=bool(), animLayer=str(), al=str(), animated=bool(), an=bool(),
                attribute=str(), at=str(), breakdown=bool(), bd=bool(), clip=str(), c=str(), controlPoints=bool(),
                cp=bool(), dirtyDG=bool(), dd=bool(), float=float(), f=float(), hierarchy=str(), hi=str(),
                identity=bool(), id=bool(), inTangentType=str(), itt=str(), insert=bool(), i=bool(), insertBlend=bool(),
                ib=bool(), minimizeRotation=bool(), mr=bool(), noResolve=bool(), nr=bool(), outTangentType=str(),
                ott=str(), preserveCurveShape=bool(), pcs=bool(), respectKeyable=bool(), rk=bool(), shape=bool(),
                s=bool(), time=float(), t=float(), useCurrentLockedWeights=bool(), lw=bool(), value=float(), v=float(),
                *args, **kwargs):
    pass


def setKeyframeBlendshapeTargetWts(*args, **kwargs):
    pass


def setKeyPath(*args, **kwargs):
    pass


def setMenuMode(*args, **kwargs):
    pass


def setNodeTypeFlag(display=bool(), dsp=bool(), threadSafe=bool(), ts=bool(), *args, **kwargs):
    pass


def setParent(defineTemplate=str(), dt=str(), menu=bool(), m=bool(), topLevel=bool(), top=bool(), upLevel=bool(),
              u=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def setParticleAttr(attribute=str(), at=str(), floatValue=float(), fv=float(), object=str(), o=str(),
                    randomFloat=float(), rf=float(), randomVector=list, rv=list, relative=bool(), r=bool(),
                    vectorValue=list, vv=list, *args, **kwargs):
    pass


def setRenderPassType(defaultDataType=bool(), d=bool(), numChannels=int(), n=int(), type=str(), t=str(), *args,
                      **kwargs):
    pass


def sets(addElement=str(), add=str(), afterFilters=bool(), af=bool(), anyMember=str(), am=str(), clear=str(), cl=str(),
         color=int(), co=int(), copy=str(), cp=str(), edges=bool(), eg=bool(), editPoints=bool(), ep=bool(),
         empty=bool(), em=bool(), facets=bool(), fc=bool(), flatten=str(), fl=str(), forceElement=str(), fe=str(),
         include=str(), intersection=str(), int=str(), isIntersecting=str(), ii=str(), isMember=str(), im=str(),
         layer=bool(), l=bool(), name=str(), n=str(), noIntermediate=bool(), ni=bool(), noSurfaceShader=bool(),
         nss=bool(), noWarnings=bool(), nw=bool(), nodesOnly=bool(), no=bool(), remove=str(), rm=str(),
         renderable=bool(), r=bool(), size=bool(), s=bool(), split=str(), sp=str(), subtract=str(), sub=str(),
         text=str(), t=str(), union=str(), un=str(), vertices=bool(), v=bool(), *args, **kwargs):
    pass


def setStartupMessage(*args, **kwargs):
    pass


def setToolTo(*args, **kwargs):
    pass


def setUITemplate(popTemplate=bool(), ppt=bool(), pushTemplate=bool(), pst=bool(), *args, **kwargs):
    pass


def setXformManip(showUnits=bool(), su=bool(), suppress=bool(), s=bool(), useRotatePivot=bool(), urp=bool(),
                  worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def shadingConnection(connectionState=bool(), cs=bool(), *args, **kwargs):
    pass


def shadingGeometryRelCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                          i2=str(), image3=str(), i3=str(), name=str(), n=str(), offCommand=str(), ofc=str(),
                          onCommand=str(), onc=str(), shadingCentric=bool(), s=bool(), *args, **kwargs):
    pass


def shadingLightRelCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                       i2=str(), image3=str(), i3=str(), name=str(), n=str(), offCommand=str(), ofc=str(),
                       onCommand=str(), onc=str(), shadingCentric=bool(), s=bool(), *args, **kwargs):
    pass


def shadingNetworkCompare(byName=bool(), nam=bool(), byValue=bool(), val=bool(), delete=bool(), equivalent=bool(),
                          eq=bool(), network1=bool(), n1=bool(), network2=bool(), n2=bool(), upstreamOnly=bool(),
                          up=bool(), *args, **kwargs):
    pass


def shadingNode(asLight=bool(), al=bool(), asPostProcess=bool(), app=bool(), asRendering=bool(), ar=bool(),
                asShader=bool(), asTexture=bool(), at=bool(), asUtility=bool(), au=bool(), isColorManaged=bool(),
                icm=bool(), name=str(), n=str(), parent=str(), p=str(), shared=bool(), s=bool(), skipSelect=bool(),
                ss=bool(), *args, **kwargs):
    pass


def shapeCompare(*args, **kwargs):
    pass


def shapeEditor(clearSelection=bool(), cs=bool(), control=bool(), ctl=bool(), defineTemplate=str(), dt=str(),
                docTag=str(), dtg=str(), exists=bool(), ex=bool(), filter=str(), f=str(), forceMainConnection=str(),
                fmc=str(), highlightConnection=str(), hlc=str(), lockMainConnection=bool(), lck=bool(),
                lowestSelection=bool(), ls=bool(), mainListConnection=str(), mlc=str(), panel=str(), pnl=str(),
                parent=str(), p=str(), selectionConnection=str(), slc=str(), stateString=bool(), sts=bool(),
                targetControlList=bool(), tcl=bool(), targetList=bool(), tl=bool(), unParent=bool(), up=bool(),
                unlockMainConnection=bool(), ulk=bool(), updateMainConnection=bool(), upd=bool(), useTemplate=str(),
                ut=str(), verticalSliders=bool(), vs=bool(), *args, **kwargs):
    pass


def shapePanel(control=bool(), ctl=bool(), copy=str(), cp=str(), createString=bool(), cs=bool(), defineTemplate=str(),
               dt=str(), docTag=str(), dtg=str(), editString=bool(), es=bool(), exists=bool(), ex=bool(), init=bool(),
               isUnique=bool(), iu=bool(), label=str(), l=str(), menuBarRepeatLast=bool(), mrl=bool(),
               menuBarVisible=bool(), mbv=bool(), needsInit=bool(), ni=bool(), parent=str(), p=str(),
               popupMenuProcedure=str(), pmp=str(), replacePanel=str(), rp=str(), shapeEditor=bool(), se=bool(),
               tearOff=bool(), to=bool(), tearOffCopy=str(), toc=str(), tearOffRestore=bool(), tor=bool(),
               unParent=bool(), up=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def shelfButton(align=str(), al=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list, command=str(),
                c=str(), commandRepeatable=bool(), rpt=bool(), defineTemplate=str(), dt=str(), disabledImage=str(),
                di=str(), docTag=str(), dtg=str(), doubleClickCommand=str(), dcc=str(), dragCallback=str(), dgc=str(),
                dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                enableCommandRepeat=bool(), ecr=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                ex=bool(), flat=bool(), fla=bool(), flexibleWidthType=int(), fwt=int(), flexibleWidthValue=int(),
                fwv=int(), flipX=bool(), fx=bool(), flipY=bool(), fy=bool(), font=str(), fn=str(), fullPathName=bool(),
                fpn=bool(), handleNodeDropCallback=str(), hnd=str(), height=int(), h=int(), highlightColor=list,
                hlc=list, highlightImage=str(), hi=str(), image=str(), i=str(), image1=str(), i1=str(), image2=str(),
                i2=str(), image3=str(), i3=str(), imageOverlayLabel=str(), iol=str(), isObscured=bool(), io=bool(),
                label=str(), l=str(), labelEditingCallback=str(), lec=str(), labelOffset=int(), lo=int(),
                ltVersion=str(), lt=str(), manage=bool(), m=bool(), marginHeight=int(), mh=int(), marginWidth=int(),
                mw=int(), menuItem=list, mi=list, menuItemPython=int(), mip=int(), noBackground=bool(), nbg=bool(),
                noDefaultPopup=bool(), ndp=bool(), numberOfPopupMenus=bool(), npm=bool(), overlayLabelBackColor=list,
                olb=list, overlayLabelColor=list, olc=list, parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                preventOverride=bool(), po=bool(), rotation=float(), rot=float(), scaleIcon=bool(), sic=bool(),
                selectionImage=str(), si=str(), sourceType=str(), stp=str(), statusBarMessage=str(), sbm=str(),
                style=str(), st=str(), useAlpha=bool(), ua=bool(), useTemplate=str(), ut=str(), version=str(),
                ver=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
                *args, **kwargs):
    pass


def shelfLayout(alignment=str(), aln=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                cellHeight=int(), ch=int(), cellWidth=int(), cw=int(), cellWidthHeight=list, cwh=list,
                childArray=bool(), ca=bool(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
                fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                horizontal=bool(), hr=bool(), isObscured=bool(), io=bool(), ltVersion=str(), lt=str(), manage=bool(),
                m=bool(), noBackground=bool(), nbg=bool(), numberOfChildren=bool(), nch=bool(),
                numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                position=list, pos=list, preventOverride=bool(), po=bool(), spacing=int(), spa=int(),
                statusBarMessage=str(), sbm=str(), style=str(), st=str(), useTemplate=str(), ut=str(), version=str(),
                ver=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
                *args, **kwargs):
    pass


def shelfTabLayout(annotation=str(), ann=str(), backgroundColor=list, bgc=list, borderStyle=str(), bs=str(),
                   changeCommand=str(), cc=str(), childArray=bool(), ca=bool(), childResizable=bool(), cr=bool(),
                   closeTab=int(), ct=int(), closeTabCommand=str(), ctc=str(), defineTemplate=str(), dt=str(),
                   docTag=str(), dtg=str(), doubleClickCommand=str(), dcc=str(), dragCallback=str(), dgc=str(),
                   dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                   enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(),
                   height=int(), h=int(), highlightColor=list, hlc=list, horizontalScrollBarThickness=int(), hst=int(),
                   image=str(), i=str(), imageVisible=bool(), iv=bool(), innerMarginHeight=int(), imh=int(),
                   innerMarginWidth=int(), imw=int(), isObscured=bool(), io=bool(), manage=bool(), m=bool(),
                   minChildWidth=int(), mcw=int(), moveTab=list, mt=list, newTabCommand=str(), ntc=str(),
                   noBackground=bool(), nbg=bool(), numberOfChildren=bool(), nch=bool(), numberOfPopupMenus=bool(),
                   npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), postMenuCommand=str(),
                   pmc=str(), preSelectCommand=str(), psc=str(), preventOverride=bool(), po=bool(), scrollable=bool(),
                   scr=bool(), scrollableTabs=bool(), stb=bool(), selectCommand=str(), sc=str(), selectTab=str(),
                   st=str(), selectTabIndex=int(), sti=int(), showNewTab=bool(), snt=bool(), statusBarMessage=str(),
                   sbm=str(), tabIcon=list, ti=list, tabIconIndex=list, tii=list, tabLabel=list, tl=list,
                   tabLabelIndex=list, tli=list, tabPosition=str(), tp=str(), tabTooltip=list, tt=list,
                   tabTooltipIndex=list, tti=list, tabsClosable=bool(), tc=bool(), tabsVisible=bool(), tv=bool(),
                   useTemplate=str(), ut=str(), verticalScrollBarThickness=int(), vst=int(), visible=bool(), vis=bool(),
                   visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def shot(audio=str(), aud=str(), clip=str(), cl=str(), clipDuration=float(), cd=float(), clipOpacity=float(),
         co=float(), clipSyncState=bool(), css=bool(), clipZeroOffset=float(), czo=float(), copy=bool(), c=bool(),
         createCustomAnim=bool(), cca=bool(), currentCamera=str(), cc=str(), customAnim=bool(), ca=bool(),
         deleteCustomAnim=bool(), dca=bool(), determineTrack=bool(), dt=bool(), endTime=float(), et=float(),
         favorite=bool(), fav=bool(), flag1=bool(), f1=bool(), flag10=bool(), f10=bool(), flag11=bool(), f11=bool(),
         flag12=bool(), f12=bool(), flag2=bool(), f2=bool(), flag3=bool(), f3=bool(), flag4=bool(), f4=bool(),
         flag5=bool(), f5=bool(), flag6=bool(), f6=bool(), flag7=bool(), f7=bool(), flag8=bool(), f8=bool(),
         flag9=bool(), f9=bool(), hasCameraSet=bool(), hcs=bool(), hasStereoCamera=bool(), hsc=bool(),
         imagePlaneVisibility=bool(), ipv=bool(), linkAudio=str(), la=str(), lock=bool(), lck=bool(), mute=bool(),
         m=bool(), paste=bool(), p=bool(), pasteInstance=bool(), pi=bool(), postHoldTime=float(), pst=float(),
         preHoldTime=float(), prt=float(), scale=float(), s=float(), selfmute=bool(), sm=bool(),
         sequenceDuration=float(), sqd=float(), sequenceEndTime=float(), set=float(), sequenceStartTime=float(),
         sst=float(), shotName=str(), sn=str(), sourceDuration=float(), sd=float(), startTime=float(), st=float(),
         track=int(), trk=int(), transitionInLength=float(), til=float(), transitionInType=int(), tit=int(),
         transitionOutLength=float(), tol=float(), transitionOutType=int(), tot=int(), unlinkAudio=bool(), ula=bool(),
         *args, **kwargs):
    pass


def shotRipple(deleted=bool(), d=bool(), endDelta=float(), ed=float(), endTime=float(), et=float(), startDelta=float(),
               sd=float(), startTime=float(), st=float(), *args, **kwargs):
    pass


def shotTrack(insertTrack=int(), it=int(), lock=bool(), l=bool(), mute=bool(), m=bool(), numTracks=int(), nt=int(),
              removeEmptyTracks=bool(), ret=bool(), removeTrack=int(), rt=int(), selfmute=bool(), sm=bool(),
              solo=bool(), so=bool(), swapTracks=list, st=list, title=str(), t=str(), track=int(), tr=int(),
              unsolo=bool(), uso=bool(), *args, **kwargs):
    pass


def showHelp(absolute=bool(), a=bool(), docs=bool(), d=bool(), helpTable=bool(), ht=bool(), version=bool(), v=bool(),
             *args, **kwargs):
    pass


def showHidden(above=bool(), a=bool(), allObjects=bool(), all=bool(), below=bool(), b=bool(), lastHidden=bool(),
               lh=bool(), *args, **kwargs):
    pass


def showManipCtx(currentNodeName=bool(), cnn=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
                 i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), incSnap=list, incSnapRelative=list, isr=list,
                 incSnapUI=bool(), isu=bool(), incSnapValue=list, isv=list, lockSelection=bool(), ls=bool(), name=str(),
                 n=str(), toggleIncSnap=bool(), tis=bool(), toolFinish=str(), tf=str(), toolStart=str(), ts=str(),
                 *args, **kwargs):
    pass


def showMetadata(auto=bool(), a=bool(), dataType=str(), dt=str(), interpolation=bool(), i=bool(), isActivated=bool(),
                 ia=bool(), listAllStreams=bool(), las=bool(), listMembers=bool(), lm=bool(), listValidMethods=bool(),
                 lvm=bool(), listVisibleStreams=bool(), lvs=bool(), member=str(), mb=str(), method=str(), m=str(),
                 off=bool(), range=list, r=list, rayScale=float(), rs=float(), stream=str(), s=str(), *args, **kwargs):
    pass


def showSelectionInTitle(*args, **kwargs):
    pass


def showShadingGroupAttrEditor(*args, **kwargs):
    pass


def showWindow(*args, **kwargs):
    pass


def simplify(animation=str(), an=str(), attribute=str(), at=str(), controlPoints=bool(), cp=bool(), float=tuple(),
             f=tuple(), floatTolerance=float(), ft=float(), hierarchy=str(), hi=str(), includeUpperBound=bool(),
             iub=bool(), index=int(), shape=bool(), s=bool(), time=tuple(), t=tuple(), timeTolerance=float(),
             tt=float(), valueTolerance=float(), vt=float(), *args, **kwargs):
    pass


def singleProfileBirailSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(),
                               nodeState=int(), nds=int(), object=bool(), o=bool(), polygon=int(), po=int(),
                               tangentContinuityProfile1=bool(), tp1=bool(), transformMode=int(), tm=int(), *args,
                               **kwargs):
    pass


def skeletonEmbed(mergedMesh=bool(), mm=bool(), segmentationMethod=int(), sm=int(), segmentationResolution=int(),
                  sr=int(), *args, **kwargs):
    pass


def skinBindCtx(about=str(), a=str(), axis=str(), ax=str(), colorRamp=str(), cr=str(), currentInfluence=str(), ci=str(),
                displayInactiveMode=int(), di=int(), displayNormalized=bool(), dn=bool(), exists=bool(), ex=bool(),
                falloffCurve=str(), fc=str(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                image3=str(), i3=str(), name=str(), n=str(), symmetry=bool(), s=bool(), tolerance=float(), t=float(),
                *args, **kwargs):
    pass


def skinCluster(addInfluence=str(), ai=str(), addToSelection=bool(), ats=bool(), after=bool(), af=bool(),
                afterReference=bool(), ar=bool(), baseShape=str(), bsh=str(), before=bool(), bf=bool(),
                bindMethod=int(), bm=int(), deformerTools=bool(), dt=bool(), dropoffRate=float(), dr=float(),
                exclusive=str(), ex=str(), forceNormalizeWeights=bool(), fnw=bool(), frontOfChain=bool(), foc=bool(),
                geometry=str(), g=str(), geometryIndices=bool(), gi=bool(), heatmapFalloff=float(), hmf=float(),
                ignoreBindPose=bool(), ibp=bool(), ignoreHierarchy=bool(), ih=bool(), ignoreSelected=bool(),
                includeHiddenSelections=bool(), ihs=bool(), influence=str(), inf=str(), lockWeights=bool(), lw=bool(),
                maximumInfluences=int(), mi=int(), moveJointsMode=bool(), mjm=bool(), name=str(), n=str(),
                normalizeWeights=int(), nw=int(), nurbsSamples=int(), ns=int(), obeyMaxInfluences=bool(), omi=bool(),
                parallel=bool(), par=bool(), polySmoothness=float(), ps=float(), prune=bool(), pr=bool(),
                recacheBindMatrices=bool(), rbm=bool(), remove=bool(), rm=bool(), removeFromSelection=bool(),
                rfs=bool(), removeInfluence=str(), ri=str(), removeUnusedInfluence=bool(), rui=bool(),
                selectInfluenceVerts=str(), siv=str(), skinMethod=int(), sm=int(), smoothWeights=float(), sw=float(),
                smoothWeightsMaxIterations=int(), swi=int(), split=bool(), sp=bool(), toSelectedBones=bool(),
                tsb=bool(), toSkeletonAndTransforms=bool(), tst=bool(), unbind=bool(), ub=bool(),
                unbindKeepHistory=bool(), ubk=bool(), useComponentTags=bool(), uct=bool(), useGeometry=bool(),
                ug=bool(), volumeBind=float(), vb=float(), volumeType=int(), vt=int(), weight=float(), wt=float(),
                weightDistribution=int(), wd=int(), weightedInfluence=bool(), wi=bool(), *args, **kwargs):
    pass


def skinPercent(ignoreBelow=float(), ib=float(), normalize=bool(), nrm=bool(), pruneWeights=float(), prw=float(),
                relative=bool(), r=bool(), resetToDefault=bool(), rtd=bool(), transform=str(), t=str(),
                transformMoveWeights=str(), tmw=str(), transformValue=list, tv=list, value=bool(), v=bool(),
                zeroRemainingInfluences=bool(), zri=bool(), *args, **kwargs):
    pass


def smoothCurve(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(), nodeState=int(),
                nds=int(), object=bool(), o=bool(), replaceOriginal=bool(), rpo=bool(), smoothness=float(), s=float(),
                *args, **kwargs):
    pass


def smoothTangentSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), direction=int(), d=int(),
                         name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), parameter=float(),
                         p=float(), replaceOriginal=bool(), rpo=bool(), smoothness=int(), s=int(), *args, **kwargs):
    pass


def snapKey(animation=str(), an=str(), attribute=str(), at=str(), controlPoints=bool(), cp=bool(), float=tuple(),
            f=tuple(), hierarchy=str(), hi=str(), includeUpperBound=bool(), iub=bool(), index=int(),
            mergeDuplicate=bool(), md=bool(), shape=bool(), s=bool(), time=tuple(), t=tuple(), timeMultiple=float(),
            tm=float(), valueMultiple=float(), vm=float(), *args, **kwargs):
    pass


def snapMode(curve=bool(), c=bool(), distanceIncrement=float(), dsi=float(), edgeMagnet=int(), em=int(),
             edgeMagnetTolerance=float(), emt=float(), grid=bool(), gr=bool(), liveFaceCenter=bool(), lfc=bool(),
             livePoint=bool(), lp=bool(), meshCenter=bool(), mc=bool(), pixelCenter=bool(), pc=bool(), pixelSnap=bool(),
             ps=bool(), point=bool(), p=bool(), tolerance=int(), t=int(), useTolerance=bool(), ut=bool(),
             uvTolerance=int(), uvt=int(), viewPlane=bool(), vp=bool(), *args, **kwargs):
    pass


def snapshot(constructionHistory=bool(), ch=bool(), endTime=float(), et=float(), increment=float(), i=float(),
             motionTrail=bool(), mt=bool(), name=str(), n=str(), startTime=float(), st=float(), update=str(), u=str(),
             *args, **kwargs):
    pass


def snapshotBeadCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
                    image3=str(), i3=str(), inTangent=bool(), i=bool(), name=str(), n=str(), outTangent=bool(),
                    o=bool(), *args, **kwargs):
    pass


def snapshotModifyKeyCtx(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                         i2=str(), image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def snapTogetherCtx(clearSelection=bool(), cs=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
                    i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(),
                    setOrientation=bool(), so=bool(), snapPolygonFace=bool(), spf=bool(), *args, **kwargs):
    pass


def soft(convert=bool(), c=bool(), duplicate=bool(), d=bool(), duplicateHistory=bool(), dh=bool(), goal=float(),
         g=float(), hideOriginal=bool(), h=bool(), name=str(), n=str(), *args, **kwargs):
    pass


def softMod(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(), bindState=bool(),
            bs=bool(), curveInterpolation=int(), ci=int(), curvePoint=float(), cp=float(), curveValue=float(),
            cv=float(), deformerTools=bool(), dt=bool(), envelope=float(), en=float(), exclusive=str(), ex=str(),
            falloffAroundSelection=bool(), fas=bool(), falloffBasedOnX=bool(), fbx=bool(), falloffBasedOnY=bool(),
            fby=bool(), falloffBasedOnZ=bool(), fbz=bool(), falloffCenter=list, fc=list, falloffMasking=bool(),
            fm=bool(), falloffMode=int(), fom=int(), falloffRadius=float(), fr=float(), frontOfChain=bool(), foc=bool(),
            geometry=str(), g=str(), geometryIndices=bool(), gi=bool(), ignoreSelected=bool(),
            includeHiddenSelections=bool(), ihs=bool(), name=str(), n=str(), parallel=bool(), par=bool(), prune=bool(),
            pr=bool(), relative=bool(), rel=bool(), remove=bool(), rm=bool(), resetGeometry=bool(), rg=bool(),
            split=bool(), sp=bool(), useComponentTags=bool(), uct=bool(), weightedNode=list, wn=list, *args, **kwargs):
    pass


def softModCtx(dragSlider=str(), ds=str(), exists=bool(), ex=bool(), falseColor=bool(), fc=bool(), image1=str(),
               i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), reset=bool(), rst=bool(), *args, **kwargs):
    pass


def softSelect(compressUndo=int(), cu=int(), enableFalseColor=int(), efc=int(), softSelectColorCurve=str(), scc=str(),
               softSelectCurve=str(), ssc=str(), softSelectDistance=float(), ssd=float(), softSelectEnabled=int(),
               sse=int(), softSelectFalloff=int(), ssf=int(), softSelectReset=bool(), ssr=bool(),
               softSelectUVDistance=float(), sud=float(), *args, **kwargs):
    pass


def soloMaterial(attr=str(), a=str(), last=bool(), l=bool(), node=str(), n=str(), unsolo=bool(), us=bool(), *args,
                 **kwargs):
    pass


def sortCaseInsensitive(*args, **kwargs):
    pass


def sound(endTime=float(), et=float(), file=str(), f=str(), length=bool(), l=bool(), mute=bool(), m=bool(), name=str(),
          n=str(), offset=float(), o=float(), sourceEnd=float(), se=float(), sourceStart=float(), ss=float(), *args,
          **kwargs):
    pass


def soundControl(annotation=str(), ann=str(), backgroundColor=list, bgc=list, beginScrub=bool(), bs=bool(),
                 defineTemplate=str(), dt=str(), displaySound=bool(), ds=bool(), docTag=str(), dtg=str(),
                 dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                 enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), endScrub=bool(),
                 es=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                 highlightColor=list, hlc=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(), maxTime=float(),
                 max=float(), minTime=float(), min=float(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(),
                 npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), pressCommand=str(), pc=str(),
                 preventOverride=bool(), po=bool(), releaseCommand=str(), rc=str(), repeatChunkSize=float(),
                 rcs=float(), repeatOnHold=bool(), roh=bool(), resample=bool(), r=bool(), sound=str(), s=str(),
                 statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                 visibleChangeCommand=str(), vcc=str(), waveform=str(), wf=str(), width=int(), w=int(), *args,
                 **kwargs):
    pass


def soundPopup(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(),
               docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
               en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
               ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
               isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
               numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
               preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
               visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
               **kwargs):
    pass


def spaceLocator(absolute=bool(), a=bool(), name=str(), n=str(), position=list, p=list, relative=bool(), r=bool(),
                 *args, **kwargs):
    pass


def sphere(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), degree=int(), d=int(),
           endSweep=float(), esw=float(), heightRatio=float(), hr=float(), name=str(), n=str(), nodeState=int(),
           nds=int(), object=bool(), o=bool(), pivot=list, p=list, polygon=int(), po=int(), radius=float(), r=float(),
           sections=int(), s=int(), spans=int(), nsp=int(), startSweep=float(), ssw=float(), tolerance=float(),
           tol=float(), useTolerance=bool(), ut=bool(), *args, **kwargs):
    pass


def spotLight(barnDoors=bool(), bd=bool(), bottomBarnDoorAngle=float(), bbd=float(), coneAngle=float(), ca=float(),
              decayRate=int(), d=int(), discRadius=float(), drs=float(), dropOff=float(), do=float(), exclusive=bool(),
              exc=bool(), intensity=float(), i=float(), leftBarnDoorAngle=float(), lbd=float(), name=str(), n=str(),
              penumbra=float(), p=float(), position=list, pos=list, rgb=list, rightBarnDoorAngle=float(), rbd=float(),
              rotation=list, rot=list, shadowColor=list, sc=list, shadowDither=float(), sd=float(), shadowSamples=int(),
              sh=int(), softShadow=bool(), ss=bool(), topBarnDoorAngle=float(), tbd=float(), useRayTraceShadows=bool(),
              rs=bool(), *args, **kwargs):
    pass


def spotLightPreviewPort(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(),
                         docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
                         enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
                         ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                         highlightColor=list, hlc=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(),
                         noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                         popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), spotLight=str(),
                         sl=str(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(),
                         vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), widthHeight=list,
                         wh=list, *args, **kwargs):
    pass


def spreadSheetEditor(allAttr=bool(), aa=bool(), attrRegExp=str(), are=str(), control=bool(), ctl=bool(),
                      defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), execute=str(), exe=str(), exists=bool(),
                      ex=bool(), filter=str(), f=str(), fixedAttrList=list, fal=list, forceMainConnection=str(),
                      fmc=str(), highlightConnection=str(), hlc=str(), keyableOnly=bool(), ko=bool(),
                      lockMainConnection=bool(), lck=bool(), longNames=bool(), ln=bool(), mainListConnection=str(),
                      mlc=str(), niceNames=bool(), nn=bool(), panel=str(), pnl=str(), parent=str(), p=str(),
                      precision=int(), pre=int(), selectedAttr=bool(), sla=bool(), selectionConnection=str(), slc=str(),
                      showShapes=bool(), ss=bool(), stateString=bool(), sts=bool(), unParent=bool(), up=bool(),
                      unlockMainConnection=bool(), ulk=bool(), updateMainConnection=bool(), upd=bool(),
                      useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def spring(addSprings=bool(), add=bool(), allPoints=bool(), all=bool(), count=bool(), ct=bool(), damping=float(),
           d=float(), dampingPS=float(), dPS=float(), endForceWeight=float(), efw=float(), exclusive=bool(), exc=bool(),
           length=float(), l=float(), maxDistance=float(), mxd=float(), minDistance=float(), mnd=float(), minMax=bool(),
           mm=bool(), name=str(), n=str(), noDuplicate=bool(), nd=bool(), restLength=float(), rl=float(),
           restLengthPS=float(), rPS=float(), startForceWeight=float(), sfw=float(), stiffness=float(), s=float(),
           stiffnessPS=float(), sPS=float(), useDampingPS=bool(), udp=bool(), useRestLengthPS=bool(), urp=bool(),
           useStiffnessPS=bool(), usp=bool(), walkLength=int(), wl=int(), wireframe=bool(), wf=bool(), *args, **kwargs):
    pass


def squareSurface(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), continuityType1=int(), ct1=int(),
                  continuityType2=int(), ct2=int(), continuityType3=int(), ct3=int(), continuityType4=int(), ct4=int(),
                  curveFitCheckpoints=int(), cfc=int(), endPointTolerance=float(), ept=float(), name=str(), n=str(),
                  nodeState=int(), nds=int(), object=bool(), o=bool(), polygon=int(), po=int(), rebuildCurve1=bool(),
                  rc1=bool(), rebuildCurve2=bool(), rc2=bool(), rebuildCurve3=bool(), rc3=bool(), rebuildCurve4=bool(),
                  rc4=bool(), *args, **kwargs):
    pass


def srtContext(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(),
               image3=str(), i3=str(), name=str(), n=str(), *args, **kwargs):
    pass


def stereoCameraView(activeComponentsXray=bool(), acx=bool(), activeCustomEnvironment=str(), ace=str(),
                     activeCustomGeometry=str(), acg=str(), activeCustomLighSet=str(), acl=str(),
                     activeCustomOverrideGeometry=str(), aog=str(), activeCustomRenderer=str(), acr=str(),
                     activeOnly=bool(), ao=bool(), activeShadingGraph=str(), asg=str(), activeSupported=bool(),
                     ams=bool(), activeView=bool(), av=bool(), addObjects=str(), aob=str(), addSelected=bool(),
                     allObjects=bool(), alo=bool(), backfaceCulling=bool(), bfc=bool(), bufferMode=str(), bm=str(),
                     bumpResolution=list, brz=list, camera=str(), cam=str(), cameraName=str(), cn=str(),
                     cameraSet=str(), cst=str(), cameraSetup=bool(), cs=bool(), cameras=bool(), ca=bool(),
                     capture=str(), cpt=str(), captureSequenceNumber=int(), csn=int(), centerCamera=str(), ccm=str(),
                     colorMap=bool(), cm=bool(), colorResolution=list, crz=list, control=bool(), ctl=bool(),
                     controlVertices=bool(), cv=bool(), cullingOverride=str(), cov=str(), default=bool(), d=bool(),
                     defineTemplate=str(), dt=str(), deformers=bool(), df=bool(), dimensions=bool(), dim=bool(),
                     displayAppearance=str(), da=str(), displayLights=str(), dl=str(), displayMode=str(), dm=str(),
                     displayTextures=bool(), dtx=bool(), docTag=str(), dtg=str(), dynamicConstraints=bool(), dc=bool(),
                     dynamics=bool(), dy=bool(), editorChanged=str(), ec=str(), exists=bool(), ex=bool(), filter=str(),
                     f=str(), filteredObjectList=bool(), fol=bool(), fluids=bool(), fl=bool(), fogColor=list, fcl=list,
                     fogDensity=float(), fdn=float(), fogEnd=float(), fen=float(), fogMode=str(), fmd=str(),
                     fogSource=str(), fsc=str(), fogStart=float(), fst=float(), fogging=bool(), fg=bool(),
                     follicles=bool(), fo=bool(), forceMainConnection=str(), fmc=str(), grid=bool(), gr=bool(),
                     hairSystems=bool(), hs=bool(), handles=bool(), ha=bool(), headsUpDisplay=bool(), hud=bool(),
                     height=bool(), h=bool(), highlightConnection=str(), hlc=str(), hulls=bool(), hu=bool(),
                     ignorePanZoom=bool(), ipz=bool(), ikHandles=bool(), ikh=bool(), imagePlane=bool(), imp=bool(),
                     interactive=bool(), i=bool(), interactiveBackFaceCull=bool(), ibc=bool(),
                     interactiveDisableShadows=bool(), dis=bool(), isFiltered=bool(), jointXray=bool(), jx=bool(),
                     joints=bool(), j=bool(), leftCamera=str(), lcm=str(), lights=bool(), lt=bool(), lineWidth=float(),
                     lw=float(), locators=bool(), lc=bool(), lockMainConnection=bool(), lck=bool(),
                     lowQualityLighting=bool(), lql=bool(), mainListConnection=str(), mlc=str(), manipulators=bool(),
                     m=bool(), maxConstantTransparency=float(), mct=float(), maximumNumHardwareLights=bool(),
                     mhl=bool(), modelPanel=str(), mp=str(), motionTrails=bool(), mt=bool(), nCloths=bool(), ncl=bool(),
                     nParticles=bool(), npa=bool(), nRigids=bool(), nr=bool(), noUndo=bool(), nud=bool(),
                     nurbsCurves=bool(), nc=bool(), nurbsSurfaces=bool(), ns=bool(), objectFilter=str(), obf=str(),
                     objectFilterList=str(), ofl=str(), objectFilterListUI=str(), ofu=str(),
                     objectFilterShowInHUD=bool(), ofs=bool(), objectFilterUI=str(), obu=str(), occlusionCulling=bool(),
                     ocl=bool(), panel=str(), pnl=str(), parent=str(), p=str(), pivots=bool(), pv=bool(), planes=bool(),
                     pl=bool(), pluginObjects=list, po=list, pluginShapes=bool(), ps=bool(), polymeshes=bool(),
                     pm=bool(), queryPluginObjects=str(), qpo=str(), removeSelected=bool(), rs=bool(),
                     rendererDeviceName=bool(), rdn=bool(), rendererList=bool(), rls=bool(), rendererListUI=bool(),
                     rlu=bool(), rendererName=str(), rnm=str(), rendererOverrideList=bool(), rol=bool(),
                     rendererOverrideListUI=bool(), rou=bool(), rendererOverrideName=str(), rom=str(),
                     resetCustomCamera=bool(), rcc=bool(), rigRoot=str(), rr=str(), rightCamera=str(), rcm=str(),
                     sceneRenderFilter=str(), srf=str(), selectionConnection=str(), slc=str(),
                     selectionHiliteDisplay=bool(), sel=bool(), setSelected=bool(), ss=bool(), shadingModel=int(),
                     sml=int(), shadows=bool(), sdw=bool(), smallObjectCulling=bool(), soc=bool(),
                     smallObjectThreshold=float(), sot=float(), smoothWireframe=bool(), swf=bool(),
                     sortTransparent=bool(), st=bool(), stateString=bool(), sts=bool(), stereoDrawMode=bool(),
                     sdm=bool(), strokes=bool(), str=bool(), subdivSurfaces=bool(), sds=bool(), swapEyes=bool(),
                     se=bool(), textureAnisotropic=bool(), ta=bool(), textureCompression=bool(), tcp=bool(),
                     textureDisplay=str(), td=str(), textureEnvironmentMap=bool(), tem=bool(), textureHilight=bool(),
                     th=bool(), textureMaxSize=int(), tms=int(), textureMemoryUsed=bool(), tmu=bool(),
                     textureSampling=int(), ts=int(), textures=bool(), tx=bool(), transpInShadows=bool(), tis=bool(),
                     transparencyAlgorithm=str(), tal=str(), twoSidedLighting=bool(), tsl=bool(), unParent=bool(),
                     up=bool(), unlockMainConnection=bool(), ulk=bool(), updateColorMode=bool(), ucm=bool(),
                     updateMainConnection=bool(), upd=bool(), useBaseRenderer=bool(), ubr=bool(), useColorIndex=bool(),
                     uci=bool(), useCustomBackground=bool(), ucb=bool(), useDefaultMaterial=bool(), udm=bool(),
                     useInteractiveMode=bool(), ui=bool(), useRGBImagePlane=bool(), ip=bool(),
                     useReducedRenderer=bool(), urr=bool(), useTemplate=str(), ut=str(), userNode=str(), un=str(),
                     viewColor=list, vc=list, viewObjects=bool(), vo=bool(), viewSelected=bool(), vs=bool(),
                     viewType=bool(), vt=bool(), width=bool(), w=bool(), wireframeBackingStore=bool(), wbs=bool(),
                     wireframeOnShaded=bool(), wos=bool(), xray=bool(), xr=bool(), *args, **kwargs):
    pass


def stereoRigManager(addRig=list, add=list, cameraSetFunc=list, csf=list, creationProcedure=list, cp=list,
                     defaultRig=str(), dr=str(), delete=str(), d=str(), language=list, l=list, listRigs=bool(),
                     lr=bool(), rigDefinition=str(), rd=str(), *args, **kwargs):
    pass


def stitchSurface(bias=float(), b=float(), caching=bool(), cch=bool(), cascade=bool(), c=bool(),
                  constructionHistory=bool(), ch=bool(), cvIthIndex=int(), ci=int(), cvJthIndex=int(), cj=int(),
                  fixBoundary=bool(), fb=bool(), keepG0Continuity=bool(), kg0=bool(), keepG1Continuity=bool(),
                  kg1=bool(), name=str(), n=str(), nodeState=int(), nds=int(), numberOfSamples=int(), ns=int(),
                  object=bool(), o=bool(), parameterU=float(), u=float(), parameterV=float(), v=float(),
                  positionalContinuity=bool(), pc=bool(), replaceOriginal=bool(), rpo=bool(), stepCount=int(), sc=int(),
                  tangentialContinuity=bool(), tc=bool(), togglePointNormals=bool(), tpn=bool(),
                  togglePointPosition=bool(), tpp=bool(), toggleTolerance=bool(), tt=bool(), tolerance=float(),
                  tol=float(), weight0=float(), wt0=float(), weight1=float(), wt1=float(), *args, **kwargs):
    pass


def stitchSurfacePoints(bias=float(), b=float(), caching=bool(), cch=bool(), cascade=bool(), c=bool(),
                        constructionHistory=bool(), ch=bool(), cvIthIndex=int(), ci=int(), cvJthIndex=int(), cj=int(),
                        equalWeight=bool(), ewt=bool(), fixBoundary=bool(), fb=bool(), keepG0Continuity=bool(),
                        kg0=bool(), keepG1Continuity=bool(), kg1=bool(), name=str(), n=str(), nodeState=int(),
                        nds=int(), object=bool(), o=bool(), parameterU=float(), u=float(), parameterV=float(),
                        v=float(), positionalContinuity=bool(), pc=bool(), replaceOriginal=bool(), rpo=bool(),
                        stepCount=int(), sc=int(), tangentialContinuity=bool(), tc=bool(), togglePointNormals=bool(),
                        tpn=bool(), togglePointPosition=bool(), tpp=bool(), toggleTolerance=bool(), tt=bool(),
                        tolerance=float(), tol=float(), *args, **kwargs):
    pass


def stringArrayIntersector(allowDuplicates=bool(), ad=bool(), defineTemplate=str(), dt=str(), exists=bool(), ex=bool(),
                           intersect=list, i=list, reset=bool(), r=bool(), useTemplate=str(), ut=str(), *args,
                           **kwargs):
    pass


def stroke(name=str(), n=str(), pressure=bool(), pr=bool(), seed=int(), s=int(), *args, **kwargs):
    pass


def subdAutoProjection(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), layout=int(), l=int(),
                       layoutMethod=int(), lm=int(), name=str(), n=str(), nodeState=int(), nds=int(), optimize=int(),
                       o=int(), percentageSpace=float(), ps=float(), planes=int(), p=int(), scale=int(), sc=int(),
                       skipIntersect=bool(), si=bool(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def subdCleanTopology(*args, **kwargs):
    pass


def subdCollapse(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), level=int(), l=int(), name=str(),
                 n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), *args, **kwargs):
    pass


def subdDuplicateAndConnect(*args, **kwargs):
    pass


def subdEditUV(angle=float(), a=float(), pivotU=float(), pu=float(), pivotV=float(), pv=float(), relative=bool(),
               r=bool(), rotateRatio=float(), rr=float(), rotation=bool(), rot=bool(), scale=bool(), s=bool(),
               scaleU=float(), su=float(), scaleV=float(), sv=float(), uValue=float(), u=float(), uvSetName=str(),
               uvs=str(), vValue=float(), v=float(), *args, **kwargs):
    pass


def subdiv(currentLevel=bool(), cl=bool(), currentSubdLevel=bool(), csl=bool(), deepestLevel=int(), dl=int(),
           displayLoad=bool(), dsl=bool(), edgeStats=bool(), est=bool(), faceStats=bool(), fst=bool(),
           maxPossibleLevel=int(), mpl=int(), proxyMode=int(), pm=int(), smallOffsets=bool(), so=bool(), *args,
           **kwargs):
    pass


def subdivCrease(sharpness=bool(), sh=bool(), *args, **kwargs):
    pass


def subdivDisplaySmoothness(all=bool(), smoothness=int(), s=int(), *args, **kwargs):
    pass


def subdLayoutUV(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), flipReversed=bool(), fr=bool(),
                 layout=int(), l=int(), layoutMethod=int(), lm=int(), name=str(), n=str(), nodeState=int(), nds=int(),
                 percentageSpace=float(), ps=float(), rotateForBestFit=int(), rbf=int(), scale=int(), sc=int(),
                 separate=int(), se=int(), worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def subdListComponentConversion(border=bool(), bo=bool(), fromEdge=bool(), fe=bool(), fromFace=bool(), ff=bool(),
                                fromUV=bool(), fuv=bool(), fromVertex=bool(), fv=bool(), internal=bool(), toEdge=bool(),
                                te=bool(), toFace=bool(), tf=bool(), toUV=bool(), tuv=bool(), toVertex=bool(),
                                tv=bool(), uvShell=bool(), uvs=bool(), uvShellBorder=bool(), uvb=bool(), *args,
                                **kwargs):
    pass


def subdMapCut(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(), nodeState=int(),
               nds=int(), *args, **kwargs):
    pass


def subdMapSewMove(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), limitPieceSize=bool(), lps=bool(),
                   name=str(), n=str(), nodeState=int(), nds=int(), numberFaces=int(), nf=int(), worldSpace=bool(),
                   ws=bool(), *args, **kwargs):
    pass


def subdMatchTopology(frontOfChain=bool(), foc=bool(), *args, **kwargs):
    pass


def subdMirror(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), name=str(), n=str(), nodeState=int(),
               nds=int(), object=bool(), o=bool(), xMirror=bool(), xm=bool(), yMirror=bool(), ym=bool(), zMirror=bool(),
               zm=bool(), *args, **kwargs):
    pass


def subdPlanarProjection(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), createNewMap=bool(),
                         cm=bool(), imageCenter=list, ic2=list, imageCenterX=float(), icx=float(), imageCenterY=float(),
                         icy=float(), imageScale=list, is2=list, imageScaleU=float(), isu=float(), imageScaleV=float(),
                         isv=float(), insertBeforeDeformers=bool(), ibd=bool(), keepImageRatio=bool(), kir=bool(),
                         mapDirection=str(), md=str(), name=str(), n=str(), nodeState=int(), nds=int(),
                         projectionCenter=list, pc=list, projectionCenterX=float(), pcx=float(),
                         projectionCenterY=float(), pcy=float(), projectionCenterZ=float(), pcz=float(),
                         projectionHeight=float(), ph=float(), projectionScale=list, ps=list, projectionWidth=float(),
                         pw=float(), rotate=list, ro=list, rotateX=float(), rx=float(), rotateY=float(), ry=float(),
                         rotateZ=float(), rz=float(), rotationAngle=float(), ra=float(), smartFit=bool(), sf=bool(),
                         worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def subdToBlind(absolutePosition=bool(), ap=bool(), includeCreases=bool(), ic=bool(), includeZeroOffsets=bool(),
                izo=bool(), *args, **kwargs):
    pass


def subdToPoly(addUnderTransform=bool(), aut=bool(), applyMatrixToResult=bool(), amr=bool(), caching=bool(), cch=bool(),
               connectShaders=bool(), cs=bool(), constructionHistory=bool(), ch=bool(), copyUVTopology=bool(),
               cut=bool(), depth=int(), d=int(), extractPointPosition=bool(), epp=bool(), format=int(), f=int(),
               inSubdCVId=list, inSubdCVIdLeft=int(), isl=int(), inSubdCVIdRight=int(), isr=int(), maxPolys=int(),
               mp=int(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), outSubdCVId=list,
               os=list, outSubdCVIdLeft=int(), osl=int(), outSubdCVIdRight=int(), osr=int(), outv=int(), ov=int(),
               preserveVertexOrdering=bool(), pvo=bool(), sampleCount=int(), sc=int(), shareUVs=bool(), suv=bool(),
               subdNormals=bool(), un=bool(), *args, **kwargs):
    pass


def subdTransferUVsToCache(*args, **kwargs):
    pass


def substituteGeometry(disableNonSkinDeformers=bool(), dnd=bool(), newGeometryToLayer=bool(), ngl=bool(),
                       oldGeometryToLayer=bool(), ogl=bool(), reWeightDistTolerance=float(), wdt=float(),
                       retainOldGeometry=bool(), rog=bool(), *args, **kwargs):
    pass


def suitePrefs(applyToSuite=str(), ats=str(), installedAsSuite=bool(), ias=bool(), isCompleteSuite=bool(), ics=bool(),
               *args, **kwargs):
    pass


def surface(degreeU=int(), du=int(), degreeV=int(), dv=int(), formU=str(), fu=str(), formV=str(), fv=str(),
            knotU=float(), ku=float(), knotV=float(), kv=float(), name=str(), n=str(), objectSpace=bool(), ob=bool(),
            point=list, p=list, pointWeight=list, pw=list, worldSpace=bool(), ws=bool(), *args, **kwargs):
    pass


def surfaceSampler(camera=str(), cam=str(), fileFormat=str(), ff=str(), filename=str(), fn=str(), filterSize=float(),
                   fs=float(), filterType=int(), ft=int(), flipU=bool(), fu=bool(), flipV=bool(), fv=bool(),
                   ignoreMirroredFaces=bool(), imf=bool(), ignoreTransforms=bool(), it=bool(), mapHeight=int(),
                   mh=int(), mapMaterials=bool(), mm=bool(), mapOutput=str(), mo=str(), mapSpace=str(), sp=str(),
                   mapWidth=int(), mw=int(), maxSearchDistance=float(), msd=float(), maximumValue=float(), max=float(),
                   overscan=int(), os=int(), searchCage=str(), sc=str(), searchMethod=int(), sm=int(),
                   searchOffset=float(), so=float(), shadows=bool(), sh=bool(), source=str(), s=str(),
                   sourceUVSpace=str(), sus=str(), superSampling=int(), ss=int(), target=str(), t=str(),
                   targetUVSpace=str(), tus=str(), useGeometryNormals=bool(), ugn=bool(), uvSet=str(), uv=str(), *args,
                   **kwargs):
    pass


def surfaceShaderList(add=str(), remove=str(), rm=str(), *args, **kwargs):
    pass


def swatchDisplayPort(annotation=str(), ann=str(), backgroundColor=list, bgc=list, borderColor=list, bc=list,
                      borderWidth=int(), bw=int(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                      dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
                      enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                      ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                      isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                      numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
                      pressCommand=str(), pc=str(), preventOverride=bool(), po=bool(), renderPriority=int(), rp=int(),
                      renderSize=int(), rs=int(), shadingNode=str(), sn=str(), statusBarMessage=str(), sbm=str(),
                      useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                      width=int(), w=int(), widthHeight=list, wh=list, *args, **kwargs):
    pass


def swatchRefresh(*args, **kwargs):
    pass


def switchTable(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(),
                docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
                en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(),
                ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                isObscured=bool(), io=bool(), label1=str(), l1=str(), label2=str(), l2=str(), manage=bool(), m=bool(),
                noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), selectedRow=bool(), sr=bool(),
                statusBarMessage=str(), sbm=str(), switchNode=str(), sn=str(), underPointerRow=bool(), upr=bool(),
                useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                width=int(), w=int(), *args, **kwargs):
    pass


def symbolButton(annotation=str(), ann=str(), backgroundColor=list, bgc=list, command=str(), c=str(),
                 defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                 dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                 enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(),
                 height=int(), h=int(), highlightColor=list, hlc=list, image=str(), i=str(), isObscured=bool(),
                 io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(),
                 npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(),
                 po=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                 visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def symbolCheckBox(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(),
                   defineTemplate=str(), dt=str(), disableOffImage=str(), dfi=str(), disableOnImage=str(), dni=str(),
                   docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
                   en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(),
                   exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
                   highlightColor=list, hlc=list, image=str(), i=str(), innerMargin=bool(), im=bool(),
                   isObscured=bool(), io=bool(), ltVersion=str(), lt=str(), manage=bool(), m=bool(),
                   noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), offCommand=str(), ofc=str(),
                   offImage=str(), ofi=str(), onCommand=str(), onc=str(), onImage=str(), oni=str(), parent=str(),
                   p=str(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(),
                   statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(), value=bool(), v=bool(),
                   version=str(), ver=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                   width=int(), w=int(), *args, **kwargs):
    pass


def symmetricModelling(about=str(), a=str(), allowPartial=bool(), ap=bool(), axis=str(), ax=str(), preserveSeam=int(),
                       ps=int(), reset=bool(), r=bool(), seamFalloffCurve=str(), sf=str(), seamTolerance=float(),
                       st=float(), symmetry=int(), s=int(), tolerance=float(), t=float(), topoSymmetry=bool(),
                       ts=bool(), *args, **kwargs):
    pass


def sysFile(copy=str(), cp=str(), delete=bool(), makeDir=bool(), md=bool(), move=str(), mov=str(),
            removeEmptyDir=bool(), red=bool(), rename=str(), ren=str(), *args, **kwargs):
    pass


def tabLayout(annotation=str(), ann=str(), backgroundColor=list, bgc=list, borderStyle=str(), bs=str(),
              changeCommand=str(), cc=str(), childArray=bool(), ca=bool(), childResizable=bool(), cr=bool(),
              closeTab=int(), ct=int(), closeTabCommand=str(), ctc=str(), defineTemplate=str(), dt=str(), docTag=str(),
              dtg=str(), doubleClickCommand=str(), dcc=str(), dragCallback=str(), dgc=str(), dropCallback=str(),
              dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
              ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
              highlightColor=list, hlc=list, horizontalScrollBarThickness=int(), hst=int(), image=str(), i=str(),
              imageVisible=bool(), iv=bool(), innerMarginHeight=int(), imh=int(), innerMarginWidth=int(), imw=int(),
              isObscured=bool(), io=bool(), manage=bool(), m=bool(), minChildWidth=int(), mcw=int(), moveTab=list,
              mt=list, newTabCommand=str(), ntc=str(), noBackground=bool(), nbg=bool(), numberOfChildren=bool(),
              nch=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(),
              pma=bool(), postMenuCommand=str(), pmc=str(), preSelectCommand=str(), psc=str(), preventOverride=bool(),
              po=bool(), scrollable=bool(), scr=bool(), scrollableTabs=bool(), stb=bool(), selectCommand=str(),
              sc=str(), selectTab=str(), st=str(), selectTabIndex=int(), sti=int(), showNewTab=bool(), snt=bool(),
              statusBarMessage=str(), sbm=str(), tabIcon=list, ti=list, tabIconIndex=list, tii=list, tabLabel=list,
              tl=list, tabLabelIndex=list, tli=list, tabPosition=str(), tp=str(), tabTooltip=list, tt=list,
              tabTooltipIndex=list, tti=list, tabsClosable=bool(), tc=bool(), tabsVisible=bool(), tv=bool(),
              useTemplate=str(), ut=str(), verticalScrollBarThickness=int(), vst=int(), visible=bool(), vis=bool(),
              visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def tangentConstraint(aimVector=list, aim=list, layer=str(), l=str(), name=str(), n=str(), remove=bool(), rm=bool(),
                      targetList=bool(), tl=bool(), upVector=list, u=list, weight=float(), w=float(),
                      weightAliasList=bool(), wal=bool(), worldUpObject=str(), wuo=str(), worldUpType=str(), wut=str(),
                      worldUpVector=list, wu=list, *args, **kwargs):
    pass


def targetWeldCtx(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                  mergeToCenter=bool(), mtc=bool(), preserveUV=bool(), puv=bool(), *args, **kwargs):
    pass


def tension(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(), deformerTools=bool(),
            dt=bool(), envelope=float(), en=float(), exclusive=str(), ex=str(), frontOfChain=bool(), foc=bool(),
            geometry=str(), g=str(), geometryIndices=bool(), gi=bool(), ignoreSelected=bool(),
            includeHiddenSelections=bool(), ihs=bool(), inwardConstraint=float(), iwc=float(), name=str(), n=str(),
            outwardConstraint=float(), owc=float(), parallel=bool(), par=bool(), pinBorderVertices=bool(), pbv=bool(),
            prune=bool(), pr=bool(), remove=bool(), rm=bool(), smoothingIterations=int(), si=int(),
            smoothingStep=float(), ss=float(), split=bool(), sp=bool(), useComponentTags=bool(), uct=bool(), *args,
            **kwargs):
    pass


def texCutContext(adjustSize=bool(), asz=bool(), displayShellBorders=bool(), dsb=bool(), edgeSelectSensitive=float(),
                  ess=float(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(),
                  image2=str(), i2=str(), image3=str(), i3=str(), mode=str(), m=str(), moveRatio=float(), mvr=float(),
                  name=str(), n=str(), size=float(), sz=float(), steadyStroke=bool(), ss=bool(),
                  steadyStrokeDistance=float(), ssd=float(), touchToSew=bool(), tts=bool(), *args, **kwargs):
    pass


def texLatticeDeformContext(envelope=float(), ev=float(), exists=bool(), ex=bool(), history=bool(), ch=bool(),
                            image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                            latticeColumns=int(), lc=int(), latticeRows=int(), lr=int(), name=str(), n=str(),
                            showMoveManipulator=bool(), smm=bool(), snapPixelMode=bool(), spm=bool(),
                            useBoundingRect=bool(), ubr=bool(), *args, **kwargs):
    pass


def texManipContext(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                    *args, **kwargs):
    pass


def texMoveContext(editPivotMode=bool(), epm=bool(), exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(),
                   i2=str(), image3=str(), i3=str(), position=bool(), p=bool(), snap=bool(), s=bool(),
                   snapComponentsRelative=bool(), scr=bool(), snapPixelMode=int(), spm=int(), snapValue=float(),
                   sv=float(), tweakMode=bool(), twk=bool(), *args, **kwargs):
    pass


def texMoveUVShellContext(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(),
                          i3=str(), iterations=int(), it=int(), mask=bool(), m=bool(), position=bool(), p=bool(),
                          shellBorder=float(), sb=float(), *args, **kwargs):
    pass


def texRotateContext(editPivotMode=bool(), epm=bool(), exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(),
                     i2=str(), image3=str(), i3=str(), position=bool(), p=bool(), snap=bool(), s=bool(),
                     snapRelative=bool(), sr=bool(), snapValue=float(), sv=float(), tweakMode=bool(), twk=bool(), *args,
                     **kwargs):
    pass


def texScaleContext(editPivotMode=bool(), epm=bool(), exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(),
                    i2=str(), image3=str(), i3=str(), position=bool(), p=bool(), preventNegativeScale=bool(),
                    pns=bool(), snap=bool(), s=bool(), snapRelative=bool(), sr=bool(), snapValue=float(), sv=float(),
                    tweakMode=bool(), twk=bool(), *args, **kwargs):
    pass


def texSculptCacheContext(adjustSize=bool(), asz=bool(), adjustStrength=bool(), ast=bool(), direction=int(), d=int(),
                          falloffType=int(), ft=int(), floodPin=float(), fp=float(), grabTwist=bool(), gtw=bool(),
                          inverted=bool(), inv=bool(), mode=str(), m=str(), sculptFalloffCurve=str(), sfc=str(),
                          showBrushRingDuringStroke=bool(), sbr=bool(), size=float(), sz=float(), strength=float(),
                          st=float(), *args, **kwargs):
    pass


def texSelectContext(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                     *args, **kwargs):
    pass


def texSelectShortestPathCtx(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(),
                             i3=str(), *args, **kwargs):
    pass


def texSmudgeUVContext(dragSlider=str(), ds=str(), effectType=str(), et=str(), exists=bool(), ex=bool(),
                       functionType=str(), ft=str(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                       i2=str(), image3=str(), i3=str(), name=str(), n=str(), pressure=float(), prs=float(),
                       radius=float(), r=float(), smudgeIsMiddle=bool(), sim=bool(), *args, **kwargs):
    pass


def text(align=str(), al=str(), annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(),
         dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(),
         dropRectCallback=str(), drc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
         enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), font=str(), fn=str(), fullPathName=bool(),
         fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, hyperlink=bool(), hl=bool(),
         isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
         numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
         preventOverride=bool(), po=bool(), recomputeSize=bool(), rs=bool(), statusBarMessage=str(), sbm=str(),
         useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(),
         w=int(), wordWrap=bool(), ww=bool(), *args, **kwargs):
    pass


def textCurves(font=str(), f=str(), name=str(), n=str(), object=bool(), o=bool(), text=str(), t=str(), *args, **kwargs):
    pass


def textField(alwaysInvokeEnterCommandOnReturn=bool(), aie=bool(), annotation=str(), ann=str(), backgroundColor=list,
              bgc=list, changeCommand=str(), cc=str(), defineTemplate=str(), dt=str(), disableButtons=bool(), db=bool(),
              disableClearButton=bool(), dcb=bool(), disableHistoryButton=bool(), dhb=bool(), docTag=str(), dtg=str(),
              dragCallback=str(), dgc=str(), drawInactiveFrame=bool(), dif=bool(), dropCallback=str(), dpc=str(),
              editable=bool(), ed=bool(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
              enableKeyboardFocus=bool(), ekf=bool(), enterCommand=str(), ec=str(), exists=bool(), ex=bool(),
              fileName=str(), fi=str(), font=str(), fn=str(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
              highlightColor=list, hlc=list, insertText=str(), it=str(), insertionPosition=int(), ip=int(),
              isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
              numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), placeholderText=str(), pht=str(),
              popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), receiveFocusCommand=str(),
              rfc=str(), searchField=bool(), sf=bool(), statusBarMessage=str(), sbm=str(), text=str(), tx=str(),
              textChangedCommand=str(), tcc=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
              visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def textFieldButtonGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                       ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                       adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                       buttonCommand=str(), bc=str(), buttonLabel=str(), bl=str(), changeCommand=str(), cc=str(),
                       columnAlign=list, cal=list, columnAlign2=list, cl2=list, columnAlign3=list, cl3=list,
                       columnAlign4=list, cl4=list, columnAlign5=list, cl5=list, columnAlign6=list, cl6=list,
                       columnAttach=list, cat=list, columnAttach2=list, ct2=list, columnAttach3=list, ct3=list,
                       columnAttach4=list, ct4=list, columnAttach5=list, ct5=list, columnAttach6=list, ct6=list,
                       columnOffset2=list, co2=list, columnOffset3=list, co3=list, columnOffset4=list, co4=list,
                       columnOffset5=list, co5=list, columnOffset6=list, co6=list, columnWidth=list, cw=list,
                       columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list, columnWidth3=list, cw3=list,
                       columnWidth4=list, cw4=list, columnWidth5=list, cw5=list, columnWidth6=list, cw6=list,
                       defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
                       dropCallback=str(), dpc=str(), editable=bool(), ed=bool(), enable=bool(), en=bool(),
                       enableBackground=bool(), ebg=bool(), enableButton=bool(), eb=bool(), enableKeyboardFocus=bool(),
                       ekf=bool(), exists=bool(), ex=bool(), fileName=str(), fi=str(), forceChangeCommand=bool(),
                       fcc=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list,
                       hlc=list, insertText=str(), it=str(), insertionPosition=int(), ip=int(), isObscured=bool(),
                       io=bool(), label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                       numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), placeholderText=str(), pht=str(),
                       popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rowAttach=list, rat=list,
                       statusBarMessage=str(), sbm=str(), text=str(), tx=str(), textChangedCommand=str(), tcc=str(),
                       useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                       width=int(), w=int(), *args, **kwargs):
    pass


def textFieldGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                 ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                 adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                 changeCommand=str(), cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list,
                 columnAlign3=list, cl3=list, columnAlign4=list, cl4=list, columnAlign5=list, cl5=list,
                 columnAlign6=list, cl6=list, columnAttach=list, cat=list, columnAttach2=list, ct2=list,
                 columnAttach3=list, ct3=list, columnAttach4=list, ct4=list, columnAttach5=list, ct5=list,
                 columnAttach6=list, ct6=list, columnOffset2=list, co2=list, columnOffset3=list, co3=list,
                 columnOffset4=list, co4=list, columnOffset5=list, co5=list, columnOffset6=list, co6=list,
                 columnWidth=list, cw=list, columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list,
                 columnWidth3=list, cw3=list, columnWidth4=list, cw4=list, columnWidth5=list, cw5=list,
                 columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                 dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), editable=bool(), ed=bool(),
                 enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(),
                 exists=bool(), ex=bool(), fileName=str(), fi=str(), forceChangeCommand=bool(), fcc=bool(),
                 fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                 insertText=str(), it=str(), insertionPosition=int(), ip=int(), isObscured=bool(), io=bool(),
                 label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
                 numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), placeholderText=str(), pht=str(),
                 popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), rowAttach=list, rat=list,
                 statusBarMessage=str(), sbm=str(), text=str(), tx=str(), textChangedCommand=str(), tcc=str(),
                 useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                 width=int(), w=int(), *args, **kwargs):
    pass


def textManip(visible=bool(), v=bool(), *args, **kwargs):
    pass


def textScrollList(allItems=bool(), ai=bool(), allowAutomaticSelection=bool(), aas=bool(), allowMultiSelection=bool(),
                   ams=bool(), annotation=str(), ann=str(), append=str(), a=str(), appendPosition=list, ap=list,
                   backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(), deleteKeyCommand=str(), dkc=str(),
                   deselectAll=bool(), da=bool(), deselectIndexedItem=int(), dii=int(), deselectItem=str(), di=str(),
                   docTag=str(), dtg=str(), doubleClickCommand=str(), dcc=str(), dragCallback=str(), dgc=str(),
                   dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
                   enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), font=str(), fn=str(),
                   fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                   isObscured=bool(), io=bool(), lineFont=list, lf=list, manage=bool(), m=bool(), noBackground=bool(),
                   nbg=bool(), numberOfItems=bool(), ni=bool(), numberOfPopupMenus=bool(), npm=bool(),
                   numberOfRows=int(), nr=int(), numberOfSelectedItems=bool(), nsi=bool(), parent=str(), p=str(),
                   popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), removeAll=bool(), ra=bool(),
                   removeIndexedItem=int(), rii=int(), removeItem=str(), ri=str(), selectCommand=str(), sc=str(),
                   selectIndexedItem=int(), sii=int(), selectItem=str(), si=str(), selectUniqueTagItem=str(), sut=str(),
                   showIndexedItem=int(), shi=int(), statusBarMessage=str(), sbm=str(), uniqueTag=str(), utg=str(),
                   useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                   width=int(), w=int(), *args, **kwargs):
    pass


def textureDeformer(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(),
                    deformerTools=bool(), dt=bool(), direction=str(), d=str(), envelope=float(), en=float(),
                    exclusive=str(), ex=str(), frontOfChain=bool(), foc=bool(), geometry=str(), g=str(),
                    geometryIndices=bool(), gi=bool(), ignoreSelected=bool(), includeHiddenSelections=bool(),
                    ihs=bool(), name=str(), n=str(), offset=float(), o=float(), parallel=bool(), par=bool(),
                    pointSpace=str(), ps=str(), prune=bool(), pr=bool(), remove=bool(), rm=bool(), split=bool(),
                    sp=bool(), strength=float(), s=float(), useComponentTags=bool(), uct=bool(), vectorOffset=list,
                    vo=list, vectorSpace=str(), vsp=str(), vectorStrength=list, vs=list, *args, **kwargs):
    pass


def texturePlacementContext(exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
                            i2=str(), image3=str(), i3=str(), labelMapping=bool(), lm=bool(), name=str(), n=str(),
                            *args, **kwargs):
    pass


def textureWindow(activeSelectionOnTop=bool(), ast=bool(), axesColor=list, axc=list, backFacingColor=list, bfc=list,
                  capture=str(), cpt=str(), captureSequenceNumber=int(), csn=int(), changeCommand=list, cc=list,
                  checkerColor1=list, cc1=list, checkerColor2=list, cc2=list, checkerColorMode=int(), ccm=int(),
                  checkerDensity=int(), cd=int(), checkerDrawTileLabels=bool(), cdt=bool(), checkerGradient1=list,
                  cg1=list, checkerGradient2=list, cg2=list, checkerGradientOverlay=bool(), cgo=bool(),
                  checkerTileLabelColor=list, ctc=list, clearImage=bool(), ci=bool(), cmEnabled=bool(), cme=bool(),
                  control=bool(), ctl=bool(), defineTemplate=str(), dt=str(), displayAxes=bool(), dax=bool(),
                  displayCheckered=bool(), dct=bool(), displayDistortion=bool(), ddt=bool(),
                  displayDivisionLines=bool(), ddl=bool(), displayGridLines=bool(), dgl=bool(), displayImage=int(),
                  di=int(), displayIsolateSelectHUD=bool(), dih=bool(), displayLabels=bool(), dl=bool(),
                  displayOverlappingUVCountHUD=bool(), doh=bool(), displayPreselection=bool(), dps=bool(),
                  displayReversedUVCountHUD=bool(), drh=bool(), displaySolidMap=bool(), dsm=bool(), displayStyle=str(),
                  dst=str(), displayTextureBorder=bool(), dtb=bool(), displayUVPositionHUD=bool(), duv=bool(),
                  displayUVShellCountHUD=bool(), dsh=bool(), displayUVStatisticsHUD=bool(), duh=bool(),
                  displayUsedPercentageHUD=bool(), dph=bool(), distortionAlpha=float(), dta=float(),
                  distortionPerObject=bool(), dpo=bool(), divisions=int(), d=int(), docTag=str(), dtg=str(),
                  doubleBuffer=bool(), dbf=bool(), drawAxis=bool(), da=bool(), drawSubregions=bool(), dsr=bool(),
                  exists=bool(), ex=bool(), exposure=float(), exp=float(), filter=str(), f=str(),
                  forceMainConnection=str(), fmc=str(), forceRebake=bool(), frb=bool(), frameAll=bool(), fa=bool(),
                  frameSelected=bool(), fs=bool(), frontFacingColor=list, ffc=list, gamma=float(), ga=float(),
                  gridLinesColor=list, glc=list, gridNumbersColor=list, gnc=list, highlightConnection=str(), hlc=str(),
                  imageBaseColor=list, ibc=list, imageDim=bool(), idm=bool(), imageDisplay=bool(), id=bool(),
                  imageNames=bool(), imn=bool(), imageNumber=int(), imagePixelSnap=bool(), ip=bool(), imageRatio=bool(),
                  imr=bool(), imageRatioValue=float(), irv=float(), imageSize=bool(), imageTileRange=list, itr=list,
                  imageUnfiltered=bool(), iuf=bool(), internalFaces=bool(), labelPosition=str(), lp=str(),
                  loadImage=str(), li=str(), lockMainConnection=bool(), lck=bool(), mainListConnection=str(), mlc=str(),
                  maxResolution=int(), mrs=int(), multiColorAlpha=float(), mca=float(), nbImages=bool(), nim=bool(),
                  nextView=bool(), nv=bool(), numUvSets=bool(), nuv=bool(), numberOfImages=int(), ni=int(),
                  numberOfTextures=int(), nt=int(), panel=str(), pnl=str(), parent=str(), p=str(), previousView=bool(),
                  pv=bool(), realSize=bool(), rs=bool(), refresh=bool(), ref=bool(), relatedFaces=bool(), rf=bool(),
                  removeAllImages=bool(), ra=bool(), removeImage=bool(), ri=bool(), rendererString=str(), rds=str(),
                  reset=bool(), r=bool(), saveImage=bool(), si=bool(), scaleBlue=float(), sb=float(),
                  scaleGreen=float(), sg=float(), scaleRed=float(), sr=float(), selectInternalFaces=bool(), sif=bool(),
                  selectRelatedFaces=bool(), srf=bool(), selectionConnection=str(), slc=str(), setUvSet=int(),
                  suv=int(), singleBuffer=bool(), sbf=bool(), size=float(), s=float(), solidMap3dView=bool(),
                  s3d=bool(), solidMapColorSeed=int(), scs=int(), solidMapPerShell=bool(), sps=bool(), spacing=float(),
                  sp=float(), stateString=bool(), sts=bool(), style=int(), st=int(), subdivisionLinesColor=list,
                  sdc=list, textureBorder3dView=bool(), t3d=bool(), textureBorderColor=list, tbc=list,
                  textureBorderWidth=int(), tbw=int(), textureNames=bool(), txn=bool(), textureNumber=int(), tn=int(),
                  tileLabels=bool(), tlb=bool(), tileLinesColor=list, tlc=list, toggle=bool(), tgl=bool(),
                  toggleExposure=bool(), tge=bool(), toggleGamma=bool(), tgg=bool(), unParent=bool(), up=bool(),
                  unlockMainConnection=bool(), ulk=bool(), updateMainConnection=bool(), upd=bool(), useFaceGroup=bool(),
                  uf=bool(), useTemplate=str(), ut=str(), usedPercentageHUDRange=list, upr=list, uvSets=bool(),
                  uvs=bool(), viewPortImage=bool(), vpi=bool(), viewTransformName=str(), vtn=str(),
                  wireframeComponentColor=list, wcc=list, wireframeObjectColor=list, woc=list, writeImage=str(),
                  wi=str(), *args, **kwargs):
    pass


def texTweakUVContext(exists=bool(), ex=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                      position=bool(), p=bool(), tolerance=float(), t=float(), *args, **kwargs):
    pass


def texWinToolCtx(alternateContext=bool(), ac=bool(), boxzoom=bool(), bz=bool(), dolly=bool(), do=bool(), exists=bool(),
                  ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(),
                  i3=str(), name=str(), n=str(), toolName=str(), tn=str(), track=bool(), tr=bool(), *args, **kwargs):
    pass


def threadCount(numberOfThreads=int(), n=int(), *args, **kwargs):
    pass


def threePointArcCtx(degree=int(), d=int(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(),
                     image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), spans=int(), s=int(), *args,
                     **kwargs):
    pass


def thumbnailCaptureComponent(capture=bool(), c=bool(), capturedFrameCount=bool(), cfc=bool(),
                              closeCurrentSession=bool(), ccs=bool(), delete=bool(), d=bool(), endFrame=int(), ef=int(),
                              fileDialogCallback=str(), fdc=str(), isSessionOpened=bool(), iso=bool(),
                              launchedFromOptionsBox=bool(), lfo=bool(), previewPath=bool(), pp=bool(),
                              removeProjectThumbnail=str(), rpt=str(), save=str(), s=str(), startFrame=int(), sf=int(),
                              *args, **kwargs):
    pass


def timeCode(mayaStartFrame=float(), msf=float(), productionStartFrame=float(), psf=float(),
             productionStartHour=float(), psh=float(), productionStartMinute=float(), psm=float(),
             productionStartSecond=float(), pss=float(), *args, **kwargs):
    pass


def timeControl(animCurveNames=bool(), acn=bool(), animLayerFilterOptions=str(), alf=str(), animLayerShowWeight=bool(),
                asw=bool(), annotation=str(), ann=str(), backgroundColor=list, bgc=list, beginScrub=bool(), bs=bool(),
                currentFrameColor=list, cfc=list, defineTemplate=str(), dt=str(), displaySound=bool(), ds=bool(),
                docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(),
                en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), endScrub=bool(),
                es=bool(), exists=bool(), ex=bool(), forceRedraw=bool(), fd=bool(), forceRefresh=bool(), fr=bool(),
                foregroundColor=list, fgc=list, fullPathName=bool(), fpn=bool(), globalTime=bool(), gt=bool(),
                greasePencilSequenceNames=bool(), gn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                isObscured=bool(), io=bool(), mainListConnection=str(), mlc=str(), manage=bool(), m=bool(),
                noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
                popupMenuArray=bool(), pma=bool(), pressCommand=str(), pc=str(), preventOverride=bool(), po=bool(),
                range=bool(), rng=bool(), rangeArray=bool(), ra=bool(), rangeVisible=bool(), rv=bool(),
                releaseCommand=str(), rc=str(), repeatChunkSize=float(), rcs=float(), repeatOnHold=bool(), roh=bool(),
                resample=bool(), r=bool(), showGreaseFrames=str(), sg=str(), showKeys=str(), sk=str(),
                showKeysCombined=bool(), skc=bool(), snap=bool(), sn=bool(), sound=str(), s=str(),
                statusBarMessage=str(), sbm=str(), tickSize=int(), ts=int(), tickSpan=int(), tsp=int(),
                useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
                waveform=str(), wf=str(), width=int(), w=int(), *args, **kwargs):
    pass


def timeEditor(allClips=str(), alc=str(), clipId=int(), id=int(), commonParentTrack=bool(), cpt=bool(),
               composition=str(), cp=str(), drivingClipsForAttr=str(), dca=str(), drivingClipsForObj=list, dco=list,
               includeParent=bool(), ip=bool(), mute=bool(), m=bool(), selectedClips=str(), sc=str(),
               topLevelClips=str(), tlc=str(), *args, **kwargs):
    pass


def timeEditorAnimSource(addObjects=str(), ao=str(), addRelatedKG=bool(), akg=bool(), addSelectedObjects=bool(),
                         aso=bool(), addSource=str(), asc=str(), apply=bool(), ap=bool(), attribute=str(), at=str(),
                         bakeToAnimSource=str(), bas=str(), calculateTiming=bool(), ct=bool(), copyAnimation=bool(),
                         cp=bool(), drivenClips=bool(), dc=bool(), exclusive=bool(), exc=bool(), export=str(), ex=str(),
                         importAllFbxTakes=bool(), aft=bool(), importFbx=str(), fbx=str(), importFbxTakes=str(),
                         ft=str(), importMayaFile=str(), mf=str(), importOption=str(), io=str(),
                         importPopulateOption=str(), ipo=str(), importedContainerNames=str(), icn=str(),
                         includeRoot=bool(), irt=bool(), isUnique=bool(), iu=bool(), populateImportedAnimSources=str(),
                         pia=str(), poseClip=bool(), poc=bool(), recursively=bool(), rec=bool(),
                         removeSceneAnimation=bool(), rsa=bool(), removeSource=str(), rs=str(),
                         showAnimSourceRemapping=bool(), sar=bool(), takeList=str(), tl=str(), takesToImport=str(),
                         toi=str(), targetIndex=str(), ti=str(), targets=bool(), trg=bool(), type=str(), typ=str(),
                         *args, **kwargs):
    pass


def timeEditorBakeClips(bakeToAnimSource=str(), bas=str(), bakeToClip=str(), btc=str(), clipId=int(), id=int(),
                        combineLayers=bool(), cl=bool(), forceSampling=bool(), fs=bool(), keepOriginalClip=bool(),
                        koc=bool(), path=str(), pt=str(), sampleBy=float(), sb=float(), targetTrackIndex=int(),
                        tti=int(), targetTracksNode=str(), ttn=str(), *args, **kwargs):
    pass


def timeEditorClip(absolute=bool(), abs=bool(), addAttribute=str(), aa=str(), addObjects=str(), ao=str(),
                   addRelatedKG=bool(), akg=bool(), addSelectedObjects=bool(), aso=bool(), allowShrinking=bool(),
                   eas=bool(), animSource=str(), asr=str(), attribute=str(), at=str(), audio=str(), au=str(),
                   blendMode=int(), bm=int(), children=int(), chl=int(), clipAfter=bool(), ca=bool(), clipBefore=bool(),
                   cb=bool(), clipDataType=bool(), cdt=bool(), clipId=int(), id=int(), clipIdFromNodeName=int(),
                   idn=int(), clipIdFromPath=bool(), idp=bool(), clipNode=bool(), cln=bool(), clipPath=bool(),
                   clp=bool(), copyClip=bool(), ccl=bool(), crossfadeMode=int(), cfm=int(), crossfadePlug=bool(),
                   cfp=bool(), curveTime=float(), cvt=float(), defaultGhostRoot=bool(), dgr=bool(),
                   drivenAttributes=bool(), dat=bool(), drivenClipsBySource=str(), dcs=str(), drivenObjects=bool(),
                   dos=bool(), drivenRootObjects=bool(), dro=bool(), drivingSources=str(), dsc=str(),
                   duplicateClip=bool(), dcl=bool(), duration=float(), d=float(), emptySource=bool(), ems=bool(),
                   endTime=float(), et=float(), exclusive=bool(), exc=bool(), existingOnly=bool(), exo=bool(),
                   exists=bool(), exs=bool(), explode=int(), epl=int(), exportAllClips=bool(), eac=bool(),
                   exportFbx=str(), ef=str(), extend=bool(), ex=bool(), extendParent=bool(), exp=bool(), ghost=bool(),
                   gh=bool(), ghostRootAdd=str(), gra=str(), ghostRootRemove=str(), grr=str(), group=bool(), grp=bool(),
                   holdEnd=float(), he=float(), holdStart=float(), hs=float(), importAllFbxTakes=bool(), aft=bool(),
                   importFbx=str(), fbx=str(), importFbxTakes=str(), ft=str(), importMayaFile=str(), mf=str(),
                   importOption=str(), io=str(), importPopulateOption=str(), ipo=str(), importTakeDestination=int(),
                   itd=int(), importedContainerNames=str(), icn=str(), includeRoot=bool(), irt=bool(),
                   isContainer=bool(), ict=bool(), listUserGhostRoot=bool(), lug=bool(), loopEnd=float(), le=float(),
                   loopStart=float(), ls=float(), minClipDuration=bool(), mcd=bool(), modifyAnimSource=bool(),
                   mas=bool(), moveClip=float(), mcl=float(), mute=bool(), m=bool(), name=str(), n=str(), parent=int(),
                   p=int(), parentClipId=int(), pid=int(), parentGroupId=bool(), pgd=bool(), pasteClip=float(),
                   pcl=float(), path=str(), pt=str(), populateImportedAnimSources=str(), pia=str(), poseClip=bool(),
                   poc=bool(), preserveAnimationTiming=bool(), pat=bool(), razorClip=float(), rcl=float(),
                   recursively=bool(), rec=bool(), remap=list, rmp=list, remapNamespace=list, rns=list,
                   remapSource=list, rs=list, remappedSourceAttrs=bool(), rms=bool(), remappedTargetAttrs=bool(),
                   rmt=bool(), removeAttribute=str(), ra=str(), removeClip=bool(), rmc=bool(), removeCrossfade=bool(),
                   rcf=bool(), removeSceneAnimation=bool(), rsa=bool(), removeWeightCurve=bool(), rwc=bool(),
                   resetTiming=bool(), rt=bool(), resetTransition=bool(), rtr=bool(), ripple=bool(), rpl=bool(),
                   rootClipId=int(), rti=int(), rootPath=str(), rpt=str(), scaleEnd=float(), sce=float(),
                   scalePivot=float(), scp=float(), scaleStart=float(), scs=float(), setKeyframe=str(), k=str(),
                   showAnimSourceRemapping=bool(), sar=bool(), speedRamping=int(), src=int(), startTime=float(),
                   s=float(), takeList=str(), tl=str(), takesToImport=str(), toi=str(), timeWarp=bool(), tw=bool(),
                   timeWarpCurve=bool(), twc=bool(), timeWarpType=int(), twt=int(), track=str(), trk=str(),
                   tracksNode=bool(), trn=bool(), transition=bool(), tra=bool(), trimEnd=float(), tre=float(),
                   trimStart=float(), trs=float(), truncated=bool(), trc=bool(), type=str(), typ=str(),
                   uniqueAnimSource=bool(), uas=bool(), userGhostRoot=bool(), ugr=bool(), weightCurve=bool(), wc=bool(),
                   zeroKeying=bool(), zk=bool(), *args, **kwargs):
    pass


def timeEditorClipLayer(addAttribute=str(), aa=str(), addLayer=str(), al=str(), addObject=str(), ao=str(),
                        allLayers=bool(), all=bool(), attribute=str(), a=str(), attributeKeyable=str(), ak=str(),
                        clipId=int(), cid=int(), index=int(), idx=int(), keySiblings=bool(), ks=bool(), layerId=int(),
                        lid=int(), layerName=str(), ln=str(), mode=int(), m=int(), mute=bool(), mu=bool(), name=bool(),
                        n=bool(), path=str(), pt=str(), removeAttribute=str(), ra=str(), removeLayer=bool(), rl=bool(),
                        removeObject=str(), ro=str(), resetSolo=bool(), rs=bool(), setKeyframe=bool(), k=bool(),
                        solo=bool(), sl=bool(), zeroKeying=bool(), zk=bool(), *args, **kwargs):
    pass


def timeEditorClipOffset(applyToAllRoots=bool(), atr=bool(), clipId=int(), id=int(), matchClipId=int(), mci=int(),
                         matchDstTime=float(), mdt=float(), matchObj=str(), mob=str(), matchOffsetRot=bool(),
                         mor=bool(), matchOffsetTrans=bool(), mot=bool(), matchPath=str(), mpt=str(), matchRotOp=int(),
                         mro=int(), matchSrcTime=float(), mst=float(), matchTransOp=int(), mto=int(),
                         offsetTransform=bool(), oft=bool(), path=str(), pt=str(), resetMatch=int(), rsm=int(),
                         resetMatchPath=str(), rmp=str(), rootObj=str(), rob=str(), upVectorX=float(), upx=float(),
                         upVectorY=float(), upy=float(), upVectorZ=float(), upz=float(), *args, **kwargs):
    pass


def timeEditorComposition(active=bool(), act=bool(), allCompositions=bool(), acp=bool(), createTrack=bool(), ct=bool(),
                          delete=bool(), duplicateFrom=str(), df=str(), rename=list, ren=list, tracksNode=bool(),
                          tn=bool(), *args, **kwargs):
    pass


def timeEditorPanel(activeClipEditMode=int(), ace=int(), activeTabRootClipId=bool(), atr=bool(), activeTabTime=bool(),
                    att=bool(), activeTabView=int(), atv=int(), autoFit=str(), af=str(), autoFitTime=str(), aft=str(),
                    control=bool(), ctl=bool(), defineTemplate=str(), dt=str(), displayActiveKeyTangents=str(),
                    dat=str(), displayActiveKeys=str(), dak=str(), displayInfinities=str(), di=str(), displayKeys=str(),
                    dk=str(), displayTangents=str(), dtn=str(), displayValues=str(), dv=str(), docTag=str(), dtg=str(),
                    exists=bool(), ex=bool(), filter=str(), f=str(), forceMainConnection=str(), fmc=str(),
                    groupIdForTabView=int(), gtv=int(), highlightConnection=str(), hlc=str(), keyingTarget=int(),
                    kt=int(), layerId=int(), l=int(), lockMainConnection=bool(), lck=bool(), lookAt=str(), la=str(),
                    mainListConnection=str(), mlc=str(), menu=str(), m=str(), minClipWidth=int(), mcw=int(),
                    panel=str(), pnl=str(), parent=str(), p=str(), selectionConnection=str(), slc=str(),
                    setToPrevClipEditMode=bool(), spe=bool(), snapTime=str(), st=str(), snapToClip=bool(), stc=bool(),
                    snapToFrame=bool(), stf=bool(), snapTolerance=int(), sto=int(), snapValue=str(), sv=str(),
                    stateString=bool(), sts=bool(), tabView=int(), tv=int(), timeCursor=bool(), tc=bool(),
                    unParent=bool(), up=bool(), unlockMainConnection=bool(), ulk=bool(), updateMainConnection=bool(),
                    upd=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def timeEditorTracks(activeClipWeight=float(), acw=float(), activeClipWeightId=float(), aci=float(), addTrack=int(),
                     at=int(), allClips=bool(), ac=bool(), allTracks=bool(), atc=bool(), allTracksRecursive=bool(),
                     atr=bool(), composition=bool(), cp=bool(), path=str(), pt=str(), plugIndex=int(), pi=int(),
                     removeTrack=int(), rt=int(), removeTrackByPath=str(), rtp=str(), reorderTrack=list, rot=list,
                     resetMute=bool(), rm=bool(), resetSolo=bool(), rs=bool(), selectedTracks=bool(), st=bool(),
                     trackGhost=bool(), tgh=bool(), trackIndex=int(), ti=int(), trackMuted=bool(), tm=bool(),
                     trackName=str(), tn=str(), trackSolo=bool(), ts=bool(), trackType=int(), tt=int(), *args,
                     **kwargs):
    pass


def timeField(annotation=str(), ann=str(), backgroundColor=list, bgc=list, changeCommand=str(), cc=str(),
              defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(), dragCommand=str(),
              dc=str(), dropCallback=str(), dpc=str(), editable=bool(), ed=bool(), enable=bool(), en=bool(),
              enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), enterCommand=str(), ec=str(),
              exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list,
              hlc=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
              numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
              precision=int(), pre=int(), preventOverride=bool(), po=bool(), receiveFocusCommand=str(), rfc=str(),
              statusBarMessage=str(), sbm=str(), step=float(), s=float(), useTemplate=str(), ut=str(), value=float(),
              v=float(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args,
              **kwargs):
    pass


def timeFieldGrp(adjustableColumn=int(), adj=int(), adjustableColumn2=int(), ad2=int(), adjustableColumn3=int(),
                 ad3=int(), adjustableColumn4=int(), ad4=int(), adjustableColumn5=int(), ad5=int(),
                 adjustableColumn6=int(), ad6=int(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
                 changeCommand=str(), cc=str(), columnAlign=list, cal=list, columnAlign2=list, cl2=list,
                 columnAlign3=list, cl3=list, columnAlign4=list, cl4=list, columnAlign5=list, cl5=list,
                 columnAlign6=list, cl6=list, columnAttach=list, cat=list, columnAttach2=list, ct2=list,
                 columnAttach3=list, ct3=list, columnAttach4=list, ct4=list, columnAttach5=list, ct5=list,
                 columnAttach6=list, ct6=list, columnOffset2=list, co2=list, columnOffset3=list, co3=list,
                 columnOffset4=list, co4=list, columnOffset5=list, co5=list, columnOffset6=list, co6=list,
                 columnWidth=list, cw=list, columnWidth1=int(), cw1=int(), columnWidth2=list, cw2=list,
                 columnWidth3=list, cw3=list, columnWidth4=list, cw4=list, columnWidth5=list, cw5=list,
                 columnWidth6=list, cw6=list, defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
                 dragCallback=str(), dgc=str(), dragCommand=str(), dc=str(), dropCallback=str(), dpc=str(),
                 enable=bool(), en=bool(), enable1=bool(), en1=bool(), enable2=bool(), en2=bool(), enable3=bool(),
                 en3=bool(), enable4=bool(), en4=bool(), enableBackground=bool(), ebg=bool(),
                 enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), extraLabel=str(), el=str(),
                 fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
                 isObscured=bool(), io=bool(), label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(),
                 nbg=bool(), numberOfFields=int(), nf=int(), numberOfPopupMenus=bool(), npm=bool(), parent=str(),
                 p=str(), popupMenuArray=bool(), pma=bool(), precision=int(), pre=int(), preventOverride=bool(),
                 po=bool(), rowAttach=list, rat=list, statusBarMessage=str(), sbm=str(), step=float(), s=float(),
                 useTemplate=str(), ut=str(), value=list, v=list, value1=float(), v1=float(), value2=float(),
                 v2=float(), value3=float(), v3=float(), value4=float(), v4=float(), visible=bool(), vis=bool(),
                 visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def timePort(annotation=str(), ann=str(), backgroundColor=list, bgc=list, defineTemplate=str(), dt=str(), docTag=str(),
             dtg=str(), dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
             enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
             fullPathName=bool(), fpn=bool(), globalTime=bool(), gt=bool(), height=int(), h=int(), highlightColor=list,
             hlc=list, isObscured=bool(), io=bool(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
             numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
             preventOverride=bool(), po=bool(), snap=bool(), sn=bool(), statusBarMessage=str(), sbm=str(),
             useTemplate=str(), ut=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(),
             width=int(), w=int(), *args, **kwargs):
    pass


def timer(endTimer=bool(), e=bool(), lapTime=bool(), lap=bool(), name=str(), n=str(), startTimer=bool(), s=bool(),
          *args, **kwargs):
    pass


def timerX(startTime=float(), st=float(), *args, **kwargs):
    pass


def timeWarp(deleteFrame=int(), df=int(), frame=float(), f=float(), g=bool(), interpType=list, it=list, moveFrame=list,
             mf=list, *args, **kwargs):
    pass


def toggle(above=bool(), a=bool(), below=bool(), b=bool(), boundary=bool(), bn=bool(), boundingBox=bool(), box=bool(),
           controlVertex=bool(), cv=bool(), doNotWrite=bool(), dnw=bool(), editPoint=bool(), ep=bool(), extent=bool(),
           et=bool(), facet=bool(), f=bool(), geometry=bool(), g=bool(), gl=bool(), highPrecisionNurbs=bool(),
           hpn=bool(), hull=bool(), hl=bool(), latticePoint=bool(), lp=bool(), latticeShape=bool(), ls=bool(),
           localAxis=bool(), la=bool(), newCurve=bool(), nc=bool(), newPolymesh=bool(), np=bool(), newSurface=bool(),
           ns=bool(), normal=bool(), nr=bool(), origin=bool(), o=bool(), point=bool(), pt=bool(), pointDisplay=bool(),
           pd=bool(), pointFacet=bool(), pf=bool(), rotatePivot=bool(), rp=bool(), scalePivot=bool(), sp=bool(),
           selectHandle=bool(), sh=bool(), state=bool(), st=bool(), surfaceFace=bool(), sf=bool(), template=bool(),
           te=bool(), uvCoords=bool(), uv=bool(), vertex=bool(), vt=bool(), *args, **kwargs):
    pass


def toggleAxis(origin=bool(), o=bool(), view=bool(), v=bool(), *args, **kwargs):
    pass


def toggleDisplacement(*args, **kwargs):
    pass


def toggleWindowVisibility(*args, **kwargs):
    pass


def tolerance(angular=float(), a=float(), linear=float(), l=float(), *args, **kwargs):
    pass


def toolBar(allowedArea=str(), aa=str(), annotation=str(), ann=str(), area=str(), a=str(), backgroundColor=list,
            bgc=list, content=str(), con=str(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(),
            dragCallback=str(), dgc=str(), dropCallback=str(), dpc=str(), enable=bool(), en=bool(),
            enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(),
            fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list, isObscured=bool(),
            io=bool(), label=str(), l=str(), manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
            numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(), popupMenuArray=bool(), pma=bool(),
            preventOverride=bool(), po=bool(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
            visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def toolButton(allowMultipleTools=bool(), amt=bool(), annotation=str(), ann=str(), backgroundColor=list, bgc=list,
               changeCommand=str(), cc=str(), collection=str(), cl=str(), defineTemplate=str(), dt=str(), docTag=str(),
               dtg=str(), doubleClickCommand=str(), dcc=str(), dragCallback=str(), dgc=str(), dropCallback=str(),
               dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(), enableKeyboardFocus=bool(),
               ekf=bool(), exists=bool(), ex=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
               highlightColor=list, hlc=list, image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
               imageOverlayLabel=str(), iol=str(), isObscured=bool(), io=bool(), ltVersion=str(), lt=str(),
               manage=bool(), m=bool(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(),
               offCommand=str(), ofc=str(), onCommand=str(), onc=str(), parent=str(), p=str(),
               popupIndicatorVisible=bool(), piv=bool(), popupMenuArray=bool(), pma=bool(), preventOverride=bool(),
               po=bool(), select=bool(), sl=bool(), statusBarMessage=str(), sbm=str(), style=str(), st=str(),
               tool=str(), t=str(), toolArray=bool(), ta=bool(), toolCount=bool(), tc=bool(), toolImage1=list, ti1=list,
               toolImage2=list, ti2=list, toolImage3=list, ti3=list, useTemplate=str(), ut=str(), version=str(),
               ver=str(), visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), width=int(), w=int(),
               *args, **kwargs):
    pass


def toolCollection(collectionItemArray=bool(), cia=bool(), defineTemplate=str(), dt=str(), exists=bool(), ex=bool(),
                   gl=bool(), numberOfCollectionItems=bool(), nci=bool(), parent=str(), p=str(), select=str(), sl=str(),
                   useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def toolDropped(*args, **kwargs):
    pass


def toolHasOptions(*args, **kwargs):
    pass


def toolPropertyWindow(field=str(), fld=str(), helpButton=str(), hb=str(), icon=str(), icn=str(), inMainWindow=bool(),
                       imw=bool(), location=str(), loc=str(), noviceMode=bool(), nm=bool(), resetButton=str(), rb=str(),
                       restore=bool(), rs=bool(), selectCommand=str(), sel=str(), showCommand=str(), shw=str(), *args,
                       **kwargs):
    pass


def torus(axis=list, ax=list, caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), degree=int(), d=int(),
          endSweep=float(), esw=float(), heightRatio=float(), hr=float(), minorSweep=float(), msw=float(), name=str(),
          n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(), pivot=list, p=list, polygon=int(), po=int(),
          radius=float(), r=float(), sections=int(), s=int(), spans=int(), nsp=int(), startSweep=float(), ssw=float(),
          tolerance=float(), tol=float(), useTolerance=bool(), ut=bool(), *args, **kwargs):
    pass


def track(down=float(), d=float(), left=float(), l=float(), right=float(), r=float(), upDistance01=float(), u=float(),
          upDistance02=float(), up=float(), *args, **kwargs):
    pass


def trackCtx(alternateContext=bool(), ac=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(),
             i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), toolName=str(), tn=str(),
             trackGeometry=bool(), tg=bool(), trackScale=float(), ts=float(), *args, **kwargs):
    pass


def transferAttributes(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(),
                       colorBorders=int(), clb=int(), deformerTools=bool(), dt=bool(), exclusive=str(), ex=str(),
                       flipUVs=int(), fuv=int(), frontOfChain=bool(), foc=bool(), geometry=str(), g=str(),
                       geometryIndices=bool(), gi=bool(), ignoreSelected=bool(), includeHiddenSelections=bool(),
                       ihs=bool(), matchChoice=int(), mch=int(), name=str(), n=str(), parallel=bool(), par=bool(),
                       prune=bool(), pr=bool(), remove=bool(), rm=bool(), sampleSpace=int(), spa=int(),
                       searchMethod=int(), sm=int(), searchScaleX=float(), ssx=float(), searchScaleY=float(),
                       ssy=float(), searchScaleZ=float(), ssz=float(), sourceColorSet=str(), scs=str(),
                       sourceUvSet=str(), suv=str(), sourceUvSpace=str(), sus=str(), split=bool(), sp=bool(),
                       targetColorSet=str(), tcs=str(), targetUvSet=str(), tuv=str(), targetUvSpace=str(), tus=str(),
                       transferColors=int(), col=int(), transferNormals=int(), nml=int(), transferPositions=int(),
                       pos=int(), transferUVs=int(), uvs=int(), useComponentTags=bool(), uct=bool(), *args, **kwargs):
    pass


def transferShadingSets(sampleSpace=int(), spa=int(), searchMethod=int(), sm=int(), *args, **kwargs):
    pass


def transformCompare(root=bool(), r=bool(), *args, **kwargs):
    pass


def transformLimits(enableRotationX=list, erx=list, enableRotationY=list, ery=list, enableRotationZ=list, erz=list,
                    enableScaleX=list, esx=list, enableScaleY=list, esy=list, enableScaleZ=list, esz=list,
                    enableTranslationX=list, etx=list, enableTranslationY=list, ety=list, enableTranslationZ=list,
                    etz=list, remove=bool(), rm=bool(), rotationX=list, rx=list, rotationY=list, ry=list,
                    rotationZ=list, rz=list, scaleX=list, sx=list, scaleY=list, sy=list, scaleZ=list, sz=list,
                    translationX=list, tx=list, translationY=list, ty=list, translationZ=list, tz=list, *args,
                    **kwargs):
    pass


def translator(defaultFileRule=bool(), dfr=bool(), defaultOptions=str(), do=str(), extension=bool(), ext=bool(),
               fileCompression=str(), cmp=str(), filter=bool(), f=bool(), list=bool(), l=bool(), loaded=bool(),
               ld=bool(), objectType=bool(), ot=bool(), optionsScript=bool(), os=bool(), readSupport=bool(), rs=bool(),
               writeSupport=bool(), ws=bool(), *args, **kwargs):
    pass


def treeLister(addFavorite=str(), af=str(), addItem=list, add=list, addVnnItem=list, avi=list, annotation=str(),
               ann=str(), backgroundColor=list, bgc=list, clearContents=bool(), clr=bool(), collapsePath=str(),
               cp=str(), defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
               dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
               enableKeyboardFocus=bool(), ekf=bool(), executeItem=str(), ei=str(), exists=bool(), ex=bool(),
               expandPath=str(), ep=str(), expandToDepth=int(), etd=int(), favoritesCallback=str(), fcb=str(),
               favoritesList=bool(), fl=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(),
               highlightColor=list, hlc=list, isObscured=bool(), io=bool(), itemScript=str(), isc=str(), manage=bool(),
               m=bool(), noBackground=bool(), nbg=bool(), numberOfPopupMenus=bool(), npm=bool(), parent=str(), p=str(),
               popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), refreshCommand=str(), rc=str(),
               removeFavorite=str(), rf=str(), removeItem=str(), rem=str(), resultsPathUnderCursor=bool(), ruc=bool(),
               selectPath=str(), sp=str(), statusBarMessage=str(), sbm=str(), useTemplate=str(), ut=str(),
               visible=bool(), vis=bool(), visibleChangeCommand=str(), vcc=str(), vnnString=bool(), vnn=bool(),
               width=int(), w=int(), *args, **kwargs):
    pass


def treeView(addItem=list, ai=list, allowDragAndDrop=bool(), adr=bool(), allowHiddenParents=bool(), ahp=bool(),
             allowMultiSelection=bool(), ams=bool(), allowReparenting=bool(), arp=bool(), annotation=str(), ann=str(),
             attachButtonRight=int(), abr=int(), backgroundColor=list, bgc=list, borderHighlite=list, bh=list,
             borderHighliteColor=list, bcl=list, buttonErase=list, bef=list, buttonState=list, bst=list,
             buttonStyle=list, bs=list, buttonTextIcon=list, bti=list, buttonTooltip=list, btp=list,
             buttonTransparencyColor=list, btc=list, buttonTransparencyOverride=list, bto=list, buttonVisible=list,
             bvf=list, children=str(), ch=str(), clearSelection=bool(), cs=bool(), contextMenuCommand=str(), cmc=str(),
             defineTemplate=str(), dt=str(), displayLabel=list, dl=list, displayLabelSuffix=list, dls=list,
             docTag=str(), dtg=str(), dragAndDropCommand=str(), dad=str(), dragCallback=str(), dgc=str(),
             dropCallback=str(), dpc=str(), editLabelCommand=str(), elc=str(), enable=bool(), en=bool(),
             enableBackground=bool(), ebg=bool(), enableButton=list, eb=list, enableKeyboardFocus=bool(), ekf=bool(),
             enableKeys=bool(), enk=bool(), enableLabel=list, enl=list, exists=bool(), ex=bool(),
             expandCollapseCommand=str(), ecc=str(), expandItem=list, ei=list, flatButton=int(), fb=int(), font=list,
             fn=list, fontFace=list, ff=list, fullPathName=bool(), fpn=bool(), height=int(), h=int(),
             hideButtons=bool(), hb=bool(), highlightColor=list, hlc=list, highlite=list, hl=list, highliteColor=list,
             hc=list, ignoreButtonClick=list, ibc=list, image=list, i=list, insertItem=list, ii=list,
             isItemExpanded=str(), iie=str(), isLeaf=str(), il=str(), isObscured=bool(), io=bool(), item=str(),
             it=str(), itemAnnotation=list, ia=list, itemDblClickCommand=str(), idc=str(), itemDblClickCommand2=str(),
             dc2=str(), itemExists=str(), iex=str(), itemIndex=str(), idx=str(), itemParent=str(), ip=str(),
             itemRenamedCommand=str(), irc=str(), itemSelected=str(), isl=str(), itemVisible=list, iv=list,
             labelBackgroundColor=list, lbc=list, manage=bool(), m=bool(), noBackground=bool(), nbg=bool(),
             numberOfButtons=int(), nb=int(), numberOfPopupMenus=bool(), npm=bool(), ornament=list, ornamentColor=list,
             orc=list, parent=str(), p=str(), popupMenuArray=bool(), pma=bool(), pressCommand=list, pc=list,
             preventOverride=bool(), po=bool(), removeAll=bool(), ra=bool(), removeItem=str(), ri=str(),
             reverseTreeOrder=bool(), rto=bool(), rightPressCommand=list, rpc=list, select=list, sl=list,
             selectCommand=str(), sc=str(), selectItem=list, si=list, selectionChangedCommand=str(), scc=str(),
             selectionColor=list, scl=list, showItem=str(), shi=str(), statusBarMessage=str(), sbm=str(),
             textColor=list, tc=list, useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
             visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), *args, **kwargs):
    pass


def trim(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), locatorU=float(), lu=float(),
         locatorV=float(), lv=float(), name=str(), n=str(), nodeState=int(), nds=int(), object=bool(), o=bool(),
         selected=int(), sl=int(), shrink=bool(), sh=bool(), tolerance=float(), tol=float(), *args, **kwargs):
    pass


def truncateFluidCache(*args, **kwargs):
    pass


def truncateHairCache(*args, **kwargs):
    pass


def tumble(azimuthAngle=float(), aa=float(), elevationAngle=float(), ea=float(), localTumble=int(), lt=int(),
           pivotPoint=list, pp=list, rotationAngles=list, ra=list, *args, **kwargs):
    pass


def tumbleCtx(alternateContext=bool(), ac=bool(), autoOrthoConstrain=bool(), aoc=bool(), autoSetPivot=bool(),
              asp=bool(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(),
              i2=str(), image3=str(), i3=str(), localTumble=int(), lt=int(), name=str(), n=str(), objectTumble=bool(),
              ot=bool(), orthoLock=bool(), ol=bool(), orthoStep=float(), os=float(), toolName=str(), tn=str(),
              tumbleScale=float(), ts=float(), *args, **kwargs):
    pass


def turbulence(attenuation=float(), att=float(), frequency=float(), f=float(), magnitude=float(), m=float(),
               maxDistance=float(), mxd=float(), name=str(), n=str(), noiseLevel=int(), nsl=int(), noiseRatio=float(),
               nsr=float(), perVertex=bool(), pv=bool(), phase=float(), p=float(), phaseX=float(), px=float(),
               phaseY=float(), py=float(), phaseZ=float(), pz=float(), position=list, pos=list,
               torusSectionRadius=float(), tsr=float(), volumeExclusion=bool(), vex=bool(), volumeOffset=list, vof=list,
               volumeShape=str(), vsh=str(), volumeSweep=float(), vsw=float(), *args, **kwargs):
    pass


def twoPointArcCtx(degree=int(), d=int(), exists=bool(), ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(),
                   image2=str(), i2=str(), image3=str(), i3=str(), name=str(), n=str(), spans=int(), s=int(), *args,
                   **kwargs):
    pass


def ubercam(*args, **kwargs):
    pass


def uiTemplate(defineTemplate=str(), dt=str(), exists=bool(), ex=bool(), useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def unassignInputDevice(clutch=str(), c=str(), device=str(), d=str(), *args, **kwargs):
    pass


def undo(*args, **kwargs):
    pass


def undoInfo(chunkName=str(), cn=str(), closeChunk=bool(), cck=bool(), infinity=bool(), length=int(), l=int(),
             openChunk=bool(), ock=bool(), printQueue=bool(), pq=bool(), printRedoQueue=bool(), prq=bool(),
             redoName=str(), rn=str(), redoQueueEmpty=bool(), rqe=bool(), state=bool(), st=bool(),
             stateWithoutFlush=bool(), swf=bool(), undoName=str(), un=str(), undoQueueEmpty=bool(), uqe=bool(), *args,
             **kwargs):
    pass


def unfold(applyToShell=bool(), areaWeight=float(), aw=float(), globalBlend=float(), gb=float(),
           globalMethodBlend=float(), gmb=float(), iterations=int(), i=int(), optimizeAxis=int(), oa=int(),
           pinSelected=bool(), ps=bool(), pinUvBorder=bool(), pub=bool(), scale=float(), s=float(),
           stoppingThreshold=float(), ss=float(), useScale=bool(), us=bool(), *args, **kwargs):
    pass


def ungroup(absolute=bool(), a=bool(), parent=str(), p=str(), relative=bool(), r=bool(), world=bool(), w=bool(), *args,
            **kwargs):
    pass


def uniform(attenuation=float(), att=float(), directionX=float(), dx=float(), directionY=float(), dy=float(),
            directionZ=float(), dz=float(), magnitude=float(), m=float(), maxDistance=float(), mxd=float(), name=str(),
            n=str(), perVertex=bool(), pv=bool(), position=list, pos=list, torusSectionRadius=float(), tsr=float(),
            volumeExclusion=bool(), vex=bool(), volumeOffset=list, vof=list, volumeShape=str(), vsh=str(),
            volumeSweep=float(), vsw=float(), *args, **kwargs):
    pass


def unknownNode(plugin=bool(), p=bool(), realClassName=bool(), rcn=bool(), realClassTag=bool(), rct=bool(), *args,
                **kwargs):
    pass


def unknownPlugin(dataTypes=bool(), dt=bool(), list=bool(), l=bool(), nodeTypes=bool(), nt=bool(), remove=bool(),
                  r=bool(), version=bool(), v=bool(), *args, **kwargs):
    pass


def unloadPlugin(addCallback=str(), ac=str(), force=bool(), f=bool(), removeCallback=str(), rc=str(), *args, **kwargs):
    pass


def untangleUV(mapBorder=str(), mb=str(), maxRelaxIterations=int(), mri=int(), pinBorder=bool(), pb=bool(),
               pinSelected=bool(), ps=bool(), pinUnselected=bool(), pu=bool(), relax=str(), r=str(),
               relaxTolerance=float(), rt=float(), shapeDetail=float(), sd=float(), *args, **kwargs):
    pass


def untrim(caching=bool(), cch=bool(), constructionHistory=bool(), ch=bool(), curveOnSurface=bool(), cos=bool(),
           name=str(), n=str(), noChanges=bool(), nc=bool(), nodeState=int(), nds=int(), object=bool(), o=bool(),
           replaceOriginal=bool(), rpo=bool(), untrimAll=bool(), all=bool(), *args, **kwargs):
    pass


def upAxis(axis=str(), ax=str(), rotateView=bool(), rv=bool(), *args, **kwargs):
    pass


def uvLink(b=bool(), isValid=bool(), iv=bool(), make=bool(), m=bool(), queryObject=str(), qo=str(), texture=str(),
           t=str(), uvSet=str(), uvs=str(), *args, **kwargs):
    pass


def uvSnapshot(antiAliased=bool(), aa=bool(), blueColor=int(), b=int(), entireUVRange=bool(), euv=bool(),
               fileFormat=str(), ff=str(), greenColor=int(), g=int(), name=str(), n=str(), overwrite=bool(), o=bool(),
               redColor=int(), r=int(), uMax=float(), umx=float(), uMin=float(), umn=float(), uvSetName=str(),
               uvs=str(), vMax=float(), vmx=float(), vMin=float(), vmn=float(), xResolution=int(), xr=int(),
               yResolution=int(), yr=int(), *args, **kwargs):
    pass


def vectorize(browserView=bool(), bv=bool(), byFrame=float(), bf=float(), camera=str(), c=str(),
              combineFillsEdges=bool(), cfe=bool(), currentFrame=bool(), cf=bool(), curveTolerance=float(), ct=float(),
              customExtension=str(), ce=str(), detailLevel=int(), dl=int(), edgeColor=list, ec=list, edgeDetail=bool(),
              ed=bool(), edgeStyle=str(), es=str(), edgeWeight=float(), ew=float(), endFrame=float(), ef=float(),
              filenameFormat=str(), ff=str(), fillStyle=str(), fs=str(), flashVersion=int(), fv=int(), frameRate=int(),
              fr=int(), height=int(), h=int(), hiddenEdges=bool(), he=bool(), highlightLevel=int(), hl=int(),
              highlights=bool(), hi=bool(), imageFormat=str(), layer=str(), l=str(), minEdgeAngle=float(), mea=float(),
              outlinesAtIntersections=bool(), oai=bool(), outputFileName=str(), of=str(), pixelAspectRatio=float(),
              par=float(), reflectionDepth=int(), rd=int(), reflections=bool(), rf=bool(), renderLayers=bool(),
              rl=bool(), renderOptimization=str(), ro=str(), renderView=bool(), rv=bool(), secondaryCurveFitting=bool(),
              scf=bool(), shadows=bool(), sh=bool(), showBackFaces=bool(), sb=bool(), startFrame=float(), sf=float(),
              svgAnimation=str(), sa=str(), svgCompression=bool(), sc=bool(), width=int(), w=int(), *args, **kwargs):
    pass


def view2dToolCtx(alternateContext=bool(), ac=bool(), boxzoom=bool(), bz=bool(), dolly=bool(), do=bool(), exists=bool(),
                  ex=bool(), history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(),
                  i3=str(), name=str(), n=str(), toolName=str(), tn=str(), track=bool(), tr=bool(), *args, **kwargs):
    pass


def viewCamera(move=str(), m=str(), sideView=bool(), s=bool(), topView=bool(), t=bool(), *args, **kwargs):
    pass


def viewClipPlane(autoClipPlane=bool(), acp=bool(), farClipPlane=float(), fcp=float(), nearClipPlane=float(),
                  ncp=float(), surfacesOnly=bool(), so=bool(), *args, **kwargs):
    pass


def viewFit(allObjects=bool(), all=bool(), animate=bool(), an=bool(), center=bool(), c=bool(), fitFactor=float(),
            f=float(), namespace=str(), ns=str(), noChildren=bool(), noc=bool(), *args, **kwargs):
    pass


def viewHeadOn(*args, **kwargs):
    pass


def viewLookAt(position=list, pos=list, *args, **kwargs):
    pass


def viewManip(bottomLeft=bool(), bl=bool(), bottomRight=bool(), br=bool(), compassAngle=float(), ca=float(),
              dragSnap=bool(), ds=bool(), drawCompass=bool(), dc=bool(), fitToView=bool(), ftv=bool(),
              frontParameters=str(), fp=str(), goDefault=bool(), gd=bool(), goHome=bool(), gh=bool(),
              homeParameters=str(), hp=str(), levelCamera=bool(), lc=bool(), minOpacity=float(), mo=float(),
              namespace=str(), ns=str(), postCommand=str(), p=str(), preCommand=str(), pr=str(), preserveSceneUp=bool(),
              psu=bool(), resetFront=bool(), rf=bool(), resetHome=bool(), rh=bool(), restoreCenter=bool(), rc=bool(),
              selectionLockParameters=str(), slp=str(), setFront=bool(), sf=bool(), setHome=bool(), sh=bool(),
              size=str(), s=str(), toggleSelectionLock=bool(), tsl=bool(), topLeft=bool(), tl=bool(), topRight=bool(),
              tr=bool(), visible=bool(), v=bool(), zoomToFitScene=bool(), zf=bool(), *args, **kwargs):
    pass


def viewPlace(animate=bool(), an=bool(), eyePoint=list, eye=list, fieldOfView=float(), fov=float(), lookAt=list,
              la=list, ortho=bool(), o=bool(), perspective=bool(), p=bool(), upDirection=list, up=list,
              viewDirection=list, vd=list, *args, **kwargs):
    pass


def viewSet(animate=bool(), an=bool(), back=bool(), b=bool(), bottom=bool(), bo=bool(), fit=bool(), fitFactor=float(),
            ff=float(), front=bool(), f=bool(), home=bool(), h=bool(), keepRenderSettings=bool(), krs=bool(),
            leftSide=bool(), ls=bool(), namespace=str(), ns=str(), nextView=bool(), nv=bool(), persp=bool(), p=bool(),
            previousView=bool(), pv=bool(), rightSide=bool(), rs=bool(), side=bool(), s=bool(), top=bool(), t=bool(),
            viewNegativeX=bool(), vnx=bool(), viewNegativeY=bool(), vny=bool(), viewNegativeZ=bool(), vnz=bool(),
            viewX=bool(), vx=bool(), viewY=bool(), vy=bool(), viewZ=bool(), vz=bool(), *args, **kwargs):
    pass


def visor(addFolder=bool(), add=bool(), addNodes=str(), adn=str(), allowPanningInX=bool(), apx=bool(),
          allowPanningInY=bool(), apy=bool(), allowZooming=bool(), az=bool(), command=str(), cmd=str(),
          deleteFolder=str(), editFolder=str(), edf=str(), folderList=str(), fl=str(), menu=str(), mn=str(), name=str(),
          n=str(), nodeType=str(), ntp=str(), openDirectories=bool(), opd=bool(), openFolder=bool(), opf=bool(),
          parent=str(), p=str(), path=str(), pth=str(), popupMenuScript=str(), pms=str(), rebuild=bool(), re=bool(),
          refreshAllSwatches=bool(), ras=bool(), refreshSelectedSwatches=bool(), rss=bool(), refreshSwatch=str(),
          rs=str(), reset=bool(), rst=bool(), restrictPanAndZoom=bool(), rpz=bool(), saveSwatches=bool(), ss=bool(),
          scrollBar=str(), sb=str(), scrollPercent=float(), sp=float(), selectedGadgets=str(), sg=str(),
          showDividers=bool(), sd=bool(), showFiles=bool(), sfi=bool(), showFolders=bool(), sfo=bool(),
          showNodes=bool(), sn=bool(), stateString=bool(), sts=bool(), style=str(), stl=str(), transform=str(),
          trn=str(), type=str(), typ=str(), *args, **kwargs):
    pass


def volumeAxis(alongAxis=float(), alx=float(), aroundAxis=float(), arx=float(), attenuation=float(), att=float(),
               awayFromAxis=float(), afx=float(), awayFromCenter=float(), afc=float(), detailTurbulence=float(),
               dtr=float(), directionX=float(), dx=float(), directionY=float(), dy=float(), directionZ=float(),
               dz=float(), directionalSpeed=float(), drs=float(), invertAttenuation=bool(), ia=bool(),
               magnitude=float(), m=float(), maxDistance=float(), mxd=float(), name=str(), n=str(), perVertex=bool(),
               pv=bool(), position=list, pos=list, torusSectionRadius=float(), tsr=float(), turbulence=float(),
               trb=float(), turbulenceFrequencyX=float(), tfx=float(), turbulenceFrequencyY=float(), tfy=float(),
               turbulenceFrequencyZ=float(), tfz=float(), turbulenceOffsetX=float(), tox=float(),
               turbulenceOffsetY=float(), toy=float(), turbulenceOffsetZ=float(), toz=float(), turbulenceSpeed=float(),
               trs=float(), volumeExclusion=bool(), vex=bool(), volumeOffset=list, vof=list, volumeShape=str(),
               vsh=str(), volumeSweep=float(), vsw=float(), *args, **kwargs):
    pass


def volumeBind(influence=str(), inf=str(), name=str(), n=str(), *args, **kwargs):
    pass


def vortex(attenuation=float(), att=float(), axisX=float(), ax=float(), axisY=float(), ay=float(), axisZ=float(),
           az=float(), magnitude=float(), m=float(), maxDistance=float(), mxd=float(), name=str(), n=str(),
           perVertex=bool(), pv=bool(), position=list, pos=list, torusSectionRadius=float(), tsr=float(),
           volumeExclusion=bool(), vex=bool(), volumeOffset=list, vof=list, volumeShape=str(), vsh=str(),
           volumeSweep=float(), vsw=float(), *args, **kwargs):
    pass


def waitCursor(state=bool(), st=bool(), *args, **kwargs):
    pass


def walkCtx(alternateContext=bool(), ac=bool(), crouchCount=float(), wcc=float(), exists=bool(), ex=bool(),
            history=bool(), ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
            name=str(), n=str(), toolName=str(), tn=str(), walkHeight=float(), wh=float(), walkSensitivity=float(),
            wsv=float(), walkSpeed=float(), ws=float(), walkToolHud=bool(), wth=bool(), *args, **kwargs):
    pass


def warning(noContext=bool(), n=bool(), showLineNumber=bool(), sl=bool(), *args, **kwargs):
    pass


def webBrowser(annotation=str(), ann=str(), back=bool(), bk=bool(), backgroundColor=list, bgc=list,
               defineTemplate=str(), dt=str(), docTag=str(), dtg=str(), dragCallback=str(), dgc=str(),
               dropCallback=str(), dpc=str(), enable=bool(), en=bool(), enableBackground=bool(), ebg=bool(),
               enableKeyboardFocus=bool(), ekf=bool(), exists=bool(), ex=bool(), find=str(), f=str(), forward=bool(),
               fwd=bool(), fullPathName=bool(), fpn=bool(), height=int(), h=int(), highlightColor=list, hlc=list,
               home=bool(), hm=bool(), isObscured=bool(), io=bool(), manage=bool(), m=bool(), matchCase=bool(),
               mc=bool(), matchWholeWorld=bool(), mww=bool(), noBackground=bool(), nbg=bool(),
               numberOfPopupMenus=bool(), npm=bool(), openURL=str(), url=str(), parent=str(), p=str(),
               popupMenuArray=bool(), pma=bool(), preventOverride=bool(), po=bool(), reload=bool(), rl=bool(),
               searchForward=bool(), sf=bool(), statusBarMessage=str(), sbm=str(), stop=bool(), st=bool(),
               urlChangedCb=str(), ucc=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
               visibleChangeCommand=str(), vcc=str(), width=int(), w=int(), wrap=bool(), wr=bool(), *args, **kwargs):
    pass


def weightsColor(colorRamp=str(), cr=str(), deformer=str(), dfm=str(), falseColor=bool(), fc=bool(),
                 outOfRangeColor=list, orc=list, rampMaxColor=list, rxc=list, rampMinColor=list, rmc=list,
                 useColorRamp=bool(), ucr=bool(), useMaxMinColor=bool(), umc=bool(), *args, **kwargs):
    pass


def whatsNewHighlight(highlightColor=list, hc=list, highlightOn=bool(), ho=bool(), showStartupDialog=bool(), ssd=bool(),
                      *args, **kwargs):
    pass


def window(backgroundColor=list, bgc=list, closeCommand=str(), cc=str(), defineTemplate=str(), dt=str(), docTag=str(),
           dtg=str(), dockCorner=list, dc=list, dockStation=bool(), ds=bool(), dockingLayout=str(), dl=str(),
           exists=bool(), ex=bool(), frontWindow=bool(), fw=bool(), height=int(), h=int(), iconName=str(),
           iconify=bool(), i=bool(), interactivePlacement=bool(), ip=bool(), leftEdge=int(), le=int(),
           mainMenuBar=bool(), mm=bool(), mainWindow=bool(), mw=bool(), maximizeButton=bool(), mxb=bool(),
           menuArray=bool(), ma=bool(), menuBar=bool(), mb=bool(), menuBarCornerWidget=list, mcw=list,
           menuBarResize=bool(), mbr=bool(), menuBarVisible=bool(), mbv=bool(), menuIndex=list, mi=list,
           minimizeButton=bool(), mnb=bool(), minimizeCommand=str(), mnc=str(), nestedDockingEnabled=bool(), nde=bool(),
           numberOfMenus=bool(), nm=bool(), parent=str(), p=str(), resizeToFitChildren=bool(), rtf=bool(),
           restoreCommand=str(), rc=str(), retain=bool(), ret=bool(), sizeable=bool(), s=bool(), state=str(), st=str(),
           title=str(), t=str(), titleBar=bool(), tb=bool(), titleBarMenu=bool(), tbm=bool(), toolbox=bool(),
           tlb=bool(), topEdge=int(), te=int(), topLeftCorner=list, tlc=list, useTemplate=str(), ut=str(),
           visible=bool(), vis=bool(), width=int(), w=int(), widthHeight=list, wh=list, *args, **kwargs):
    pass


def windowPref(enableAll=bool(), ea=bool(), exists=bool(), ex=bool(), height=int(), h=int(), leftEdge=int(), le=int(),
               loadAll=bool(), la=bool(), maximized=bool(), max=bool(), parentMain=bool(), pm=bool(), remove=bool(),
               r=bool(), removeAll=bool(), ra=bool(), restoreMainWindowState=str(), rms=str(), saveAll=bool(),
               sa=bool(), saveMainWindowState=str(), sms=str(), topEdge=int(), te=int(), topLeftCorner=list, tlc=list,
               width=int(), w=int(), widthHeight=list, wh=list, *args, **kwargs):
    pass


def wire(after=bool(), af=bool(), afterReference=bool(), ar=bool(), before=bool(), bf=bool(), crossingEffect=float(),
         ce=float(), deformerTools=bool(), dt=bool(), dropoffDistance=list, dds=list, envelope=float(), en=float(),
         exclusive=str(), ex=str(), frontOfChain=bool(), foc=bool(), geometry=str(), g=str(), geometryIndices=bool(),
         gi=bool(), groupWithBase=bool(), gw=bool(), holder=list, ho=list, ignoreSelected=bool(),
         includeHiddenSelections=bool(), ihs=bool(), localInfluence=float(), li=float(), name=str(), n=str(),
         parallel=bool(), par=bool(), prune=bool(), pr=bool(), remove=bool(), rm=bool(), split=bool(), sp=bool(),
         useComponentTags=bool(), uct=bool(), wire=str(), w=str(), wireCount=int(), wc=int(), *args, **kwargs):
    pass


def wireContext(crossingEffect=float(), ce=float(), deformationOrder=str(), do=str(), dropoffDistance=float(),
                dds=float(), envelope=float(), en=float(), exclusive=bool(), exc=bool(), exclusivePartition=str(),
                ep=str(), exists=bool(), ex=bool(), groupWithBase=bool(), gw=bool(), history=bool(), ch=bool(),
                holder=bool(), ho=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(),
                localInfluence=float(), li=float(), name=str(), n=str(), *args, **kwargs):
    pass


def workspace(active=bool(), act=bool(), baseWorkspace=str(), bw=str(), create=str(), cr=str(), directory=str(),
              dir=str(), expandName=str(), en=str(), fileRule=list, fr=list, fileRuleEntry=str(), fre=str(),
              fileRuleList=bool(), frl=bool(), filter=bool(), f=bool(), fullName=bool(), fn=bool(), list=bool(),
              l=bool(), listFullWorkspaces=bool(), lfw=bool(), listWorkspaces=bool(), lw=bool(), newWorkspace=bool(),
              n=bool(), objectType=list, ot=list, objectTypeEntry=str(), ote=str(), objectTypeList=bool(), otl=bool(),
              openWorkspace=bool(), o=bool(), projectPath=str(), pp=str(), removeFileRuleEntry=str(), rfr=str(),
              removeVariableEntry=str(), rve=str(), renderType=list, rt=list, renderTypeEntry=str(), rte=str(),
              renderTypeList=bool(), rtl=bool(), rootDirectory=bool(), rd=bool(), saveWorkspace=bool(), s=bool(),
              shortName=bool(), sn=bool(), update=bool(), u=bool(), updateAll=bool(), ua=bool(), variable=list, v=list,
              variableEntry=str(), ve=str(), variableList=bool(), vl=bool(), *args, **kwargs):
    pass


def workspaceControl(checksPlugins=bool(), cp=bool(), close=bool(), cl=bool(), closeCommand=str(), cc=str(),
                     collapse=bool(), clp=bool(), defineTemplate=str(), dt=str(), dockToControl=list, dtc=list,
                     dockToMainWindow=list, dtm=list, dockToPanel=list, dtp=list, duplicatable=bool(), dup=bool(),
                     exists=bool(), ex=bool(), floating=bool(), fl=bool(), height=bool(), h=bool(),
                     heightProperty=str(), hp=str(), horizontal=bool(), hr=bool(), initCallback=str(), ic=str(),
                     initialHeight=int(), ih=int(), initialWidth=int(), iw=int(), label=str(), l=str(),
                     loadImmediately=bool(), li=bool(), minimumHeight=int(), mh=int(), minimumWidth=int(), mw=int(),
                     r=bool(), requiredControl=str(), rc=str(), requiredPlugin=str(), rp=str(), resizeHeight=int(),
                     rsh=int(), resizeWidth=int(), rsw=int(), restore=bool(), rs=bool(), retain=bool(), rt=bool(),
                     stateString=str(), ss=str(), tabPosition=list, tp=list, tabToControl=list, ttc=list,
                     uiScript=str(), ui=str(), useTemplate=str(), ut=str(), visible=bool(), vis=bool(),
                     visibleChangeCommand=str(), vcc=str(), width=bool(), w=bool(), widthProperty=str(), wp=str(),
                     *args, **kwargs):
    pass


def workspaceControlState(defaultTopLeftCorner=list, dc=list, defaultWidthHeight=list, dwh=list, exists=bool(),
                          ex=bool(), height=int(), h=int(), leftEdge=int(), le=int(), maximized=bool(), max=bool(),
                          remove=bool(), r=bool(), topEdge=int(), te=int(), topLeftCorner=list, tlc=list, width=int(),
                          w=int(), widthHeight=list, wh=list, *args, **kwargs):
    pass


def workspaceLayoutManager(collapseMainWindowControls=list, cmw=list, current=bool(), cu=bool(), delete=str(), d=str(),
                           i=str(), listLayouts=bool(), ll=bool(), listModuleLayouts=bool(), lml=bool(),
                           listUserLayouts=bool(), lul=bool(), modified=str(), m=str(), parentWorkspaceControl=str(),
                           pwc=str(), reset=bool(), rs=bool(), restoreMainWindowControls=bool(), rmw=bool(),
                           save=bool(), s=bool(), saveAs=str(), sa=str(), setCurrent=str(), sc=str(),
                           setCurrentCallback=str(), scc=str(), setModifiedCallback=str(), smc=str(), type=str(),
                           t=str(), *args, **kwargs):
    pass


def workspacePanel(defineTemplate=str(), dt=str(), exists=bool(), ex=bool(), mainWindow=bool(), mw=bool(),
                   useTemplate=str(), ut=str(), *args, **kwargs):
    pass


def wrinkle(axis=list, ax=list, branchCount=int(), brc=int(), branchDepth=int(), bd=int(), center=list, ct=list,
            crease=str(), cr=str(), dropoffDistance=float(), dds=float(), envelope=float(), en=float(),
            randomness=float(), rnd=float(), style=str(), st=str(), thickness=float(), th=float(), uvSpace=list,
            uv=list, wrinkleCount=int(), wc=int(), wrinkleIntensity=float(), wi=float(), *args, **kwargs):
    pass


def wrinkleContext(branchCount=int(), brc=int(), branchDepth=int(), bd=int(), exists=bool(), ex=bool(), history=bool(),
                   ch=bool(), image1=str(), i1=str(), image2=str(), i2=str(), image3=str(), i3=str(), name=str(),
                   n=str(), randomness=float(), rnd=float(), style=str(), st=str(), thickness=float(), th=float(),
                   wrinkleCount=int(), wc=int(), wrinkleIntensity=float(), wi=float(), *args, **kwargs):
    pass


def writeTake(angle=str(), a=str(), device=str(), d=str(), linear=str(), l=str(), noTime=bool(), nt=bool(),
              precision=int(), pre=int(), take=str(), t=str(), virtualDevice=str(), vd=str(), *args, **kwargs):
    pass


def xform(absolute=bool(), a=bool(), boundingBox=bool(), bb=bool(), boundingBoxInvisible=bool(), bbi=bool(),
          centerPivots=bool(), cp=bool(), centerPivotsOnComponents=bool(), cpc=bool(), deletePriorHistory=bool(),
          dph=bool(), euler=bool(), eu=bool(), matrix=list, m=list, objectSpace=bool(), os=bool(), pivots=list,
          piv=list, preserve=bool(), p=bool(), preserveUV=bool(), puv=bool(), reflection=bool(), rfl=bool(),
          reflectionAboutBBox=bool(), rab=bool(), reflectionAboutOrigin=bool(), rao=bool(), reflectionAboutX=bool(),
          rax=bool(), reflectionAboutY=bool(), ray=bool(), reflectionAboutZ=bool(), raz=bool(),
          reflectionTolerance=float(), rft=float(), relative=bool(), r=bool(), rotateAxis=list, ra=list,
          rotateOrder=str(), roo=str(), rotatePivot=list, rp=list, rotateTranslation=list, rt=list, rotation=list,
          ro=list, scale=list, s=list, scalePivot=list, sp=list, scaleTranslation=list, st=list, shear=list, sh=list,
          translation=list, t=list, worldSpace=bool(), ws=bool(), worldSpaceDistance=bool(), wd=bool(),
          zeroTransformPivots=bool(), ztp=bool(), *args, **kwargs):
    pass


def xformConstraint(alongNormal=int(), n=int(), live=bool(), l=bool(), type=str(), t=str(), *args, **kwargs):
    pass


def xpmPicker(fileName=str(), fn=str(), parent=str(), p=str(), *args, **kwargs):
    pass