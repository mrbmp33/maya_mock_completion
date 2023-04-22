if False:
    from typing import Dict, List, Tuple, Union, Optional


class _Object(object):
    __dict__ = None


class QTest(_Object):
    @staticmethod
    def addColumnInternal(*args, **kwargs): pass

    @staticmethod
    def asciiToKey(*args, **kwargs): pass

    @staticmethod
    def compare_ptr_helper(*args, **kwargs): pass

    @staticmethod
    def compare_string_helper(*args, **kwargs): pass

    @staticmethod
    def currentAppName(*args, **kwargs): pass

    @staticmethod
    def currentDataTag(*args, **kwargs): pass

    @staticmethod
    def currentTestFailed(*args, **kwargs): pass

    @staticmethod
    def currentTestFunction(*args, **kwargs): pass

    @staticmethod
    def ignoreMessage(*args, **kwargs): pass

    @staticmethod
    def keyClick(*args, **kwargs): pass

    @staticmethod
    def keyClicks(*args, **kwargs): pass

    @staticmethod
    def keyEvent(*args, **kwargs): pass

    @staticmethod
    def keyPress(*args, **kwargs): pass

    @staticmethod
    def keyRelease(*args, **kwargs): pass

    @staticmethod
    def keyToAscii(*args, **kwargs): pass

    @staticmethod
    def mouseClick(*args, **kwargs): pass

    @staticmethod
    def mouseDClick(*args, **kwargs): pass

    @staticmethod
    def mouseEvent(*args, **kwargs): pass

    @staticmethod
    def mouseMove(*args, **kwargs): pass

    @staticmethod
    def mousePress(*args, **kwargs): pass

    @staticmethod
    def mouseRelease(*args, **kwargs): pass

    @staticmethod
    def qElementData(*args, **kwargs): pass

    @staticmethod
    def qExpectFail(*args, **kwargs): pass

    @staticmethod
    def qFindTestData(*args, **kwargs): pass

    @staticmethod
    def qGlobalData(*args, **kwargs): pass

    @staticmethod
    def qSkip(*args, **kwargs): pass

    @staticmethod
    def qWaitForWindowActive(*args, **kwargs): pass

    @staticmethod
    def qWaitForWindowExposed(*args, **kwargs): pass

    @staticmethod
    def sendKeyEvent(*args, **kwargs): pass

    @staticmethod
    def setBenchmarkResult(*args, **kwargs): pass

    @staticmethod
    def setMainSourcePath(*args, **kwargs): pass

    @staticmethod
    def simulateEvent(*args, **kwargs): pass

    @staticmethod
    def testObject(*args, **kwargs): pass

    @staticmethod
    def toPrettyCString(*args, **kwargs): pass

    @staticmethod
    def touchEvent(*args, **kwargs): pass

    @staticmethod
    def waitForEvents(*args, **kwargs): pass

    Abort = None

    AlignmentFaults = None

    BitsPerSecond = None

    BranchInstructions = None

    BranchMisses = None

    BusCycles = None

    BytesAllocated = None

    BytesPerSecond = None

    CPUCycles = None

    CPUMigrations = None

    CPUTicks = None

    CacheMisses = None

    CachePrefetchMisses = None

    CachePrefetches = None

    CacheReadMisses = None

    CacheReads = None

    CacheReferences = None

    CacheWriteMisses = None

    CacheWrites = None

    Click = None

    ContextSwitches = None

    Continue = None

    EmulationFaults = None

    Events = None

    FramesPerSecond = None

    InstructionReads = None

    Instructions = None

    KeyAction = None

    MajorPageFaults = None

    MinorPageFaults = None

    MouseAction = None

    MouseClick = None

    MouseDClick = None

    MouseMove = None

    MousePress = None

    MouseRelease = None

    PageFaults = None

    Press = None

    QBenchmarkMetric = None

    QTouchEventSequence = None

    Release = None

    Shortcut = None

    StalledCycles = None

    TestFailMode = None

    WalltimeMilliseconds = None

    WalltimeNanoseconds = None
