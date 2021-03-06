import libdtoolconfig, libpandaphysics
from GeomBindType import *
from NotifySeverity import *
from ErrorUtilCode import *
from CoordinateSystem import *
from libpandaphysicsDowncasts import *
import AccumulatedAttribs, AngularIntegrator, AnimControlCollection, AsyncUtility, BamFile, BaseParticle, BitMask32, BoundedObject, Buffer, ButtonEvent, ButtonHandle, ButtonRegistry, CString, ChanCfgOverrides, ChanConfig, ClearableRegion, ClockObject, CollisionTraverser, ComputedVertices, ConfigExpress, ConnectionManager, ConnectionReader, ConnectionWriter, CullBinManager, CullableObject, CurveFitter, DSearchPath, DataGraphTraverser, DataNodeTransmit, DatagramIterator, Decompressor, DocumentSpec, DownloadDb, EventParameter, EventQueue, EventReceiver, Extractor, FILE, Filename, FontPool, FrameBufferProperties, Frustum, FrustumD, Fstream, GeomTransformer, GraphicsEngine, GraphicsPipeSelection, GraphicsThreadingModel, HTTPClient, HTTPDate, HTTPEntityTag, HTTPEnum, HashVal, Ifstream, Istream, KeyboardButton, LOD, LinearIntegrator, LoaderFileType, Mat3, Mat3D, Mat4, Mat4D, MaterialPool, MathNumbers, ModelPool, ModifierButtons, MouseButton, MouseData, MouseWatcherParameter, Multifile, Namable, NetAddress, NodePath, NodePathCollection, Notify, NotifyCategory, NurbsCurveInterface, Ofstream, Ostream, PGFrameStyle, PRFileDesc, PRNetAddr, PStatClient, PStatCollector, PTAUshort, ParticleSystemManager, Patcher, Patchfile, PhysicsManager, Pipeline, Plane, PlaneD, PointerToBaseConnection, PointerToBaseRefCountObjvectorLPoint2f, PointerToBaseRefCountObjvectorLPoint3f, PointerToBaseRefCountObjvectorLVecBase4f, PointerToBaseRefCountObjvectorLVector3f, PointerToBaseRefCountObjvectorunsignedchar, ProfileTimer, QueuedReturnConnectionListenerData, QueuedReturnNetDatagram, QueuedReturnPointerToConnection, Ramfile, ReferenceCount, SceneGraphReducer, StreamReader, StreamWriter, TextEncoder, TextureCollection, TexturePool, TimeVal, TypeHandle, TypeRegistry, TypedObject, URLSpec, UniqueIdAllocator, VBase2, VBase2D, VBase3, VBase3D, VBase4, VBase4D, VectorURLSpec, VectorbasicStringchar, VirtualFileSystem, WindowProperties, WindowsRegistry, AngularEulerIntegrator, AnimControl, AudioManager, AudioSound, BaseParticleEmitter, BaseParticleFactory, BaseParticleRenderer, CardMaker, Connection, ConnectionListener, Datagram, DisplayRegion, EventHandler, ISocketStream, Iostream, Light, LineSegs, LineStream, LinearEulerIntegrator, MouseWatcherGroup, MultiplexStream, NurbsCurveEvaluator, NurbsCurveResult, OSocketStream, PTAColorf, PTANormalf, PTATexCoordf, PTAUchar, PTAVertexf, PandaLoader, ParametricCurveCollection, ParametricCurveDrawer, Point2, Point2D, Point3, Point3D, Point4, Point4D, PointerToConnection, Quat, QuatD, QueuedConnectionManager, QueuedConnectionReader, RecentConnectionReader, TypedReferenceCount, TypedWritable, Vec2, Vec2D, Vec3, Vec3D, Vec4, Vec4D, VirtualFileList, AutonomousLerp, BaseForce, BoundingVolume, BoxEmitter, ClientBase, CollisionEntry, CollisionHandler, DiscEmitter, Event, GeomParticleRenderer, GraphicsChannel, GraphicsLayer, GraphicsPipe, GraphicsStateGuardianBase, GraphicsWindow, LOrientationd, LOrientationf, LRotationd, LRotationf, Lens, Lerp, LerpBlendType, LerpFunctor, LineEmitter, LineParticleRenderer, MouseWatcherRegion, NetDatagram, NurbsCurveDrawer, PGMouseWatcherParameter, PandaNode, Physical, PhysicsObject, PointEmitter, PointParticleFactory, PointParticleRenderer, QueuedConnectionListener, RectangleEmitter, RingEmitter, SocketStream, SparkleParticleRenderer, SphereSurfaceEmitter, SphereVolumeEmitter, SpriteParticleRenderer, TangentRingEmitter, TextFont, TypedWritableReferenceCount, VirtualFile, WritableConfigurable, ZSpinParticleFactory, AngularForce, AnimBundleNode, AnimGroup, CollisionHandlerEvent, CollisionHandlerQueue, CollisionNode, CollisionSolid, DDrawable, DataNode, DynamicTextFont, EaseInBlendType, EaseInOutBlendType, EaseOutBlendType, FloatLerpFunctor, Fog, ForceNode, GeomNode, GeometricBoundingVolume, GraphicsStateGuardian, HTTPChannel, HprScaleLerpFunctor, ImageBuffer, IntLerpFunctor, LensNode, LightNode, LinearForce, Material, MatrixLens, ModelNode, MultiLerpFunctor, NoBlendType, OrthographicLens, PGItem, PGMouseWatcherBackground, PGTop, ParametricCurve, PartBundleNode, PartGroup, ParticleSystem, PerspectiveLens, PhysicalNode, PlaneNode, PosHprLerpFunctor, PosHprScaleLerpFunctor, RenderAttrib, RenderEffect, RenderEffects, RenderState, RopeNode, SelectiveChildNode, SimpleLerpFunctorLPoint2f, SimpleLerpFunctorLPoint3f, SimpleLerpFunctorLPoint4f, SimpleLerpFunctorLVecBase2f, SimpleLerpFunctorLVecBase3f, SimpleLerpFunctorLVecBase4f, SimpleLerpFunctorLVector2f, SimpleLerpFunctorLVector3f, SimpleLerpFunctorLVector4f, StaticTextFont, TextNode, TransformState, VirtualFileComposite, VirtualFileSimple, AlphaTestAttrib, AmbientLight, AnalogNode, AngularVectorForce, AnimBundle, BillboardEffect, BoundingLine, ButtonNode, ButtonThrower, Camera, Character, ClipPlaneAttrib, CollisionHandlerPhysical, CollisionPlane, CollisionRay, CollisionSegment, CollisionSphere, ColorAttrib, ColorBlendAttrib, ColorLerpFunctor, ColorScaleAttrib, ColorScaleLerpFunctor, ColorWriteAttrib, CompassEffect, CubicCurveseg, CullBinAttrib, CullFaceAttrib, DecalEffect, DepthOffsetAttrib, DepthTestAttrib, DepthWriteAttrib, DialNode, DirectionalLight, DriveInterface, FiniteBoundingVolume, FloatQueryLerpFunctor, FogAttrib, Geom, HprLerpFunctor, IntQueryLerpFunctor, LODNode, LightAttrib, LightLensNode, LinearCylinderVortexForce, LinearDistanceForce, LinearFrictionForce, LinearRandomForce, LinearUserDefinedForce, LinearVectorForce, MaterialAttrib, ModelRoot, MouseAndKeyboard, MouseWatcher, MovingPartBase, OmniBoundingVolume, PGButton, PGEntry, PGWaitBar, PartBundle, PiecewiseCurve, PointLight, PosLerpFunctor, RenderModeAttrib, ScaleLerpFunctor, SequenceNode, ShowBoundsEffect, SimpleQueryLerpFunctorLPoint2f, SimpleQueryLerpFunctorLPoint3f, SimpleQueryLerpFunctorLPoint4f, SimpleQueryLerpFunctorLVecBase2f, SimpleQueryLerpFunctorLVecBase3f, SimpleQueryLerpFunctorLVecBase4f, SimpleQueryLerpFunctorLVector2f, SimpleQueryLerpFunctorLVector3f, SimpleQueryLerpFunctorLVector4f, SwitchNode, TexMatrixAttrib, Texture, TextureApplyAttrib, TextureAttrib, Trackball, TrackerNode, Transform2SG, TransparencyAttrib, VirtualMouse, BoundingSphere, CharacterJointBundle, CollisionHandlerFloor, CollisionHandlerPusher, CollisionPolygon, DynamicTextPage, GeomLine, GeomLinestrip, GeomPoint, GeomPolygon, GeomQuad, GeomSphere, GeomSprite, GeomTri, GeomTrifan, GeomTristrip, HermiteCurve, LinearJitterForce, LinearNoiseForce, LinearSinkForce, LinearSourceForce, MovingPartACMatrixSwitchType, NurbsCurve, Spotlight, GeomTextGlyph, MovingPartMatrix, CharacterJoint
from libpandaphysicsGlobals import *
AccumulatedAttribs = AccumulatedAttribs.AccumulatedAttribs
AngularIntegrator = AngularIntegrator.AngularIntegrator
AnimControlCollection = AnimControlCollection.AnimControlCollection
AsyncUtility = AsyncUtility.AsyncUtility
BamFile = BamFile.BamFile
BaseParticle = BaseParticle.BaseParticle
BitMask32 = BitMask32.BitMask32
BoundedObject = BoundedObject.BoundedObject
Buffer = Buffer.Buffer
ButtonEvent = ButtonEvent.ButtonEvent
ButtonHandle = ButtonHandle.ButtonHandle
ButtonRegistry = ButtonRegistry.ButtonRegistry
CString = CString.CString
ChanCfgOverrides = ChanCfgOverrides.ChanCfgOverrides
ChanConfig = ChanConfig.ChanConfig
ClearableRegion = ClearableRegion.ClearableRegion
ClockObject = ClockObject.ClockObject
CollisionTraverser = CollisionTraverser.CollisionTraverser
ComputedVertices = ComputedVertices.ComputedVertices
ConfigExpress = ConfigExpress.ConfigExpress
ConnectionManager = ConnectionManager.ConnectionManager
ConnectionReader = ConnectionReader.ConnectionReader
ConnectionWriter = ConnectionWriter.ConnectionWriter
CullBinManager = CullBinManager.CullBinManager
CullableObject = CullableObject.CullableObject
CurveFitter = CurveFitter.CurveFitter
DSearchPath = DSearchPath.DSearchPath
DataGraphTraverser = DataGraphTraverser.DataGraphTraverser
DataNodeTransmit = DataNodeTransmit.DataNodeTransmit
DatagramIterator = DatagramIterator.DatagramIterator
Decompressor = Decompressor.Decompressor
DocumentSpec = DocumentSpec.DocumentSpec
DownloadDb = DownloadDb.DownloadDb
EventParameter = EventParameter.EventParameter
EventQueue = EventQueue.EventQueue
EventReceiver = EventReceiver.EventReceiver
Extractor = Extractor.Extractor
FILE = FILE.FILE
Filename = Filename.Filename
FontPool = FontPool.FontPool
FrameBufferProperties = FrameBufferProperties.FrameBufferProperties
Frustum = Frustum.Frustum
FrustumD = FrustumD.FrustumD
Fstream = Fstream.Fstream
GeomTransformer = GeomTransformer.GeomTransformer
GraphicsEngine = GraphicsEngine.GraphicsEngine
GraphicsPipeSelection = GraphicsPipeSelection.GraphicsPipeSelection
GraphicsThreadingModel = GraphicsThreadingModel.GraphicsThreadingModel
HTTPClient = HTTPClient.HTTPClient
HTTPDate = HTTPDate.HTTPDate
HTTPEntityTag = HTTPEntityTag.HTTPEntityTag
HTTPEnum = HTTPEnum.HTTPEnum
HashVal = HashVal.HashVal
Ifstream = Ifstream.Ifstream
Istream = Istream.Istream
KeyboardButton = KeyboardButton.KeyboardButton
LOD = LOD.LOD
LinearIntegrator = LinearIntegrator.LinearIntegrator
LoaderFileType = LoaderFileType.LoaderFileType
Mat3 = Mat3.Mat3
Mat3D = Mat3D.Mat3D
Mat4 = Mat4.Mat4
Mat4D = Mat4D.Mat4D
MaterialPool = MaterialPool.MaterialPool
MathNumbers = MathNumbers.MathNumbers
ModelPool = ModelPool.ModelPool
ModifierButtons = ModifierButtons.ModifierButtons
MouseButton = MouseButton.MouseButton
MouseData = MouseData.MouseData
MouseWatcherParameter = MouseWatcherParameter.MouseWatcherParameter
Multifile = Multifile.Multifile
Namable = Namable.Namable
NetAddress = NetAddress.NetAddress
NodePath = NodePath.NodePath
NodePathCollection = NodePathCollection.NodePathCollection
Notify = Notify.Notify
NotifyCategory = NotifyCategory.NotifyCategory
NurbsCurveInterface = NurbsCurveInterface.NurbsCurveInterface
Ofstream = Ofstream.Ofstream
Ostream = Ostream.Ostream
PGFrameStyle = PGFrameStyle.PGFrameStyle
PRFileDesc = PRFileDesc.PRFileDesc
PRNetAddr = PRNetAddr.PRNetAddr
PStatClient = PStatClient.PStatClient
PStatCollector = PStatCollector.PStatCollector
PTAUshort = PTAUshort.PTAUshort
ParticleSystemManager = ParticleSystemManager.ParticleSystemManager
Patcher = Patcher.Patcher
Patchfile = Patchfile.Patchfile
PhysicsManager = PhysicsManager.PhysicsManager
Pipeline = Pipeline.Pipeline
Plane = Plane.Plane
PlaneD = PlaneD.PlaneD
PointerToBaseConnection = PointerToBaseConnection.PointerToBaseConnection
PointerToBaseRefCountObjvectorLPoint2f = PointerToBaseRefCountObjvectorLPoint2f.PointerToBaseRefCountObjvectorLPoint2f
PointerToBaseRefCountObjvectorLPoint3f = PointerToBaseRefCountObjvectorLPoint3f.PointerToBaseRefCountObjvectorLPoint3f
PointerToBaseRefCountObjvectorLVecBase4f = PointerToBaseRefCountObjvectorLVecBase4f.PointerToBaseRefCountObjvectorLVecBase4f
PointerToBaseRefCountObjvectorLVector3f = PointerToBaseRefCountObjvectorLVector3f.PointerToBaseRefCountObjvectorLVector3f
PointerToBaseRefCountObjvectorunsignedchar = PointerToBaseRefCountObjvectorunsignedchar.PointerToBaseRefCountObjvectorunsignedchar
ProfileTimer = ProfileTimer.ProfileTimer
QueuedReturnConnectionListenerData = QueuedReturnConnectionListenerData.QueuedReturnConnectionListenerData
QueuedReturnNetDatagram = QueuedReturnNetDatagram.QueuedReturnNetDatagram
QueuedReturnPointerToConnection = QueuedReturnPointerToConnection.QueuedReturnPointerToConnection
Ramfile = Ramfile.Ramfile
ReferenceCount = ReferenceCount.ReferenceCount
SceneGraphReducer = SceneGraphReducer.SceneGraphReducer
StreamReader = StreamReader.StreamReader
StreamWriter = StreamWriter.StreamWriter
TextEncoder = TextEncoder.TextEncoder
TextureCollection = TextureCollection.TextureCollection
TexturePool = TexturePool.TexturePool
TimeVal = TimeVal.TimeVal
TypeHandle = TypeHandle.TypeHandle
TypeRegistry = TypeRegistry.TypeRegistry
TypedObject = TypedObject.TypedObject
URLSpec = URLSpec.URLSpec
UniqueIdAllocator = UniqueIdAllocator.UniqueIdAllocator
VBase2 = VBase2.VBase2
VBase2D = VBase2D.VBase2D
VBase3 = VBase3.VBase3
VBase3D = VBase3D.VBase3D
VBase4 = VBase4.VBase4
VBase4D = VBase4D.VBase4D
VectorURLSpec = VectorURLSpec.VectorURLSpec
VectorbasicStringchar = VectorbasicStringchar.VectorbasicStringchar
VirtualFileSystem = VirtualFileSystem.VirtualFileSystem
WindowProperties = WindowProperties.WindowProperties
WindowsRegistry = WindowsRegistry.WindowsRegistry
AngularEulerIntegrator = AngularEulerIntegrator.AngularEulerIntegrator
AnimControl = AnimControl.AnimControl
AudioManager = AudioManager.AudioManager
AudioSound = AudioSound.AudioSound
BaseParticleEmitter = BaseParticleEmitter.BaseParticleEmitter
BaseParticleFactory = BaseParticleFactory.BaseParticleFactory
BaseParticleRenderer = BaseParticleRenderer.BaseParticleRenderer
CardMaker = CardMaker.CardMaker
Connection = Connection.Connection
ConnectionListener = ConnectionListener.ConnectionListener
Datagram = Datagram.Datagram
DisplayRegion = DisplayRegion.DisplayRegion
EventHandler = EventHandler.EventHandler
ISocketStream = ISocketStream.ISocketStream
Iostream = Iostream.Iostream
Light = Light.Light
LineSegs = LineSegs.LineSegs
LineStream = LineStream.LineStream
LinearEulerIntegrator = LinearEulerIntegrator.LinearEulerIntegrator
MouseWatcherGroup = MouseWatcherGroup.MouseWatcherGroup
MultiplexStream = MultiplexStream.MultiplexStream
NurbsCurveEvaluator = NurbsCurveEvaluator.NurbsCurveEvaluator
NurbsCurveResult = NurbsCurveResult.NurbsCurveResult
OSocketStream = OSocketStream.OSocketStream
PTAColorf = PTAColorf.PTAColorf
PTANormalf = PTANormalf.PTANormalf
PTATexCoordf = PTATexCoordf.PTATexCoordf
PTAUchar = PTAUchar.PTAUchar
PTAVertexf = PTAVertexf.PTAVertexf
PandaLoader = PandaLoader.PandaLoader
ParametricCurveCollection = ParametricCurveCollection.ParametricCurveCollection
ParametricCurveDrawer = ParametricCurveDrawer.ParametricCurveDrawer
Point2 = Point2.Point2
Point2D = Point2D.Point2D
Point3 = Point3.Point3
Point3D = Point3D.Point3D
Point4 = Point4.Point4
Point4D = Point4D.Point4D
PointerToConnection = PointerToConnection.PointerToConnection
Quat = Quat.Quat
QuatD = QuatD.QuatD
QueuedConnectionManager = QueuedConnectionManager.QueuedConnectionManager
QueuedConnectionReader = QueuedConnectionReader.QueuedConnectionReader
RecentConnectionReader = RecentConnectionReader.RecentConnectionReader
TypedReferenceCount = TypedReferenceCount.TypedReferenceCount
TypedWritable = TypedWritable.TypedWritable
Vec2 = Vec2.Vec2
Vec2D = Vec2D.Vec2D
Vec3 = Vec3.Vec3
Vec3D = Vec3D.Vec3D
Vec4 = Vec4.Vec4
Vec4D = Vec4D.Vec4D
VirtualFileList = VirtualFileList.VirtualFileList
AutonomousLerp = AutonomousLerp.AutonomousLerp
BaseForce = BaseForce.BaseForce
BoundingVolume = BoundingVolume.BoundingVolume
BoxEmitter = BoxEmitter.BoxEmitter
ClientBase = ClientBase.ClientBase
CollisionEntry = CollisionEntry.CollisionEntry
CollisionHandler = CollisionHandler.CollisionHandler
DiscEmitter = DiscEmitter.DiscEmitter
Event = Event.Event
GeomParticleRenderer = GeomParticleRenderer.GeomParticleRenderer
GraphicsChannel = GraphicsChannel.GraphicsChannel
GraphicsLayer = GraphicsLayer.GraphicsLayer
GraphicsPipe = GraphicsPipe.GraphicsPipe
GraphicsStateGuardianBase = GraphicsStateGuardianBase.GraphicsStateGuardianBase
GraphicsWindow = GraphicsWindow.GraphicsWindow
LOrientationd = LOrientationd.LOrientationd
LOrientationf = LOrientationf.LOrientationf
LRotationd = LRotationd.LRotationd
LRotationf = LRotationf.LRotationf
Lens = Lens.Lens
Lerp = Lerp.Lerp
LerpBlendType = LerpBlendType.LerpBlendType
LerpFunctor = LerpFunctor.LerpFunctor
LineEmitter = LineEmitter.LineEmitter
LineParticleRenderer = LineParticleRenderer.LineParticleRenderer
MouseWatcherRegion = MouseWatcherRegion.MouseWatcherRegion
NetDatagram = NetDatagram.NetDatagram
NurbsCurveDrawer = NurbsCurveDrawer.NurbsCurveDrawer
PGMouseWatcherParameter = PGMouseWatcherParameter.PGMouseWatcherParameter
PandaNode = PandaNode.PandaNode
Physical = Physical.Physical
PhysicsObject = PhysicsObject.PhysicsObject
PointEmitter = PointEmitter.PointEmitter
PointParticleFactory = PointParticleFactory.PointParticleFactory
PointParticleRenderer = PointParticleRenderer.PointParticleRenderer
QueuedConnectionListener = QueuedConnectionListener.QueuedConnectionListener
RectangleEmitter = RectangleEmitter.RectangleEmitter
RingEmitter = RingEmitter.RingEmitter
SocketStream = SocketStream.SocketStream
SparkleParticleRenderer = SparkleParticleRenderer.SparkleParticleRenderer
SphereSurfaceEmitter = SphereSurfaceEmitter.SphereSurfaceEmitter
SphereVolumeEmitter = SphereVolumeEmitter.SphereVolumeEmitter
SpriteParticleRenderer = SpriteParticleRenderer.SpriteParticleRenderer
TangentRingEmitter = TangentRingEmitter.TangentRingEmitter
TextFont = TextFont.TextFont
TypedWritableReferenceCount = TypedWritableReferenceCount.TypedWritableReferenceCount
VirtualFile = VirtualFile.VirtualFile
WritableConfigurable = WritableConfigurable.WritableConfigurable
ZSpinParticleFactory = ZSpinParticleFactory.ZSpinParticleFactory
AngularForce = AngularForce.AngularForce
AnimBundleNode = AnimBundleNode.AnimBundleNode
AnimGroup = AnimGroup.AnimGroup
CollisionHandlerEvent = CollisionHandlerEvent.CollisionHandlerEvent
CollisionHandlerQueue = CollisionHandlerQueue.CollisionHandlerQueue
CollisionNode = CollisionNode.CollisionNode
CollisionSolid = CollisionSolid.CollisionSolid
DDrawable = DDrawable.DDrawable
DataNode = DataNode.DataNode
DynamicTextFont = DynamicTextFont.DynamicTextFont
EaseInBlendType = EaseInBlendType.EaseInBlendType
EaseInOutBlendType = EaseInOutBlendType.EaseInOutBlendType
EaseOutBlendType = EaseOutBlendType.EaseOutBlendType
FloatLerpFunctor = FloatLerpFunctor.FloatLerpFunctor
Fog = Fog.Fog
ForceNode = ForceNode.ForceNode
GeomNode = GeomNode.GeomNode
GeometricBoundingVolume = GeometricBoundingVolume.GeometricBoundingVolume
GraphicsStateGuardian = GraphicsStateGuardian.GraphicsStateGuardian
HTTPChannel = HTTPChannel.HTTPChannel
HprScaleLerpFunctor = HprScaleLerpFunctor.HprScaleLerpFunctor
ImageBuffer = ImageBuffer.ImageBuffer
IntLerpFunctor = IntLerpFunctor.IntLerpFunctor
LensNode = LensNode.LensNode
LightNode = LightNode.LightNode
LinearForce = LinearForce.LinearForce
Material = Material.Material
MatrixLens = MatrixLens.MatrixLens
ModelNode = ModelNode.ModelNode
MultiLerpFunctor = MultiLerpFunctor.MultiLerpFunctor
NoBlendType = NoBlendType.NoBlendType
OrthographicLens = OrthographicLens.OrthographicLens
PGItem = PGItem.PGItem
PGMouseWatcherBackground = PGMouseWatcherBackground.PGMouseWatcherBackground
PGTop = PGTop.PGTop
ParametricCurve = ParametricCurve.ParametricCurve
PartBundleNode = PartBundleNode.PartBundleNode
PartGroup = PartGroup.PartGroup
ParticleSystem = ParticleSystem.ParticleSystem
PerspectiveLens = PerspectiveLens.PerspectiveLens
PhysicalNode = PhysicalNode.PhysicalNode
PlaneNode = PlaneNode.PlaneNode
PosHprLerpFunctor = PosHprLerpFunctor.PosHprLerpFunctor
PosHprScaleLerpFunctor = PosHprScaleLerpFunctor.PosHprScaleLerpFunctor
RenderAttrib = RenderAttrib.RenderAttrib
RenderEffect = RenderEffect.RenderEffect
RenderEffects = RenderEffects.RenderEffects
RenderState = RenderState.RenderState
RopeNode = RopeNode.RopeNode
SelectiveChildNode = SelectiveChildNode.SelectiveChildNode
SimpleLerpFunctorLPoint2f = SimpleLerpFunctorLPoint2f.SimpleLerpFunctorLPoint2f
SimpleLerpFunctorLPoint3f = SimpleLerpFunctorLPoint3f.SimpleLerpFunctorLPoint3f
SimpleLerpFunctorLPoint4f = SimpleLerpFunctorLPoint4f.SimpleLerpFunctorLPoint4f
SimpleLerpFunctorLVecBase2f = SimpleLerpFunctorLVecBase2f.SimpleLerpFunctorLVecBase2f
SimpleLerpFunctorLVecBase3f = SimpleLerpFunctorLVecBase3f.SimpleLerpFunctorLVecBase3f
SimpleLerpFunctorLVecBase4f = SimpleLerpFunctorLVecBase4f.SimpleLerpFunctorLVecBase4f
SimpleLerpFunctorLVector2f = SimpleLerpFunctorLVector2f.SimpleLerpFunctorLVector2f
SimpleLerpFunctorLVector3f = SimpleLerpFunctorLVector3f.SimpleLerpFunctorLVector3f
SimpleLerpFunctorLVector4f = SimpleLerpFunctorLVector4f.SimpleLerpFunctorLVector4f
StaticTextFont = StaticTextFont.StaticTextFont
TextNode = TextNode.TextNode
TransformState = TransformState.TransformState
VirtualFileComposite = VirtualFileComposite.VirtualFileComposite
VirtualFileSimple = VirtualFileSimple.VirtualFileSimple
AlphaTestAttrib = AlphaTestAttrib.AlphaTestAttrib
AmbientLight = AmbientLight.AmbientLight
AnalogNode = AnalogNode.AnalogNode
AngularVectorForce = AngularVectorForce.AngularVectorForce
AnimBundle = AnimBundle.AnimBundle
BillboardEffect = BillboardEffect.BillboardEffect
BoundingLine = BoundingLine.BoundingLine
ButtonNode = ButtonNode.ButtonNode
ButtonThrower = ButtonThrower.ButtonThrower
Camera = Camera.Camera
Character = Character.Character
ClipPlaneAttrib = ClipPlaneAttrib.ClipPlaneAttrib
CollisionHandlerPhysical = CollisionHandlerPhysical.CollisionHandlerPhysical
CollisionPlane = CollisionPlane.CollisionPlane
CollisionRay = CollisionRay.CollisionRay
CollisionSegment = CollisionSegment.CollisionSegment
CollisionSphere = CollisionSphere.CollisionSphere
ColorAttrib = ColorAttrib.ColorAttrib
ColorBlendAttrib = ColorBlendAttrib.ColorBlendAttrib
ColorLerpFunctor = ColorLerpFunctor.ColorLerpFunctor
ColorScaleAttrib = ColorScaleAttrib.ColorScaleAttrib
ColorScaleLerpFunctor = ColorScaleLerpFunctor.ColorScaleLerpFunctor
ColorWriteAttrib = ColorWriteAttrib.ColorWriteAttrib
CompassEffect = CompassEffect.CompassEffect
CubicCurveseg = CubicCurveseg.CubicCurveseg
CullBinAttrib = CullBinAttrib.CullBinAttrib
CullFaceAttrib = CullFaceAttrib.CullFaceAttrib
DecalEffect = DecalEffect.DecalEffect
DepthOffsetAttrib = DepthOffsetAttrib.DepthOffsetAttrib
DepthTestAttrib = DepthTestAttrib.DepthTestAttrib
DepthWriteAttrib = DepthWriteAttrib.DepthWriteAttrib
DialNode = DialNode.DialNode
DirectionalLight = DirectionalLight.DirectionalLight
DriveInterface = DriveInterface.DriveInterface
FiniteBoundingVolume = FiniteBoundingVolume.FiniteBoundingVolume
FloatQueryLerpFunctor = FloatQueryLerpFunctor.FloatQueryLerpFunctor
FogAttrib = FogAttrib.FogAttrib
Geom = Geom.Geom
HprLerpFunctor = HprLerpFunctor.HprLerpFunctor
IntQueryLerpFunctor = IntQueryLerpFunctor.IntQueryLerpFunctor
LODNode = LODNode.LODNode
LightAttrib = LightAttrib.LightAttrib
LightLensNode = LightLensNode.LightLensNode
LinearCylinderVortexForce = LinearCylinderVortexForce.LinearCylinderVortexForce
LinearDistanceForce = LinearDistanceForce.LinearDistanceForce
LinearFrictionForce = LinearFrictionForce.LinearFrictionForce
LinearRandomForce = LinearRandomForce.LinearRandomForce
LinearUserDefinedForce = LinearUserDefinedForce.LinearUserDefinedForce
LinearVectorForce = LinearVectorForce.LinearVectorForce
MaterialAttrib = MaterialAttrib.MaterialAttrib
ModelRoot = ModelRoot.ModelRoot
MouseAndKeyboard = MouseAndKeyboard.MouseAndKeyboard
MouseWatcher = MouseWatcher.MouseWatcher
MovingPartBase = MovingPartBase.MovingPartBase
OmniBoundingVolume = OmniBoundingVolume.OmniBoundingVolume
PGButton = PGButton.PGButton
PGEntry = PGEntry.PGEntry
PGWaitBar = PGWaitBar.PGWaitBar
PartBundle = PartBundle.PartBundle
PiecewiseCurve = PiecewiseCurve.PiecewiseCurve
PointLight = PointLight.PointLight
PosLerpFunctor = PosLerpFunctor.PosLerpFunctor
RenderModeAttrib = RenderModeAttrib.RenderModeAttrib
ScaleLerpFunctor = ScaleLerpFunctor.ScaleLerpFunctor
SequenceNode = SequenceNode.SequenceNode
ShowBoundsEffect = ShowBoundsEffect.ShowBoundsEffect
SimpleQueryLerpFunctorLPoint2f = SimpleQueryLerpFunctorLPoint2f.SimpleQueryLerpFunctorLPoint2f
SimpleQueryLerpFunctorLPoint3f = SimpleQueryLerpFunctorLPoint3f.SimpleQueryLerpFunctorLPoint3f
SimpleQueryLerpFunctorLPoint4f = SimpleQueryLerpFunctorLPoint4f.SimpleQueryLerpFunctorLPoint4f
SimpleQueryLerpFunctorLVecBase2f = SimpleQueryLerpFunctorLVecBase2f.SimpleQueryLerpFunctorLVecBase2f
SimpleQueryLerpFunctorLVecBase3f = SimpleQueryLerpFunctorLVecBase3f.SimpleQueryLerpFunctorLVecBase3f
SimpleQueryLerpFunctorLVecBase4f = SimpleQueryLerpFunctorLVecBase4f.SimpleQueryLerpFunctorLVecBase4f
SimpleQueryLerpFunctorLVector2f = SimpleQueryLerpFunctorLVector2f.SimpleQueryLerpFunctorLVector2f
SimpleQueryLerpFunctorLVector3f = SimpleQueryLerpFunctorLVector3f.SimpleQueryLerpFunctorLVector3f
SimpleQueryLerpFunctorLVector4f = SimpleQueryLerpFunctorLVector4f.SimpleQueryLerpFunctorLVector4f
SwitchNode = SwitchNode.SwitchNode
TexMatrixAttrib = TexMatrixAttrib.TexMatrixAttrib
Texture = Texture.Texture
TextureApplyAttrib = TextureApplyAttrib.TextureApplyAttrib
TextureAttrib = TextureAttrib.TextureAttrib
Trackball = Trackball.Trackball
TrackerNode = TrackerNode.TrackerNode
Transform2SG = Transform2SG.Transform2SG
TransparencyAttrib = TransparencyAttrib.TransparencyAttrib
VirtualMouse = VirtualMouse.VirtualMouse
BoundingSphere = BoundingSphere.BoundingSphere
CharacterJointBundle = CharacterJointBundle.CharacterJointBundle
CollisionHandlerFloor = CollisionHandlerFloor.CollisionHandlerFloor
CollisionHandlerPusher = CollisionHandlerPusher.CollisionHandlerPusher
CollisionPolygon = CollisionPolygon.CollisionPolygon
DynamicTextPage = DynamicTextPage.DynamicTextPage
GeomLine = GeomLine.GeomLine
GeomLinestrip = GeomLinestrip.GeomLinestrip
GeomPoint = GeomPoint.GeomPoint
GeomPolygon = GeomPolygon.GeomPolygon
GeomQuad = GeomQuad.GeomQuad
GeomSphere = GeomSphere.GeomSphere
GeomSprite = GeomSprite.GeomSprite
GeomTri = GeomTri.GeomTri
GeomTrifan = GeomTrifan.GeomTrifan
GeomTristrip = GeomTristrip.GeomTristrip
HermiteCurve = HermiteCurve.HermiteCurve
LinearJitterForce = LinearJitterForce.LinearJitterForce
LinearNoiseForce = LinearNoiseForce.LinearNoiseForce
LinearSinkForce = LinearSinkForce.LinearSinkForce
LinearSourceForce = LinearSourceForce.LinearSourceForce
MovingPartACMatrixSwitchType = MovingPartACMatrixSwitchType.MovingPartACMatrixSwitchType
NurbsCurve = NurbsCurve.NurbsCurve
Spotlight = Spotlight.Spotlight
GeomTextGlyph = GeomTextGlyph.GeomTextGlyph
MovingPartMatrix = MovingPartMatrix.MovingPartMatrix
CharacterJoint = CharacterJoint.CharacterJoint
from FFIExternalObject import registerInTypeMap
registerInTypeMap(AccumulatedAttribs)
registerInTypeMap(AngularIntegrator)
registerInTypeMap(AnimControlCollection)
registerInTypeMap(AsyncUtility)
registerInTypeMap(BamFile)
registerInTypeMap(BaseParticle)
registerInTypeMap(BitMask32)
registerInTypeMap(BoundedObject)
registerInTypeMap(Buffer)
registerInTypeMap(ButtonEvent)
registerInTypeMap(ButtonHandle)
registerInTypeMap(ButtonRegistry)
registerInTypeMap(CString)
registerInTypeMap(ChanCfgOverrides)
registerInTypeMap(ChanConfig)
registerInTypeMap(ClearableRegion)
registerInTypeMap(ClockObject)
registerInTypeMap(CollisionTraverser)
registerInTypeMap(ComputedVertices)
registerInTypeMap(ConfigExpress)
registerInTypeMap(ConnectionManager)
registerInTypeMap(ConnectionReader)
registerInTypeMap(ConnectionWriter)
registerInTypeMap(CullBinManager)
registerInTypeMap(CullableObject)
registerInTypeMap(CurveFitter)
registerInTypeMap(DSearchPath)
registerInTypeMap(DataGraphTraverser)
registerInTypeMap(DataNodeTransmit)
registerInTypeMap(DatagramIterator)
registerInTypeMap(Decompressor)
registerInTypeMap(DocumentSpec)
registerInTypeMap(DownloadDb)
registerInTypeMap(EventParameter)
registerInTypeMap(EventQueue)
registerInTypeMap(EventReceiver)
registerInTypeMap(Extractor)
registerInTypeMap(FILE)
registerInTypeMap(Filename)
registerInTypeMap(FontPool)
registerInTypeMap(FrameBufferProperties)
registerInTypeMap(Frustum)
registerInTypeMap(FrustumD)
registerInTypeMap(Fstream)
registerInTypeMap(GeomTransformer)
registerInTypeMap(GraphicsEngine)
registerInTypeMap(GraphicsPipeSelection)
registerInTypeMap(GraphicsThreadingModel)
registerInTypeMap(HTTPClient)
registerInTypeMap(HTTPDate)
registerInTypeMap(HTTPEntityTag)
registerInTypeMap(HTTPEnum)
registerInTypeMap(HashVal)
registerInTypeMap(Ifstream)
registerInTypeMap(Istream)
registerInTypeMap(KeyboardButton)
registerInTypeMap(LOD)
registerInTypeMap(LinearIntegrator)
registerInTypeMap(LoaderFileType)
registerInTypeMap(Mat3)
registerInTypeMap(Mat3D)
registerInTypeMap(Mat4)
registerInTypeMap(Mat4D)
registerInTypeMap(MaterialPool)
registerInTypeMap(MathNumbers)
registerInTypeMap(ModelPool)
registerInTypeMap(ModifierButtons)
registerInTypeMap(MouseButton)
registerInTypeMap(MouseData)
registerInTypeMap(MouseWatcherParameter)
registerInTypeMap(Multifile)
registerInTypeMap(Namable)
registerInTypeMap(NetAddress)
registerInTypeMap(NodePath)
registerInTypeMap(NodePathCollection)
registerInTypeMap(Notify)
registerInTypeMap(NotifyCategory)
registerInTypeMap(NurbsCurveInterface)
registerInTypeMap(Ofstream)
registerInTypeMap(Ostream)
registerInTypeMap(PGFrameStyle)
registerInTypeMap(PRFileDesc)
registerInTypeMap(PRNetAddr)
registerInTypeMap(PStatClient)
registerInTypeMap(PStatCollector)
registerInTypeMap(PTAUshort)
registerInTypeMap(ParticleSystemManager)
registerInTypeMap(Patcher)
registerInTypeMap(Patchfile)
registerInTypeMap(PhysicsManager)
registerInTypeMap(Pipeline)
registerInTypeMap(Plane)
registerInTypeMap(PlaneD)
registerInTypeMap(PointerToBaseConnection)
registerInTypeMap(PointerToBaseRefCountObjvectorLPoint2f)
registerInTypeMap(PointerToBaseRefCountObjvectorLPoint3f)
registerInTypeMap(PointerToBaseRefCountObjvectorLVecBase4f)
registerInTypeMap(PointerToBaseRefCountObjvectorLVector3f)
registerInTypeMap(PointerToBaseRefCountObjvectorunsignedchar)
registerInTypeMap(ProfileTimer)
registerInTypeMap(QueuedReturnConnectionListenerData)
registerInTypeMap(QueuedReturnNetDatagram)
registerInTypeMap(QueuedReturnPointerToConnection)
registerInTypeMap(Ramfile)
registerInTypeMap(ReferenceCount)
registerInTypeMap(SceneGraphReducer)
registerInTypeMap(StreamReader)
registerInTypeMap(StreamWriter)
registerInTypeMap(TextEncoder)
registerInTypeMap(TextureCollection)
registerInTypeMap(TexturePool)
registerInTypeMap(TimeVal)
registerInTypeMap(TypeHandle)
registerInTypeMap(TypeRegistry)
registerInTypeMap(TypedObject)
registerInTypeMap(URLSpec)
registerInTypeMap(UniqueIdAllocator)
registerInTypeMap(VBase2)
registerInTypeMap(VBase2D)
registerInTypeMap(VBase3)
registerInTypeMap(VBase3D)
registerInTypeMap(VBase4)
registerInTypeMap(VBase4D)
registerInTypeMap(VectorURLSpec)
registerInTypeMap(VectorbasicStringchar)
registerInTypeMap(VirtualFileSystem)
registerInTypeMap(WindowProperties)
registerInTypeMap(WindowsRegistry)
registerInTypeMap(AngularEulerIntegrator)
registerInTypeMap(AnimControl)
registerInTypeMap(AudioManager)
registerInTypeMap(AudioSound)
registerInTypeMap(BaseParticleEmitter)
registerInTypeMap(BaseParticleFactory)
registerInTypeMap(BaseParticleRenderer)
registerInTypeMap(CardMaker)
registerInTypeMap(Connection)
registerInTypeMap(ConnectionListener)
registerInTypeMap(Datagram)
registerInTypeMap(DisplayRegion)
registerInTypeMap(EventHandler)
registerInTypeMap(ISocketStream)
registerInTypeMap(Iostream)
registerInTypeMap(Light)
registerInTypeMap(LineSegs)
registerInTypeMap(LineStream)
registerInTypeMap(LinearEulerIntegrator)
registerInTypeMap(MouseWatcherGroup)
registerInTypeMap(MultiplexStream)
registerInTypeMap(NurbsCurveEvaluator)
registerInTypeMap(NurbsCurveResult)
registerInTypeMap(OSocketStream)
registerInTypeMap(PTAColorf)
registerInTypeMap(PTANormalf)
registerInTypeMap(PTATexCoordf)
registerInTypeMap(PTAUchar)
registerInTypeMap(PTAVertexf)
registerInTypeMap(PandaLoader)
registerInTypeMap(ParametricCurveCollection)
registerInTypeMap(ParametricCurveDrawer)
registerInTypeMap(Point2)
registerInTypeMap(Point2D)
registerInTypeMap(Point3)
registerInTypeMap(Point3D)
registerInTypeMap(Point4)
registerInTypeMap(Point4D)
registerInTypeMap(PointerToConnection)
registerInTypeMap(Quat)
registerInTypeMap(QuatD)
registerInTypeMap(QueuedConnectionManager)
registerInTypeMap(QueuedConnectionReader)
registerInTypeMap(RecentConnectionReader)
registerInTypeMap(TypedReferenceCount)
registerInTypeMap(TypedWritable)
registerInTypeMap(Vec2)
registerInTypeMap(Vec2D)
registerInTypeMap(Vec3)
registerInTypeMap(Vec3D)
registerInTypeMap(Vec4)
registerInTypeMap(Vec4D)
registerInTypeMap(VirtualFileList)
registerInTypeMap(AutonomousLerp)
registerInTypeMap(BaseForce)
registerInTypeMap(BoundingVolume)
registerInTypeMap(BoxEmitter)
registerInTypeMap(ClientBase)
registerInTypeMap(CollisionEntry)
registerInTypeMap(CollisionHandler)
registerInTypeMap(DiscEmitter)
registerInTypeMap(Event)
registerInTypeMap(GeomParticleRenderer)
registerInTypeMap(GraphicsChannel)
registerInTypeMap(GraphicsLayer)
registerInTypeMap(GraphicsPipe)
registerInTypeMap(GraphicsStateGuardianBase)
registerInTypeMap(GraphicsWindow)
registerInTypeMap(LOrientationd)
registerInTypeMap(LOrientationf)
registerInTypeMap(LRotationd)
registerInTypeMap(LRotationf)
registerInTypeMap(Lens)
registerInTypeMap(Lerp)
registerInTypeMap(LerpBlendType)
registerInTypeMap(LerpFunctor)
registerInTypeMap(LineEmitter)
registerInTypeMap(LineParticleRenderer)
registerInTypeMap(MouseWatcherRegion)
registerInTypeMap(NetDatagram)
registerInTypeMap(NurbsCurveDrawer)
registerInTypeMap(PGMouseWatcherParameter)
registerInTypeMap(PandaNode)
registerInTypeMap(Physical)
registerInTypeMap(PhysicsObject)
registerInTypeMap(PointEmitter)
registerInTypeMap(PointParticleFactory)
registerInTypeMap(PointParticleRenderer)
registerInTypeMap(QueuedConnectionListener)
registerInTypeMap(RectangleEmitter)
registerInTypeMap(RingEmitter)
registerInTypeMap(SocketStream)
registerInTypeMap(SparkleParticleRenderer)
registerInTypeMap(SphereSurfaceEmitter)
registerInTypeMap(SphereVolumeEmitter)
registerInTypeMap(SpriteParticleRenderer)
registerInTypeMap(TangentRingEmitter)
registerInTypeMap(TextFont)
registerInTypeMap(TypedWritableReferenceCount)
registerInTypeMap(VirtualFile)
registerInTypeMap(WritableConfigurable)
registerInTypeMap(ZSpinParticleFactory)
registerInTypeMap(AngularForce)
registerInTypeMap(AnimBundleNode)
registerInTypeMap(AnimGroup)
registerInTypeMap(CollisionHandlerEvent)
registerInTypeMap(CollisionHandlerQueue)
registerInTypeMap(CollisionNode)
registerInTypeMap(CollisionSolid)
registerInTypeMap(DDrawable)
registerInTypeMap(DataNode)
registerInTypeMap(DynamicTextFont)
registerInTypeMap(EaseInBlendType)
registerInTypeMap(EaseInOutBlendType)
registerInTypeMap(EaseOutBlendType)
registerInTypeMap(FloatLerpFunctor)
registerInTypeMap(Fog)
registerInTypeMap(ForceNode)
registerInTypeMap(GeomNode)
registerInTypeMap(GeometricBoundingVolume)
registerInTypeMap(GraphicsStateGuardian)
registerInTypeMap(HTTPChannel)
registerInTypeMap(HprScaleLerpFunctor)
registerInTypeMap(ImageBuffer)
registerInTypeMap(IntLerpFunctor)
registerInTypeMap(LensNode)
registerInTypeMap(LightNode)
registerInTypeMap(LinearForce)
registerInTypeMap(Material)
registerInTypeMap(MatrixLens)
registerInTypeMap(ModelNode)
registerInTypeMap(MultiLerpFunctor)
registerInTypeMap(NoBlendType)
registerInTypeMap(OrthographicLens)
registerInTypeMap(PGItem)
registerInTypeMap(PGMouseWatcherBackground)
registerInTypeMap(PGTop)
registerInTypeMap(ParametricCurve)
registerInTypeMap(PartBundleNode)
registerInTypeMap(PartGroup)
registerInTypeMap(ParticleSystem)
registerInTypeMap(PerspectiveLens)
registerInTypeMap(PhysicalNode)
registerInTypeMap(PlaneNode)
registerInTypeMap(PosHprLerpFunctor)
registerInTypeMap(PosHprScaleLerpFunctor)
registerInTypeMap(RenderAttrib)
registerInTypeMap(RenderEffect)
registerInTypeMap(RenderEffects)
registerInTypeMap(RenderState)
registerInTypeMap(RopeNode)
registerInTypeMap(SelectiveChildNode)
registerInTypeMap(SimpleLerpFunctorLPoint2f)
registerInTypeMap(SimpleLerpFunctorLPoint3f)
registerInTypeMap(SimpleLerpFunctorLPoint4f)
registerInTypeMap(SimpleLerpFunctorLVecBase2f)
registerInTypeMap(SimpleLerpFunctorLVecBase3f)
registerInTypeMap(SimpleLerpFunctorLVecBase4f)
registerInTypeMap(SimpleLerpFunctorLVector2f)
registerInTypeMap(SimpleLerpFunctorLVector3f)
registerInTypeMap(SimpleLerpFunctorLVector4f)
registerInTypeMap(StaticTextFont)
registerInTypeMap(TextNode)
registerInTypeMap(TransformState)
registerInTypeMap(VirtualFileComposite)
registerInTypeMap(VirtualFileSimple)
registerInTypeMap(AlphaTestAttrib)
registerInTypeMap(AmbientLight)
registerInTypeMap(AnalogNode)
registerInTypeMap(AngularVectorForce)
registerInTypeMap(AnimBundle)
registerInTypeMap(BillboardEffect)
registerInTypeMap(BoundingLine)
registerInTypeMap(ButtonNode)
registerInTypeMap(ButtonThrower)
registerInTypeMap(Camera)
registerInTypeMap(Character)
registerInTypeMap(ClipPlaneAttrib)
registerInTypeMap(CollisionHandlerPhysical)
registerInTypeMap(CollisionPlane)
registerInTypeMap(CollisionRay)
registerInTypeMap(CollisionSegment)
registerInTypeMap(CollisionSphere)
registerInTypeMap(ColorAttrib)
registerInTypeMap(ColorBlendAttrib)
registerInTypeMap(ColorLerpFunctor)
registerInTypeMap(ColorScaleAttrib)
registerInTypeMap(ColorScaleLerpFunctor)
registerInTypeMap(ColorWriteAttrib)
registerInTypeMap(CompassEffect)
registerInTypeMap(CubicCurveseg)
registerInTypeMap(CullBinAttrib)
registerInTypeMap(CullFaceAttrib)
registerInTypeMap(DecalEffect)
registerInTypeMap(DepthOffsetAttrib)
registerInTypeMap(DepthTestAttrib)
registerInTypeMap(DepthWriteAttrib)
registerInTypeMap(DialNode)
registerInTypeMap(DirectionalLight)
registerInTypeMap(DriveInterface)
registerInTypeMap(FiniteBoundingVolume)
registerInTypeMap(FloatQueryLerpFunctor)
registerInTypeMap(FogAttrib)
registerInTypeMap(Geom)
registerInTypeMap(HprLerpFunctor)
registerInTypeMap(IntQueryLerpFunctor)
registerInTypeMap(LODNode)
registerInTypeMap(LightAttrib)
registerInTypeMap(LightLensNode)
registerInTypeMap(LinearCylinderVortexForce)
registerInTypeMap(LinearDistanceForce)
registerInTypeMap(LinearFrictionForce)
registerInTypeMap(LinearRandomForce)
registerInTypeMap(LinearUserDefinedForce)
registerInTypeMap(LinearVectorForce)
registerInTypeMap(MaterialAttrib)
registerInTypeMap(ModelRoot)
registerInTypeMap(MouseAndKeyboard)
registerInTypeMap(MouseWatcher)
registerInTypeMap(MovingPartBase)
registerInTypeMap(OmniBoundingVolume)
registerInTypeMap(PGButton)
registerInTypeMap(PGEntry)
registerInTypeMap(PGWaitBar)
registerInTypeMap(PartBundle)
registerInTypeMap(PiecewiseCurve)
registerInTypeMap(PointLight)
registerInTypeMap(PosLerpFunctor)
registerInTypeMap(RenderModeAttrib)
registerInTypeMap(ScaleLerpFunctor)
registerInTypeMap(SequenceNode)
registerInTypeMap(ShowBoundsEffect)
registerInTypeMap(SimpleQueryLerpFunctorLPoint2f)
registerInTypeMap(SimpleQueryLerpFunctorLPoint3f)
registerInTypeMap(SimpleQueryLerpFunctorLPoint4f)
registerInTypeMap(SimpleQueryLerpFunctorLVecBase2f)
registerInTypeMap(SimpleQueryLerpFunctorLVecBase3f)
registerInTypeMap(SimpleQueryLerpFunctorLVecBase4f)
registerInTypeMap(SimpleQueryLerpFunctorLVector2f)
registerInTypeMap(SimpleQueryLerpFunctorLVector3f)
registerInTypeMap(SimpleQueryLerpFunctorLVector4f)
registerInTypeMap(SwitchNode)
registerInTypeMap(TexMatrixAttrib)
registerInTypeMap(Texture)
registerInTypeMap(TextureApplyAttrib)
registerInTypeMap(TextureAttrib)
registerInTypeMap(Trackball)
registerInTypeMap(TrackerNode)
registerInTypeMap(Transform2SG)
registerInTypeMap(TransparencyAttrib)
registerInTypeMap(VirtualMouse)
registerInTypeMap(BoundingSphere)
registerInTypeMap(CharacterJointBundle)
registerInTypeMap(CollisionHandlerFloor)
registerInTypeMap(CollisionHandlerPusher)
registerInTypeMap(CollisionPolygon)
registerInTypeMap(DynamicTextPage)
registerInTypeMap(GeomLine)
registerInTypeMap(GeomLinestrip)
registerInTypeMap(GeomPoint)
registerInTypeMap(GeomPolygon)
registerInTypeMap(GeomQuad)
registerInTypeMap(GeomSphere)
registerInTypeMap(GeomSprite)
registerInTypeMap(GeomTri)
registerInTypeMap(GeomTrifan)
registerInTypeMap(GeomTristrip)
registerInTypeMap(HermiteCurve)
registerInTypeMap(LinearJitterForce)
registerInTypeMap(LinearNoiseForce)
registerInTypeMap(LinearSinkForce)
registerInTypeMap(LinearSourceForce)
registerInTypeMap(MovingPartACMatrixSwitchType)
registerInTypeMap(NurbsCurve)
registerInTypeMap(Spotlight)
registerInTypeMap(GeomTextGlyph)
registerInTypeMap(MovingPartMatrix)
registerInTypeMap(CharacterJoint)