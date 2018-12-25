DELETE FROM :table;

COPY :table (id,service_id,name,value,type) FROM stdin;
1	1	hadoop.security.groups.cache.secs	300	core
2	1	hadoop.security.dns.nameserver		core
3	1	hadoop.security.group.mapping.ldap.posix.attr.uid.name	uidNumber	core
4	1	s3.client-write-packet-size	65536	core
5	1	dfs.ha.fencing.ssh.private-key-files		core
6	1	hadoop.security.group.mapping.ldap.directory.search.timeout	10000	core
7	1	fs.s3a.server-side-encryption.key		core
8	1	ipc.client.low-latency	false	core
9	1	fs.ftp.host.port	21	core
10	1	fs.s3a.block.size	32M	core
11	1	fs.s3a.proxy.host		core
12	1	fs.s3a.signing-algorithm		core
13	1	ipc.client.connection.maxidletime	10000	core
14	1	hadoop.security.kms.client.encrypted.key.cache.expiry	43200000	core
15	1	fs.adl.oauth2.devicecode.clientapp.id		core
16	1	fs.s3a.s3guard.ddb.table		core
17	1	tfile.io.chunk.size	1048576	core
18	1	hadoop.registry.zk.session.timeout.ms	60000	core
19	1	fs.automatic.close	true	core
20	1	fs.azure.sas.expiry.period	90d	core
21	1	fs.s3a.secret.key		core
22	1	ha.health-monitor.sleep-after-disconnect.ms	1000	core
23	1	io.map.index.interval	128	core
24	1	fs.s3n.multipart.uploads.enabled	false	core
25	1	hadoop.util.hash.type	murmur	core
26	1	hadoop.security.groups.cache.background.reload.threads	3	core
27	1	fs.azure.user.agent.prefix	unknown	core
28	1	fs.s3a.session.token		core
29	1	hadoop.security.group.mapping.ldap.bind.user		core
30	1	hadoop.security.group.mapping.ldap.posix.attr.gid.name	gidNumber	core
31	1	fs.s3a.path.style.access	false	core
32	1	fs.s3a.metadatastore.authoritative	false	core
33	1	fs.AbstractFileSystem.file.impl	org.apache.hadoop.fs.local.LocalFs	core
34	1	net.topology.script.number.args	100	core
35	1	fs.s3.block.size	67108864	core
36	1	hadoop.http.authentication.token.validity	36000	core
37	1	ha.failover-controller.graceful-fence.rpc-timeout.ms	5000	core
38	1	s3native.bytes-per-checksum	512	core
39	1	hadoop.security.group.mapping	org.apache.hadoop.security.JniBasedUnixGroupsMappingWithFallback	core
40	1	fs.s3a.proxy.workstation		core
41	1	hadoop.security.groups.cache.warn.after.ms	5000	core
42	1	io.serializations	org.apache.hadoop.io.serializer.WritableSerialization, org.apache.hadoop.io.serializer.avro.AvroSpecificSerialization, org.apache.hadoop.io.serializer.avro.AvroReflectSerialization	core
43	1	fs.s3a.access.key		core
44	1	hadoop.security.crypto.buffer.size	8192	core
45	1	fs.ftp.transfer.mode	BLOCK_TRANSFER_MODE	core
46	1	hadoop.http.cross-origin.allowed-methods	GET,POST,HEAD	core
47	1	hadoop.htrace.span.receiver.classes		core
48	1	hadoop.registry.zk.retry.interval.ms	1000	core
49	1	hadoop.socks.server		core
50	1	fs.protected.directories		core
51	1	hadoop.zk.acl	world:anyone:rwcda	core
52	1	hadoop.registry.secure	false	core
53	1	hadoop.security.saslproperties.resolver.class		core
54	1	fs.wasb.impl	org.apache.hadoop.fs.azure.NativeAzureFileSystem	core
55	1	hadoop.kerberos.kinit.command	kinit	core
56	1	fs.trash.interval	0	core
57	1	fs.s3a.proxy.password		core
58	1	fs.s3a.multiobjectdelete.enable	true	core
59	1	hadoop.security.impersonation.provider.class		core
60	1	fs.viewfs.rename.strategy	SAME_MOUNTPOINT	core
61	1	ipc.client.connect.max.retries.on.timeouts	45	core
62	1	s3.blocksize	67108864	core
63	1	fs.client.resolve.topology.enabled	false	core
64	1	seq.io.sort.factor	100	core
65	1	adl.feature.ownerandgroup.enableupn	false	core
66	1	fs.s3.buffer.dir	${hadoop.tmp.dir}/s3	core
67	1	fs.s3a.security.credential.provider.path		core
68	1	fs.s3n.block.size	67108864	core
69	1	fs.s3a.fast.upload.buffer	disk	core
70	1	seq.io.sort.mb	100	core
71	1	net.topology.table.file.name		core
72	1	ha.health-monitor.connect-retry-interval.ms	1000	core
73	1	nfs.exports.allowed.hosts	* rw	core
74	1	hadoop.security.instrumentation.requires.admin	false	core
75	1	hadoop.registry.zk.retry.ceiling.ms	60000	core
76	1	io.file.buffer.size	4096	core
77	1	fs.s3a.user.agent.prefix		core
78	1	io.mapfile.bloom.size	1048576	core
79	1	fs.ftp.data.connection.mode	ACTIVE_LOCAL_DATA_CONNECTION_MODE	core
80	1	ipc.client.connect.retry.interval	1000	core
81	1	hadoop.security.secure.random.impl		core
82	1	hadoop.security.kms.client.authentication.retry-count	1	core
83	1	fs.swift.impl	org.apache.hadoop.fs.swift.snative.SwiftNativeFileSystem	core
84	1	fs.s3a.s3guard.ddb.table.capacity.write	100	core
85	1	ha.failover-controller.graceful-fence.connection.retries	1	core
86	1	fs.AbstractFileSystem.adl.impl	org.apache.hadoop.fs.adl.Adl	core
87	1	hadoop.registry.zk.connection.timeout.ms	15000	core
88	1	fs.s3a.proxy.username		core
89	1	hadoop.security.crypto.jce.provider		core
90	1	hadoop.security.java.secure.random.algorithm	SHA1PRNG	core
91	1	ftp.blocksize	67108864	core
92	1	fs.s3n.server-side-encryption-algorithm		core
93	1	hadoop.security.group.mapping.ldap.base		core
94	1	file.stream-buffer-size	4096	core
95	1	fs.s3a.max.total.tasks	5	core
96	1	fs.s3a.server-side-encryption-algorithm		core
97	1	fs.azure.secure.mode	false	core
98	1	hadoop.security.group.mapping.ldap.search.group.hierarchy.levels	0	core
99	1	ipc.client.idlethreshold	4000	core
100	1	io.skip.checksum.errors	false	core
101	1	ftp.stream-buffer-size	4096	core
102	1	fs.s3a.fast.upload	false	core
103	1	file.blocksize	67108864	core
104	1	ftp.replication	3	core
105	1	hadoop.security.authorization	false	core
106	1	hadoop.http.authentication.simple.anonymous.allowed	true	core
107	1	hadoop.rpc.socket.factory.class.default	org.apache.hadoop.net.StandardSocketFactory	core
108	1	file.bytes-per-checksum	512	core
109	1	s3native.client-write-packet-size	65536	core
110	1	fs.har.impl.disable.cache	true	core
111	1	fs.AbstractFileSystem.sweb1.impl	org.apache.hadoop.fs.SWeb1	core
112	1	hadoop.security.dns.log-slow-lookups.threshold.ms	1000	core
113	1	hadoop.common.configuration.version	0.23.0	core
114	1	hadoop.security.authentication	simple	core
115	1	file.replication	1	core
116	1	io.mapfile.bloom.error.rate	0.005	core
117	1	io.compression.codecs		core
118	1	hadoop.security.kms.client.encrypted.key.cache.size	500	core
119	1	fs.adl.oauth2.access.token.provider		core
120	1	fs.s3a.multipart.purge	false	core
121	1	hadoop.security.group.mapping.ldap.search.attr.member	member	core
122	1	fs.s3a.connection.establish.timeout	5000	core
123	1	hadoop.security.dns.interface		core
124	1	hadoop.ssl.client.conf	ssl-client.xml	core
125	1	fs.s3a.multipart.purge.age	86400	core
126	1	hadoop.security.groups.cache.background.reload	false	core
127	1	hadoop.security.kms.client.encrypted.key.cache.low-watermark	0.3f	core
128	1	hadoop.user.group.static.mapping.overrides	dr.who=;	core
129	1	hadoop.security.credential.clear-text-fallback	true	core
130	1	ipc.maximum.data.length	67108864	core
131	1	hadoop.zk.address		core
132	1	tfile.fs.input.buffer.size	262144	core
133	1	ha.failover-controller.new-active.rpc-timeout.ms	60000	core
134	1	hadoop.ssl.hostname.verifier	DEFAULT	core
135	1	hadoop.security.group.mapping.ldap.url		core
136	1	hadoop.http.authentication.type	simple	core
137	1	s3native.blocksize	67108864	core
138	1	net.topology.impl	org.apache.hadoop.net.NetworkTopology	core
139	1	fs.client.htrace.sampler.classes		core
140	1	io.seqfile.compress.blocksize	1000000	core
141	1	fs.AbstractFileSystem.web1.impl	org.apache.hadoop.fs.Web1	core
142	1	hadoop.registry.zk.retry.times	5	core
143	1	fs.AbstractFileSystem.ftp.impl	org.apache.hadoop.fs.ftp.FtpFs	core
144	1	fs.s3a.acl.default		core
145	1	ftp.bytes-per-checksum	512	core
146	1	hadoop.workaround.non.threadsafe.getpwuid	true	core
147	1	ipc.client.fallback-to-simple-auth-allowed	false	core
148	1	hadoop.zk.auth		core
149	1	hadoop.security.group.mapping.ldap.ssl.keystore.password		core
150	1	hadoop.rpc.protection	authentication	core
151	1	fs.permissions.umask-mode	22	core
152	1	fs.s3.sleepTimeSeconds	10	core
153	1	fs.adl.oauth2.msi.port		core
154	1	ha.health-monitor.rpc-timeout.ms	45000	core
155	1	hadoop.http.staticuser.user	dr.who	core
156	1	fs.s3a.connection.maximum	15	core
157	1	fs.AbstractFileSystem.viewfs.impl	org.apache.hadoop.fs.viewfs.ViewFs	core
158	1	fs.s3a.paging.maximum	5000	core
159	1	fs.s3a.s3guard.cli.prune.age	86400000	core
160	1	fs.ftp.host	0.0.0.0	core
161	1	ipc.maximum.response.length	134217728	core
162	1	fs.adl.oauth2.access.token.provider.type	ClientCredential	core
163	1	hadoop.shell.missing.defaultFs.warning	false	core
164	1	fs.s3a.impl	org.apache.hadoop.fs.s3a.S3AFileSystem	core
165	1	hadoop.http.authentication.kerberos.keytab	${user.home}/hadoop.keytab	core
166	1	hadoop.registry.zk.root	/registry	core
167	1	fs.s3a.s3guard.ddb.background.sleep	25	core
168	1	hadoop.jetty.logs.serve.aliases	true	core
169	1	hadoop.security.service.user.name.key		core
170	1	fs.azure.saskey.usecontainersaskeyforallaccess	true	core
171	1	hadoop.security.auth_to_local		core
172	1	hadoop.caller.context.max.size	128	core
173	1	hadoop.http.cross-origin.max-age	1800	core
174	1	io.compression.codec.bzip2.library	system-native	core
175	1	fs.s3n.awsSecretAccessKey		core
176	1	ipc.ping.interval	60000	core
177	1	net.topology.node.switch.mapping.impl	org.apache.hadoop.net.ScriptBasedMapping	core
178	1	hadoop.security.group.mapping.providers		core
179	1	hadoop.security.group.mapping.ldap.ssl.keystore.password.file		core
180	1	fs.s3a.aws.credentials.provider		core
181	1	fs.df.interval	60000	core
182	1	fs.s3a.readahead.range	64K	core
183	1	ha.zookeeper.parent-znode	/hadoop-ha	core
184	1	hadoop.http.cross-origin.allowed-headers	X-Requested-With,Content-Type,Accept,Origin	core
185	1	fs.s3a.proxy.port		core
186	1	fs.s3a.attempts.maximum	20	core
187	1	s3native.stream-buffer-size	4096	core
188	1	fs.s3a.proxy.domain		core
189	1	fs.azure.authorization	false	core
190	1	io.seqfile.local.dir	${hadoop.tmp.dir}/io/local	core
191	1	fs.s3n.multipart.copy.block.size	5368709120	core
192	1	fs.azure.authorization.caching.enable	true	core
193	1	hadoop.security.kms.client.failover.sleep.max.millis	2000	core
194	1	hadoop.security.credential.provider.path		core
195	1	fs.adl.oauth2.refresh.url		core
196	1	fs.wasbs.impl	org.apache.hadoop.fs.azure.NativeAzureFileSystem$Secure	core
197	1	net.topology.script.file.name		core
198	1	hadoop.ssl.keystores.factory.class	org.apache.hadoop.security.ssl.FileBasedKeyStoresFactory	core
199	1	hadoop.zk.num-retries	1000	core
200	1	fs.AbstractFileSystem.1.impl	org.apache.hadoop.fs.1	core
201	1	fs.s3.maxRetries	4	core
202	1	hadoop.security.random.device.file.path	/dev/urandom	core
203	1	hadoop.http.filter.initializers	org.apache.hadoop.http.lib.StaticUserWebFilter	core
204	1	ha.zookeeper.quorum		core
205	1	ipc.client.rpc-timeout.ms	0	core
206	1	fs.s3a.s3guard.ddb.region		core
207	1	fs.client.resolve.remote.symlinks	true	core
208	1	hadoop.rpc.socket.factory.class.ClientProtocol		core
209	1	fs.s3a.s3guard.ddb.max.retries	9	core
210	1	hadoop.ssl.enabled.protocols	TLSv1,SSLv2Hello,TLSv1.1,TLSv1.2	core
211	1	rpc.metrics.quantile.enable	false	core
212	1	hadoop.ssl.enabled	false	core
213	1	io.bytes.per.checksum	512	core
214	1	fs.azure.local.sas.key.mode	false	core
215	1	ipc.client.kill.max	10	core
216	1	fs.s3a.threads.max	10	core
217	1	ipc.server.listen.queue.size	128	core
218	1	rpc.metrics.percentiles.intervals		core
219	1	fs.s3a.connection.timeout	200000	core
220	1	fs.s3a.threads.keepalivetime	60	core
221	1	hadoop.caller.context.signature.max.size	40	core
222	1	hadoop.security.dns.log-slow-lookups.enabled	false	core
223	1	hadoop.security.group.mapping.ldap.search.attr.memberof		core
224	1	hadoop.security.group.mapping.ldap.connection.timeout.ms	60000	core
225	1	hadoop.security.groups.shell.command.timeout	0s	core
226	1	fs.s3a.s3guard.ddb.table.capacity.read	500	core
227	1	file.client-write-packet-size	65536	core
228	1	ha.failover-controller.cli-check.rpc-timeout.ms	20000	core
229	1	fs.s3.awsSecretAccessKey		core
230	1	ipc.client.connect.max.retries	10	core
231	1	ha.zookeeper.acl	world:anyone:rwcda	core
232	1	fs.adl.oauth2.credential		core
233	1	ipc.client.ping	true	core
234	1	hadoop.security.kms.client.timeout	60	core
235	1	hadoop.tmp.dir	/tmp/hadoop-${user.name}	core
236	1	hadoop.security.kms.client.failover.sleep.base.millis	100	core
237	1	fs.adl.oauth2.client.id		core
238	1	hadoop.security.group.mapping.ldap.bind.password.file		core
239	1	hadoop.ssl.require.client.cert	false	core
240	1	hadoop.security.uid.cache.secs	14400	core
241	1	hadoop.registry.rm.enabled	false	core
242	1	hadoop.registry.kerberos.realm		core
243	1	hadoop.security.key.provider.path		core
244	1	hadoop.security.group.mapping.ldap.ssl.keystore		core
245	1	fs.trash.checkpoint.interval	0	core
246	1	hadoop.zk.timeout-ms	10000	core
247	1	fs.AbstractFileSystem.s3a.impl	org.apache.hadoop.fs.s3a.S3A	core
248	1	ha.health-monitor.check-interval.ms	1000	core
249	1	ipc.client.tcpnodelay	true	core
250	1	ipc.client.connect.timeout	20000	core
251	1	hadoop.http.authentication.cookie.domain		core
252	1	fs.s3a.multipart.threshold	2147483647	core
253	1	io.map.index.skip	0	core
254	1	hadoop.http.cross-origin.enabled	false	core
255	1	io.native.lib.available	true	core
256	1	s3.replication	3	core
257	1	hadoop.security.group.mapping.providers.combined	true	core
258	1	fs.AbstractFileSystem.har.impl	org.apache.hadoop.fs.HarFs	core
259	1	hadoop.kerberos.min.seconds.before.relogin	60	core
260	1	hadoop.security.kms.client.encrypted.key.cache.num.refill.threads	2	core
261	1	fs.s3n.multipart.uploads.block.size	67108864	core
262	1	hadoop.token.files		core
263	1	fs.default.name	file:///	core
264	1	tfile.fs.output.buffer.size	262144	core
265	1	fs.du.interval	600000	core
266	1	hadoop.security.group.mapping.ldap.ssl	false	core
267	1	hadoop.zk.retry-interval-ms	1000	core
268	1	fs.s3a.buffer.dir	${hadoop.tmp.dir}/s3a	core
269	1	fs.defaultFS	file:///	core
270	1	fs.s3n.awsAccessKeyId		core
271	1	fs.s3a.multipart.size	100M	core
272	1	fs.s3.awsAccessKeyId		core
273	1	hadoop.security.group.mapping.ldap.search.attr.group.name	cn	core
274	1	fs.s3a.socket.send.buffer	8192	core
275	1	dfs.ha.fencing.ssh.connect-timeout	30000	core
276	1	hadoop.registry.zk.quorum	localhost:2181	core
277	1	hadoop.http.cross-origin.allowed-origins	*	core
278	1	dfs.ha.fencing.methods		core
279	1	hadoop.security.group.mapping.ldap.bind.password		core
280	1	hadoop.registry.system.acls	sasl:yarn@, sasl:mapred@, sasl:1@	core
281	1	fs.adl.oauth2.refresh.token		core
282	1	hadoop.security.crypto.cipher.suite	AES/CTR/NoPadding	core
283	1	fs.s3a.fast.upload.active.blocks	4	core
284	1	hadoop.security.crypto.codec.classes.aes.ctr.nopadding	org.apache.hadoop.crypto.OpensslAesCtrCryptoCodec, org.apache.hadoop.crypto.JceAesCtrCryptoCodec	core
285	1	hadoop.security.group.mapping.ldap.userbase		core
286	1	fs.s3a.metadatastore.impl	org.apache.hadoop.fs.s3a.s3guard.NullMetadataStore	core
287	1	hadoop.security.groups.negative-cache.secs	30	core
288	1	hadoop.security.group.mapping.ldap.groupbase		core
289	1	hadoop.ssl.server.conf	ssl-server.xml	core
290	1	hadoop.registry.jaas.context	Client	core
291	1	s3native.replication	3	core
292	1	hadoop.security.group.mapping.ldap.search.filter.group	(objectClass=group)	core
293	1	hadoop.http.authentication.kerberos.principal	HTTP/_HOST@LOCALHOST	core
294	1	hadoop.caller.context.enabled	false	core
295	1	hadoop.shell.safely.delete.limit.num.files	100	core
296	1	hadoop.security.group.mapping.ldap.search.filter.user	(&(objectClass=user)(sAMAccountName={0}))	core
297	1	fs.s3a.s3guard.ddb.table.create	false	core
298	1	s3.stream-buffer-size	4096	core
299	1	ftp.client-write-packet-size	65536	core
300	1	fs.s3a.socket.recv.buffer	8192	core
301	1	fs.adl.impl	org.apache.hadoop.fs.adl.AdlFileSystem	core
302	1	hadoop.security.sensitive-config-keys	"password$,fs.s3.*[Ss]ecret.?[Kk]ey,fs.azure.account.key.*,dfs.webhdfs.oauth2.[a-z]+.token,hadoop.security.sensitive-config-keys"	core
303	1	ipc.server.log.slow.rpc	false	core
304	1	hadoop.security.group.mapping.ldap.read.timeout.ms	60000	core
305	1	hadoop.http.logs.enabled	true	core
306	1	s3.bytes-per-checksum	512	core
307	1	ha.zookeeper.session-timeout.ms	5000	core
308	1	fs.s3a.connection.ssl.enabled	true	core
309	1	hadoop.security.credstore.java-keystore-provider.password-file		core
310	1	hadoop.http.authentication.signature.secret.file	${user.home}/hadoop-http-auth-signature-secret	core
311	1	ha.zookeeper.auth		core
312	1	hadoop.security.crypto.codec.classes.EXAMPLECIPHERSUITE		core
313	1	ipc.server.max.connections	0	core
314	1	fs.s3a.endpoint		core
315	1	dfs.use.dfs.network.topology	true	1
316	1	dfs.namenode.resource.check.interval	5000	1
317	1	dfs.block.invalidate.limit	1000	1
318	1	dfs.client.https.need-auth	false	1
319	1	dfs.namenode.write-lock-reporting-threshold-ms	5000	1
320	1	dfs.namenode.avoid.read.stale.datanode	false	1
321	1	dfs.journalnode.rpc-address	0.0.0.0:8485	1
322	1	dfs.qjournal.select-input-streams.timeout.ms	20000	1
323	1	dfs.namenode.lease-recheck-interval-ms	2000	1
324	1	dfs.client.block.write.locateFollowingBlock.initial.delay.ms	400	1
325	1	dfs.mover.retry.max.attempts	10	1
326	1	dfs.namenode.https-address	0.0.0.0:50470	1
327	1	dfs.mover.max-no-move-interval	60000	1
328	1	dfs.hosts.exclude		1
329	1	dfs.namenode.replication.min	1	1
330	1	dfs.client.socketcache.expiryMsec	3000	1
331	1	dfs.namenode.fs-limits.min-block-size	1048576	1
332	1	dfs.federation.router.admin-address	0.0.0.0:8111	1
333	1	dfs.namenode.path.based.cache.block.map.allocation.percent	0.25	1
334	1	dfs.web1.use.ipc.callq	true	1
335	1	dfs.datanode.cache.revocation.polling.ms	500	1
336	1	dfs.namenode.lazypersist.file.scrub.interval.sec	300	1
337	1	dfs.namenode.replication.interval	3	1
338	1	nfs.dump.dir	/tmp/.1-nfs	1
339	1	dfs.web.authentication.simple.anonymous.allowed		1
340	1	dfs.mover.movedWinWidth	5400000	1
341	1	dfs.datanode.cached-dfsused.check.interval.ms	600000	1
342	1	datanode.https.port	50475	1
343	1	dfs.client.use.datanode.hostname	false	1
344	1	dfs.balancer.getBlocks.size	2147483648	1
345	1	dfs.mover.moverThreads	1000	1
346	1	dfs.datanode.data.dir	file://${hadoop.tmp.dir}/dfs/data	1
347	1	nfs.rtmax	1048576	1
348	1	dfs.client.write.byte-array-manager.count-threshold	128	1
349	1	dfs.datanode.data.dir.perm	700	1
350	1	dfs.namenode.backup.address	0.0.0.0:50100	1
351	1	dfs.balancer.movedWinWidth	5400000	1
352	1	dfs.namenode.max-lock-hold-to-release-lease-ms	25	1
353	1	dfs.datanode.readahead.bytes	4194304	1
354	1	dfs.namenode.xattrs.enabled	true	1
355	1	dfs.datanode.transfer.socket.send.buffer.size	0	1
356	1	dfs.datanode.bp-ready.timeout	20	1
357	1	dfs.client.block.write.retries	3	1
358	1	httpfs.buffer.size	4096	1
359	1	dfs.namenode.safemode.threshold-pct	0.999f	1
360	1	dfs.namenode.servicerpc-bind-host		1
361	1	dfs.namenode.list.cache.directives.num.responses	100	1
362	1	dfs.datanode.dns.nameserver	default	1
363	1	dfs.namenode.replication.considerLoad	true	1
364	1	dfs.namenode.edits.journal-plugin.qjournal	org.apache.hadoop.1.qjournal.client.QuorumJournalManager	1
365	1	dfs.client.write.exclude.nodes.cache.expiry.interval.millis	600000	1
366	1	dfs.nameservices		1
367	1	dfs.client.mmap.cache.timeout.ms	3600000	1
368	1	dfs.namenode.replication.pending.timeout-sec	-1	1
369	1	dfs.namenode.file.close.num-committed-allowed	0	1
370	1	dfs.federation.router.heartbeat.enable	true	1
371	1	dfs.web1.oauth2.refresh.url		1
372	1	dfs.datanode.hostname		1
373	1	dfs.datanode.slow.io.warning.threshold.ms	300	1
374	1	dfs.namenode.reject-unresolved-dn-topology-mapping	false	1
375	1	dfs.datanode.drop.cache.behind.reads	false	1
376	1	dfs.client.socket-timeout	60000	1
377	1	dfs.federation.router.namenode.resolver.client.class	org.apache.hadoop.1.server.federation.resolver.MembershipNamenodeResolver	1
378	1	dfs.client.use.legacy.blockreader	false	1
379	1	dfs.xframe.value	SAMEORIGIN	1
380	1	dfs.namenode.top.num.users	10	1
381	1	dfs.namenode.replication.max-streams-hard-limit	4	1
382	1	dfs.datanode.keytab.file		1
383	1	dfs.federation.router.http-bind-host		1
384	1	dfs.namenode.edit.log.autoroll.check.interval.ms	300000	1
385	1	hadoop.1.configuration.version	1	1
386	1	dfs.federation.router.https-address	0.0.0.0:50072	1
387	1	dfs.qjournal.start-segment.timeout.ms	20000	1
388	1	dfs.federation.router.admin-bind-host		1
389	1	dfs.journalnode.https-address	0.0.0.0:8481	1
390	1	dfs.client.cache.drop.behind.reads		1
391	1	dfs.namenode.max.objects	0	1
392	1	dfs.bytes-per-checksum	512	1
393	1	dfs.cluster.administrators		1
394	1	dfs.datanode.max.transfer.threads	4096	1
395	1	dfs.block.access.key.update.interval	600	1
396	1	dfs.client.read.shortcircuit	false	1
397	1	dfs.datanode.directoryscan.throttle.limit.ms.per.sec	1000	1
398	1	dfs.datanode.1-blocks-metadata.enabled	false	1
399	1	dfs.image.transfer.chunksize	65536	1
400	1	dfs.client.https.keystore.resource	ssl-client.xml	1
401	1	dfs.namenode.audit.log.token.tracking.id	false	1
402	1	dfs.client.failover.sleep.base.millis	500	1
403	1	dfs.permissions.superusergroup	supergroup	1
404	1	dfs.federation.router.handler.count	10	1
405	1	dfs.namenode.checkpoint.edits.dir	${dfs.namenode.checkpoint.dir}	1
406	1	dfs.client.socket.send.buffer.size	0	1
407	1	dfs.balancer.getBlocks.min-block-size	10485760	1
408	1	dfs.client.hedged.read.threadpool.size	0	1
409	1	dfs.blockreport.initialDelay	0	1
410	1	dfs.namenode.heartbeat.recheck-interval	300000	1
411	1	dfs.namenode.safemode.extension	30000	1
412	1	dfs.client.cache.readahead		1
413	1	dfs.client.failover.sleep.max.millis	15000	1
414	1	dfs.http.client.failover.sleep.base.millis	500	1
415	1	dfs.namenode.delegation.key.update-interval	86400000	1
416	1	dfs.namenode.fs-limits.max-blocks-per-file	1048576	1
417	1	dfs.namenode.hosts.provider.classname	org.apache.hadoop.1.server.blockmanagement.HostFileManager	1
418	1	dfs.client.block.write.replace-datanode-on-failure.enable	true	1
419	1	dfs.balancer.keytab.enabled	false	1
420	1	dfs.namenode.lifeline.handler.ratio	0.1	1
421	1	dfs.namenode.checkpoint.dir	file://${hadoop.tmp.dir}/dfs/namesecondary	1
422	1	dfs.client.use.legacy.blockreader.local	false	1
423	1	dfs.namenode.top.windows.minutes	1,5,25	1
424	1	dfs.web1.rest-csrf.browser-useragents-regex	^Mozilla.*,^Opera.*	1
425	1	dfs.ha.zkfc.port	8019	1
426	1	dfs.client.retry.window.base	3000	1
427	1	dfs.storage.policy.enabled	true	1
428	1	dfs.federation.router.https-bind-host		1
429	1	dfs.namenode.list.cache.pools.num.responses	100	1
430	1	nfs.server.port	2049	1
431	1	dfs.checksum.type	CRC32C	1
432	1	dfs.client.read.short.circuit.replica.stale.threshold.ms	1800000	1
433	1	dfs.client.cache.drop.behind.writes		1
434	1	dfs.encrypt.data.transfer.cipher.suites		1
435	1	dfs.datanode.block-pinning.enabled	false	1
436	1	dfs.datanode.lazywriter.interval.sec	60	1
437	1	dfs.encrypt.data.transfer.cipher.key.bitlength	128	1
438	1	dfs.datanode.sync.behind.writes	false	1
439	1	dfs.balancer.dispatcherThreads	200	1
440	1	dfs.federation.router.reader.count	1	1
441	1	dfs.namenode.stale.datanode.interval	30000	1
442	1	dfs.federation.router.rpc.enable	true	1
443	1	hadoop.user.group.metrics.percentiles.intervals		1
444	1	dfs.replication.max	512	1
445	1	dfs.namenode.name.dir	file://${hadoop.tmp.dir}/dfs/name	1
446	1	dfs.datanode.https.address	0.0.0.0:50475	1
447	1	dfs.ha.standby.checkpoints	true	1
448	1	dfs.client.domain.socket.data.traffic	false	1
449	1	dfs.block.access.token.enable	false	1
450	1	dfs.web1.rest-csrf.methods-to-ignore	GET,OPTIONS,HEAD,TRACE	1
451	1	dfs.client.write.byte-array-manager.enabled	false	1
452	1	dfs.datanode.address	0.0.0.0:50010	1
453	1	dfs.datanode.fileio.profiling.sampling.percentage	0	1
454	1	dfs.web.ugi		1
455	1	dfs.namenode.lifeline.handler.count		1
456	1	dfs.ls.limit	1000	1
457	1	dfs.short.circuit.shared.memory.watcher.interrupt.check.ms	60000	1
458	1	dfs.metrics.percentiles.intervals		1
459	1	dfs.data.transfer.protection		1
460	1	dfs.web1.rest-csrf.custom-header	X-XSRF-HEADER	1
461	1	dfs.datanode.handler.count	10	1
462	1	dfs.block.local-path-access.user		1
463	1	dfs.hosts		1
464	1	dfs.namenode.block-placement-policy.default.prefer-local-node	true	1
465	1	dfs.namenode.resource.checked.volumes.minimum	1	1
466	1	dfs.http.client.retry.max.attempts	10	1
467	1	dfs.namenode.name.cache.threshold	10	1
468	1	dfs.namenode.max.full.block.report.leases	6	1
469	1	dfs.namenode.max.extra.edits.segments.retained	10000	1
470	1	dfs.web1.user.provider.user.pattern	^[A-Za-z_][A-Za-z0-9._-]*[$]?$	1
471	1	dfs.datanode.ram.disk.replica.tracker		1
472	1	dfs.client.mmap.enabled	true	1
473	1	dfs.client.file-block-storage-locations.timeout.millis	1000	1
474	1	hadoop.fuse.timer.period	5	1
475	1	dfs.journalnode.http-address	0.0.0.0:8480	1
476	1	dfs.namenode.retrycache.heap.percent	0.03f	1
477	1	dfs.client.hedged.read.threshold.millis	500	1
478	1	dfs.image.transfer-bootstrap-standby.bandwidthPerSec	0	1
479	1	dfs.balancer.kerberos.principal		1
480	1	dfs.balancer.block-move.timeout	0	1
481	1	dfs.client.write.byte-array-manager.count-limit	2048	1
482	1	dfs.federation.router.store.serializer	org.apache.hadoop.1.server.federation.store.driver.impl.StateStoreSerializerPBImpl	1
483	1	dfs.federation.router.reader.queue.size	100	1
484	1	dfs.image.compress	false	1
485	1	dfs.federation.router.rpc-bind-host		1
486	1	dfs.datanode.available-space-volume-choosing-policy.balanced-space-preference-fraction	0.75f	1
487	1	dfs.federation.router.store.driver.class	org.apache.hadoop.1.server.federation.store.driver.impl.StateStoreFileImpl	1
488	1	dfs.namenode.edit.log.autoroll.multiplier.threshold	2	1
489	1	dfs.namenode.checkpoint.check.period	60	1
490	1	dfs.namenode.http-bind-host		1
491	1	dfs.client.slow.io.warning.threshold.ms	30000	1
492	1	dfs.namenode.max-num-blocks-to-log	1000	1
493	1	dfs.qjournal.new-epoch.timeout.ms	120000	1
494	1	dfs.federation.router.http.enable	true	1
495	1	dfs.namenode.service.handler.count	10	1
496	1	dfs.namenode.edits.asynclogging	true	1
497	1	dfs.datanode.plugins		1
498	1	dfs.blockreport.incremental.intervalMsec	0	1
499	1	dfs.namenode.http-address	0.0.0.0:50070	1
500	1	dfs.ha.namenodes.EXAMPLENAMESERVICE		1
501	1	dfs.client.read.prefetch.size		1
502	1	dfs.datanode.network.counts.cache.max.size	2147483647	1
503	1	dfs.qjournal.get-journal-state.timeout.ms	120000	1
504	1	dfs.namenode.startup.delay.block.deletion.sec	0	1
505	1	dfs.client.socketcache.capacity	16	1
506	1	dfs.namenode.checkpoint.max-retries	3	1
507	1	dfs.datanode.fsdatasetcache.max.threads.per.volume	4	1
508	1	dfs.client.retry.policy.spec	10000,6,60000,10	1
509	1	dfs.heartbeat.interval	3	1
510	1	hadoop.fuse.connection.timeout	300	1
511	1	dfs.http.client.retry.policy.spec	10000,6,60000,10	1
512	1	dfs.datanode.cache.revocation.timeout.ms	900000	1
513	1	dfs.datanode.peer.stats.enabled	false	1
514	1	dfs.replication	3	1
515	1	dfs.datanode.available-space-volume-choosing-policy.balanced-space-threshold	10737418240	1
516	1	dfs.namenode.audit.log.async	false	1
517	1	dfs.datanode.disk.check.timeout	10m	1
518	1	dfs.federation.router.connection.pool-size	1	1
519	1	nfs.kerberos.principal		1
520	1	dfs.namenode.audit.log.debug.cmdlist		1
521	1	dfs.qjm.operations.timeout	60s	1
522	1	dfs.namenode.stale.datanode.minimum.interval	3	1
523	1	dfs.client.replica.accessor.builder.classes		1
524	1	dfs.federation.router.store.membership.expiration	300000	1
525	1	dfs.content-summary.sleep-microsec	500	1
526	1	dfs.datanode.directoryscan.threads	1	1
527	1	dfs.datanode.directoryscan.interval	21600	1
528	1	dfs.namenode.acls.enabled	false	1
529	1	dfs.journalnode.keytab.file		1
530	1	dfs.client.short.circuit.replica.stale.threshold.ms	1800000	1
531	1	dfs.secondary.namenode.keytab.file		1
532	1	dfs.namenode.resource.du.reserved	104857600	1
533	1	dfs.federation.router.connection.clean.ms	10000	1
534	1	dfs.namenode.datanode.registration.ip-hostname-check	true	1
535	1	dfs.journalnode.kerberos.principal		1
536	1	dfs.federation.router.metrics.class	org.apache.hadoop.1.server.federation.metrics.FederationRPCPerformanceMonitor	1
537	1	dfs.federation.router.cache.ttl	60000	1
538	1	dfs.namenode.backup.http-address	0.0.0.0:50105	1
539	1	dfs.datanode.parallel.volumes.load.threads.num		1
540	1	dfs.web.authentication.kerberos.keytab		1
541	1	dfs.namenode.edits.noeditlogchannelflush	false	1
542	1	dfs.namenode.audit.loggers	default	1
543	1	ssl.server.keystore.password		1
544	1	dfs.client.write.byte-array-manager.count-reset-time-period-ms	10000	1
545	1	dfs.namenode.snapshot.capture.openfiles	false	1
546	1	dfs.qjournal.queued-edits.limit.mb	10	1
547	1	ssl.server.keystore.keypassword		1
548	1	dfs.http.policy	HTTP_ONLY	1
549	1	dfs.balancer.max-size-to-move	10737418240	1
550	1	dfs.datanode.sync.behind.writes.in.background	false	1
551	1	dfs.namenode.safemode.min.datanodes	0	1
552	1	dfs.client.file-block-storage-locations.num-threads	10	1
553	1	dfs.datanode.kerberos.principal		1
554	1	dfs.namenode.secondary.https-address	0.0.0.0:50091	1
555	1	dfs.namenode.metrics.logger.period.seconds	600	1
556	1	dfs.namenode.snapshot.skip.capture.accesstime-only-change	false	1
557	1	dfs.block.access.token.lifetime	600	1
558	1	dfs.web1.enabled	true	1
559	1	dfs.web1.socket.read-timeout	60s	1
560	1	dfs.namenode.delegation.token.max-lifetime	604800000	1
561	1	dfs.datanode.drop.cache.behind.writes	false	1
562	1	dfs.namenode.kerberos.principal		1
563	1	dfs.namenode.avoid.write.stale.datanode	false	1
564	1	dfs.namenode.replication.considerLoad.factor	2	1
565	1	dfs.namenode.num.extra.edits.retained	1000000	1
566	1	ssl.server.keystore.location		1
567	1	dfs.namenode.edekcacheloader.initial.delay.ms	3000	1
568	1	dfs.client.mmap.cache.size	256	1
569	1	dfs.client.max.block.acquire.failures	3	1
570	1	dfs.ha.zkfc.nn.http.timeout.ms	20000	1
571	1	dfs.namenode.available-space-block-placement-policy.balanced-space-preference-fraction	0.6	1
572	1	dfs.federation.router.heartbeat.interval	5000	1
573	1	nfs.keytab.file		1
574	1	dfs.client.datanode-restart.timeout	30	1
575	1	dfs.client.retry.interval-ms.get-last-block-length	4000	1
576	1	dfs.client-write-packet-size	65536	1
577	1	dfs.namenode.checkpoint.txns	1000000	1
578	1	dfs.client.failover.proxy.provider		1
579	1	dfs.journalnode.edits.dir	/tmp/hadoop/dfs/journalnode/	1
580	1	dfs.namenode.list.openfiles.num.responses	1000	1
581	1	dfs.cachereport.intervalMsec	10000	1
582	1	dfs.ha.tail-edits.rolledits.timeout	60	1
583	1	dfs.federation.router.admin.handler.count	1	1
584	1	ssl.server.truststore.password		1
585	1	dfs.namenode.kerberos.principal.pattern	*	1
586	1	dfs.web1.socket.connect-timeout	60s	1
587	1	dfs.namenode.replication.max-streams	2	1
588	1	dfs.namenode.keytab.file		1
589	1	nfs.allow.insecure.ports	true	1
590	1	dfs.http.client.retry.policy.enabled	false	1
591	1	dfs.quota.by.storage.type.enabled	true	1
592	1	dfs.federation.router.admin.enable	true	1
593	1	dfs.client.failover.connection.retries.on.timeouts	0	1
594	1	dfs.namenode.replication.work.multiplier.per.iteration	2	1
595	1	dfs.balancer.keytab.file		1
596	1	dfs.client.retry.times.get-last-block-length	3	1
597	1	dfs.internal.nameservices		1
598	1	dfs.image.compression.codec	org.apache.hadoop.io.compress.DefaultCodec	1
599	1	dfs.client.read.shortcircuit.streams.cache.size	256	1
600	1	dfs.namenode.upgrade.domain.factor	${dfs.replication}	1
601	1	dfs.qjournal.finalize-segment.timeout.ms	120000	1
602	1	dfs.namenode.resource.checked.volumes		1
603	1	dfs.datanode.socket.write.timeout	480000	1
604	1	dfs.namenode.accesstime.precision	3600000	1
605	1	dfs.namenode.fs-limits.max-xattrs-per-inode	32	1
606	1	dfs.namenode.lifeline.rpc-bind-host		1
607	1	dfs.image.transfer.timeout	60000	1
608	1	nfs.wtmax	1048576	1
609	1	dfs.nameservice.id		1
610	1	dfs.federation.router.rpc-address	0.0.0.0:8888	1
611	1	dfs.namenode.support.allow.format	true	1
612	1	dfs.secondary.namenode.kerberos.internal.spnego.principal	${dfs.web.authentication.kerberos.principal}	1
613	1	dfs.stream-buffer-size	4096	1
614	1	dfs.namenode.invalidate.work.pct.per.iteration	0.32f	1
615	1	dfs.content-summary.limit	5000	1
616	1	dfs.datanode.outliers.report.interval	1800000	1
617	1	dfs.namenode.top.enabled	true	1
618	1	dfs.federation.router.default.nameserviceId		1
619	1	dfs.federation.router.handler.queue.size	100	1
620	1	dfs.federation.router.http-address	0.0.0.0:50071	1
621	1	dfs.https.port		1
622	1	dfs.client.cached.conn.retry	3	1
623	1	dfs.encrypt.data.transfer.algorithm		1
624	1	dfs.namenode.list.encryption.zones.num.responses	100	1
625	1	dfs.client.key.provider.cache.expiry	864000000	1
626	1	dfs.namenode.inode.attributes.provider.class		1
627	1	dfs.federation.router.file.resolver.client.class	org.apache.hadoop.1.server.federation.MockResolver	1
628	1	dfs.datanode.fsdataset.factory		1
629	1	dfs.namenode.decommission.interval	30	1
630	1	dfs.namenode.path.based.cache.refresh.interval.ms	30000	1
631	1	dfs.namenode.fs-limits.max-directory-items	1048576	1
632	1	dfs.block.replicator.classname	org.apache.hadoop.1.server.blockmanagement.BlockPlacementPolicyDefault	1
633	1	dfs.ha.log-roll.period	120	1
634	1	dfs.pipeline.ecn	false	1
635	1	dfs.user.home.dir.prefix	/user	1
636	1	dfs.ha.namenode.id		1
637	1	dfs.namenode.inotify.max.events.per.rpc	1000	1
638	1	ssl.server.truststore.location		1
639	1	dfs.xframe.enabled	true	1
640	1	dfs.datanode.transfer.socket.recv.buffer.size	0	1
641	1	dfs.namenode.fs-limits.max-xattr-size	16384	1
642	1	dfs.trustedchannel.resolver.class		1
643	1	dfs.datanode.http.address	0.0.0.0:50075	1
644	1	dfs.namenode.blocks.per.postponedblocks.rescan	10000	1
645	1	dfs.http.client.failover.sleep.max.millis	15000	1
646	1	dfs.data.transfer.saslproperties.resolver.class		1
647	1	dfs.web.authentication.filter	org.apache.hadoop.1.web.AuthFilter	1
648	1	dfs.lock.suppress.warning.interval	10s	1
649	1	dfs.balancer.moverThreads	1000	1
650	1	dfs.namenode.maintenance.replication.min	1	1
651	1	dfs.client.retry.max.attempts	10	1
652	1	dfs.web1.ugi.expire.after.access	600000	1
653	1	dfs.namenode.max.op.size	52428800	1
654	1	dfs.federation.router.metrics.enable	true	1
655	1	dfs.datanode.restart.replica.expiration	50	1
656	1	dfs.namenode.edits.dir.minimum	1	1
657	1	nfs.mountd.port	4242	1
658	1	dfs.client.test.drop.namenode.response.number	0	1
659	1	dfs.web1.netty.low.watermark	32768	1
660	1	dfs.namenode.lifeline.rpc-address		1
661	1	dfs.web1.netty.high.watermark	65535	1
662	1	dfs.secondary.namenode.kerberos.principal		1
663	1	dfs.namenode.legacy-oiv-image.dir		1
664	1	dfs.datanode.balance.max.concurrent.moves	50	1
665	1	dfs.namenode.backup.dnrpc-address		1
666	1	dfs.namenode.num.checkpoints.retained	2	1
667	1	dfs.web1.oauth2.access.token.provider		1
668	1	dfs.client.mmap.retry.timeout.ms	300000	1
669	1	dfs.namenode.fslock.fair	true	1
670	1	dfs.permissions.enabled	true	1
671	1	dfs.blockreport.split.threshold	1000000	1
672	1	dfs.datanode.balance.bandwidthPerSec	10m	1
673	1	dfs.block.scanner.volume.bytes.per.second	1048576	1
674	1	dfs.client.read.shortcircuit.buffer.size	1048576	1
675	1	dfs.http.port		1
676	1	dfs.default.chunk.view.size	32768	1
677	1	dfs.qjournal.accept-recovery.timeout.ms	120000	1
678	1	dfs.domain.socket.path		1
679	1	dfs.namenode.handler.count	10	1
680	1	dfs.namenode.decommission.blocks.per.interval	500000	1
681	1	dfs.image.transfer.bandwidthPerSec	0	1
682	1	dfs.qjournal.write-txns.timeout.ms	20000	1
683	1	dfs.namenode.read-lock-reporting-threshold-ms	5000	1
684	1	dfs.federation.router.monitor.namenode		1
685	1	dfs.datanode.failed.volumes.tolerated	0	1
686	1	dfs.client.block.write.replace-datanode-on-failure.min-replication	0	1
687	1	dfs.blocksize	134217728	1
688	1	dfs.namenode.write.stale.datanode.ratio	0.5f	1
689	1	dfs.encrypt.data.transfer	false	1
690	1	dfs.namenode.edits.dir.required		1
691	1	dfs.datanode.shared.file.descriptor.paths	/dev/shm,/tmp	1
692	1	dfs.client.failover.max.attempts	15	1
693	1	dfs.namenode.inode.attributes.provider.bypass.users		1
694	1	dfs.client.read.shortcircuit.streams.cache.expiry.ms	300000	1
695	1	dfs.balancer.max-no-move-interval	60000	1
696	1	dfs.web1.oauth2.enabled	false	1
697	1	dfs.namenode.servicerpc-address		1
698	1	dfs.journalnode.kerberos.internal.spnego.principal		1
699	1	dfs.federation.router.connection.pool.clean.ms	60000	1
700	1	dfs.client.read.shortcircuit.skip.checksum	false	1
701	1	dfs.namenode.quota.init-threads	4	1
702	1	dfs.web1.oauth2.client.id		1
703	1	dfs.federation.router.monitor.localnamenode.enable	true	1
704	1	dfs.datanode.metrics.logger.period.seconds	600	1
705	1	dfs.web1.acl.provider.permission.pattern	^(default:)?(user|group|mask|other):[[A-Za-z_][A-Za-z0-9._-]]*:([rwx-]{3})?(,(default:)?(user|group|mask|other):[[A-Za-z_][A-Za-z0-9._-]]*:([rwx-]{3})?)*$	1
706	1	dfs.datanode.use.datanode.hostname	false	1
707	1	dfs.datanode.block.id.layout.upgrade.threads	12	1
708	1	dfs.client.context	default	1
709	1	dfs.balancer.address	0.0.0.0:0	1
710	1	dfs.namenode.lock.detailed-metrics.enabled	false	1
711	1	dfs.namenode.delegation.token.renew-interval	86400000	1
712	1	dfs.datanode.fsdataset.volume.choosing.policy		1
713	1	dfs.namenode.rpc-address		1
714	1	dfs.web.authentication.kerberos.principal		1
715	1	dfs.reformat.disabled	false	1
716	1	dfs.blockreport.intervalMsec	21600000	1
717	1	dfs.client.write.max-packets-in-flight	80	1
718	1	dfs.datanode.oob.timeout-ms	1500,0,0,0	1
719	1	dfs.https.server.keystore.resource	ssl-server.xml	1
720	1	dfs.namenode.kerberos.internal.spnego.principal	${dfs.web.authentication.kerberos.principal}	1
721	1	dfs.namenode.rpc-bind-host		1
722	1	dfs.namenode.edits.journal-plugin		1
723	1	dfs.namenode.edekcacheloader.interval.ms	1000	1
724	1	dfs.datanode.dns.interface	default	1
725	1	dfs.namenode.plugins		1
726	1	dfs.client.failover.connection.retries	0	1
727	1	dfs.namenode.top.window.num.buckets	10	1
728	1	dfs.http.client.failover.max.attempts	15	1
729	1	dfs.datanode.max.locked.memory	0	1
730	1	dfs.namenode.retrycache.expirytime.millis	600000	1
731	1	dfs.federation.router.store.connection.test	60000	1
732	1	dfs.client.block.write.replace-datanode-on-failure.best-effort	false	1
733	1	dfs.datanode.scan.period.hours	504	1
734	1	dfs.client.block.write.locateFollowingBlock.retries	5	1
735	1	dfs.datanode.disk.check.min.gap	15m	1
736	1	dfs.namenode.fs-limits.max-component-length	255	1
737	1	dfs.web1.rest-csrf.enabled	false	1
738	1	dfs.ha.fencing.methods		1
739	1	dfs.namenode.enable.retrycache	true	1
740	1	dfs.datanode.du.reserved	0	1
741	1	dfs.datanode.ipc.address	0.0.0.0:50020	1
742	1	dfs.client.block.write.replace-datanode-on-failure.policy	DEFAULT	1
743	1	dfs.namenode.path.based.cache.retry.interval.ms	30000	1
744	1	dfs.block.misreplication.processing.limit	10000	1
745	1	dfs.data.transfer.client.tcpnodelay	true	1
746	1	dfs.ha.tail-edits.period	60	1
747	1	dfs.client.local.interfaces		1
748	1	dfs.client.retry.policy.enabled	false	1
749	1	dfs.namenode.https-bind-host		1
750	1	dfs.namenode.safemode.replication.min		1
751	1	dfs.namenode.edits.dir	${dfs.namenode.name.dir}	1
752	1	dfs.namenode.shared.edits.dir		1
753	1	dfs.qjournal.prepare-recovery.timeout.ms	120000	1
754	1	dfs.datanode.transferTo.allowed	true	1
755	1	dfs.federation.router.store.enable	true	1
756	1	dfs.namenode.decommission.max.concurrent.tracked.nodes	100	1
757	1	dfs.namenode.name.dir.restore	false	1
758	1	dfs.namenode.full.block.report.lease.length.ms	300000	1
759	1	dfs.namenode.secondary.http-address	0.0.0.0:50090	1
760	1	dfs.datanode.lifeline.interval.seconds		1
761	1	dfs.namenode.delegation.token.always-use	false	1
762	1	dfs.support.append	true	1
763	1	dfs.datanode.socket.reuse.keepalive	4000	1
764	1	dfs.namenode.checkpoint.period	3600	1
765	1	dfs.ha.automatic-failover.enabled	false	1
766	5	cluster.name	my-application	elasticsearch
767	5	node.name	node-1	elasticsearch
768	5	node.attr.rack	r1	elasticsearch
769	5	path.data	/var/lib/elasticsearch	elasticsearch
770	5	path.logs	/var/log/elasticsearch	elasticsearch
771	5	bootstrap.memory_lock	TRUE	elasticsearch
772	5	network.host	192.168.0.1	elasticsearch
773	5	http.port	9200	elasticsearch
774	5	discovery.zen.ping.unicast.hosts	"[""host1"",""host2""]"	elasticsearch
775	5	discovery.zen.minimum_master_nodes		elasticsearch
776	5	gateway.recover_after_nodes	3	elasticsearch
777	5	action.destructive_requires_name	TRUE	elasticsearch
778	5	node.rack	${RACK_ENV_VAR}	elasticsearch
779	5	node.master		elasticsearch
780	5	node.data		elasticsearch
781	5	node.max_local_storage_nodes		elasticsearch
782	5	index.number_of_shards		elasticsearch
783	5	index.number_of_replicas		elasticsearch
784	5	path.conf		elasticsearch
785	5	path.work		elasticsearch
786	5	path.plugins		elasticsearch
787	5	plugin.mandatory	mapper-attachments,lang-groovy	elasticsearch
788	5	bootstrap.mlockall	TRUE	elasticsearch
789	5	network.bind_host	192.168.0.1	elasticsearch
790	5	network.publish_host	192.168.0.1	elasticsearch
791	5	transport.tcp.port	9300	elasticsearch
792	5	transport.tcp.compress	TRUE	elasticsearch
793	5	http.max_content_length	100mb	elasticsearch
794	5	http.enabled	FALSE	elasticsearch
795	5	gateway.type	local	elasticsearch
796	5	gateway.recover_after_time	10m	elasticsearch
797	5	gateway.expected_nodes	2	elasticsearch
798	5	action.auto_create_index	FALSE	elasticsearch
799	5	action.disable_close_all_indices	TRUE	elasticsearch
800	5	action.disable_delete_all_indices	TRUE	elasticsearch
801	5	action.disable_shutdown	TRUE	elasticsearch
802	5	indices.recovery.max_bytes_per_sec	100mb	elasticsearch
803	5	indices.recovery.concurrent_streams	5	elasticsearch
804	5	discovery.zen.ping.timeout	3s	elasticsearch
805	5	discovery.zen.ping.multicast.enabled	FALSE	elasticsearch
806	5	index.search.slowlog.threshold.query.warn	10s	elasticsearch
807	5	index.search.slowlog.threshold.query.info	5s	elasticsearch
808	5	index.search.slowlog.threshold.query.debug	2s	elasticsearch
809	5	index.search.slowlog.threshold.query.trace	500ms	elasticsearch
810	5	index.search.slowlog.threshold.fetch.warn	1s	elasticsearch
811	5	index.search.slowlog.threshold.fetch.info	800ms	elasticsearch
812	5	index.search.slowlog.threshold.fetch.debug	500ms	elasticsearch
813	5	index.search.slowlog.threshold.fetch.trace	200ms	elasticsearch
814	5	index.indexing.slowlog.threshold.index.warn	10s	elasticsearch
815	5	index.indexing.slowlog.threshold.index.info	5s	elasticsearch
816	5	index.indexing.slowlog.threshold.index.debug	2s	elasticsearch
817	5	index.indexing.slowlog.threshold.index.trace	500ms	elasticsearch
818	5	monitor.jvm.gc.ParNew.warn	1000ms	elasticsearch
819	5	monitor.jvm.gc.ParNew.info	700ms	elasticsearch
820	5	monitor.jvm.gc.ParNew.debug	400ms	elasticsearch
821	5	monitor.jvm.gc.ConcurrentMarkSweep.warn	10s	elasticsearch
822	5	monitor.jvm.gc.ConcurrentMarkSweep.info	5s	elasticsearch
823	5	monitor.jvm.gc.ConcurrentMarkSweep.debug	2s	elasticsearch
824	1	zookeeper.recovery.retry.maxsleeptime	60000	hbase
825	1	hbase.rs.cacheblocksonwrite	false	hbase
826	1	hbase.master.mob.ttl.cleaner.period	86400	hbase
827	1	hbase.master.loadbalance.bytable	false	hbase
828	1	hbase.master.port	16000	hbase
829	1	hbase.client.localityCheck.threadPoolSize	2	hbase
830	1	hbase.client.pause.cqtbe		hbase
831	1	hbase.master.hfilecleaner.plugins	org.apache.hadoop.hbase.master.cleaner.TimeToLiveHFileCleaner	hbase
832	1	hbase.dfs.client.read.shortcircuit.buffer.size	131072	hbase
833	1	hbase.client.operation.timeout	1200000	hbase
834	1	hbase.auth.token.max.lifetime	604800000	hbase
835	1	hbase.regionserver.regionSplitLimit	1000	hbase
836	1	hbase.regionserver.dns.nameserver	default	hbase
837	1	hbase.client.scanner.timeout.period	60000	hbase
838	1	io.storefile.bloom.block.size	131072	hbase
839	1	hbase.status.multicast.address.ip	226.1.1.3	hbase
840	1	hbase.master.logcleaner.plugins	org.apache.hadoop.hbase.master.cleaner.TimeToLiveLogCleaner,org.apache.hadoop.hbase.master.cleaner.TimeToLiveProcedureWALCleaner	hbase
841	1	hbase.balancer.period	300000	hbase
842	1	hbase.rootdir	${hbase.tmp.dir}/hbase	hbase
843	1	hbase.coprocessor.enabled	true	hbase
844	1	hfile.format.version	3	hbase
845	1	hbase.zookeeper.dns.nameserver	default	hbase
846	1	hbase.hregion.majorcompaction	604800000	hbase
847	1	hbase.hstore.compaction.min	3	hbase
848	1	hbase.security.authentication	simple	hbase
849	1	hbase.dynamic.jars.dir	${hbase.rootdir}/lib	hbase
850	1	hbase.status.multicast.address.port	16100	hbase
851	1	hbase.data.umask.enable	false	hbase
852	1	hbase.snapshot.enabled	true	hbase
853	1	hbase.master.balancer.maxRitPercent	1	hbase
854	1	hbase.regionserver.checksum.verify	true	hbase
855	1	hbase.region.replica.replication.enabled	false	hbase
856	1	hbase.hstore.blockingStoreFiles	16	hbase
857	1	zookeeper.session.timeout	90000	hbase
858	1	hbase.cells.scanned.per.heartbeat.check	10000	hbase
859	1	hbase.rest.readonly	false	hbase
860	1	hbase.client.perserver.requests.threshold	2147483647	hbase
861	1	hbase.mob.compaction.batch.size	100	hbase
862	1	hbase.auth.key.update.interval	86400000	hbase
863	1	hbase.offpeak.start.hour	-1	hbase
864	1	hbase.ipc.server.callqueue.handler.factor	0.1	hbase
865	1	hbase.regionserver.logroll.period	3600000	hbase
866	1	hbase.rest.support.proxyuser	false	hbase
867	1	hbase.regionserver.handler.abort.on.error.percent	0.5	hbase
868	1	hbase.master.fileSplitTimeout	600000	hbase
869	1	hbase.hstore.compactionThreshold	3	hbase
870	1	hbase.status.publisher.class	org.apache.hadoop.hbase.master.ClusterStatusPublisher$MulticastPublisher	hbase
871	1	hbase.hstore.bytes.per.checksum	16384	hbase
872	1	hbase.hstore.checksum.algorithm	CRC32C	hbase
873	1	hbase.rest.csrf.enabled	false	hbase
874	1	hbase.hregion.memstore.block.multiplier	4	hbase
875	1	hbase.snapshot.restore.failsafe.name	hbase-failsafe-{snapshot.name}-{restore.timestamp}	hbase
876	1	hbase.client.scanner.max.result.size	2097152	hbase
877	1	hbase.regionserver.majorcompaction.pagecache.drop	true	hbase
878	1	hbase.procedure.master.classes		hbase
879	1	hbase.coordinated.state.manager.class	org.apache.hadoop.hbase.coordination.ZkCoordinatedStateManager	hbase
880	1	hbase.status.published	false	hbase
881	1	hbase.server.versionfile.writeattempts	3	hbase
882	1	hbase.hstore.time.to.purge.deletes	0	hbase
883	1	hbase.client.retries.number	15	hbase
884	1	hbase.ipc.client.fallback-to-simple-auth-allowed	false	hbase
885	1	hbase.defaults.for.version	@@@VERSION@@@	hbase
886	1	hbase.regionserver.thread.compaction.throttle	2684354560	hbase
887	1	hbase.cluster.distributed	false	hbase
888	1	hbase.ipc.server.fallback-to-simple-auth-allowed	false	hbase
889	1	hbase.regions.slop	0.001	hbase
890	1	hbase.hstore.compaction.ratio	1.2F	hbase
891	1	hbase.regionserver.minorcompaction.pagecache.drop	true	hbase
892	1	hbase.master.normalizer.class	org.apache.hadoop.hbase.master.normalizer.SimpleRegionNormalizer	hbase
893	1	hbase.regionserver.hlog.writer.impl	org.apache.hadoop.hbase.regionserver.wal.ProtobufLogWriter	hbase
894	1	hbase.zookeeper.leaderport	3888	hbase
895	1	hbase.client.max.perregion.tasks	1	hbase
896	1	hbase.thrift.minWorkerThreads	16	hbase
897	1	hbase.http.filter.initializers	org.apache.hadoop.hbase.http.lib.StaticUserWebFilter	hbase
898	1	hbase.systemtables.compacting.memstore.type	NONE	hbase
899	1	dfs.client.read.shortcircuit	false	hbase
900	1	hbase.normalizer.min.region.count	3	hbase
901	1	hbase.replication.rpc.codec	org.apache.hadoop.hbase.codec.KeyValueCodecWithTags	hbase
902	1	hbase.client.max.perserver.tasks	2	hbase
903	1	hbase.snapshot.region.timeout	300000	hbase
904	1	hbase.hstore.compaction.kv.max	10	hbase
905	1	hbase.mob.compactor.class	org.apache.hadoop.hbase.mob.compactions.PartitionedMobCompactor	hbase
906	1	hbase.hregion.max.filesize	10737418240	hbase
907	1	hbase.server.scanner.max.result.size	104857600	hbase
908	1	hbase.rest.threads.min	2	hbase
909	1	hbase.storescanner.parallel.seek.threads	10	hbase
910	1	hbase.status.listener.class	org.apache.hadoop.hbase.client.ClusterStatusListener$MulticastListener	hbase
911	1	hbase.hregion.preclose.flush.size	5242880	hbase
912	1	hbase.http.staticuser.user	dr.stack	hbase
913	1	hbase.regionserver.region.split.policy	org.apache.hadoop.hbase.regionserver.SteppingSplitPolicy	hbase
914	1	hbase.client.keyvalue.maxsize	10485760	hbase
915	1	hbase.client.scanner.caching	2147483647	hbase
916	1	hbase.mob.cache.evict.period	3600	hbase
917	1	hbase.server.keyvalue.maxsize	10485760	hbase
918	1	hbase.regionserver.optionalcacheflushinterval	3600000	hbase
919	1	hbase.rpc.timeout	60000	hbase
920	1	hbase.table.max.rowsize	1073741824	hbase
921	1	hbase.thrift.maxQueuedRequests	1000	hbase
922	1	hbase.zookeeper.property.clientPort	2181	hbase
923	1	hbase.hstore.blockingWaitTime	90000	hbase
924	1	hbase.server.thread.wakefrequency	10000	hbase
925	1	hbase.zookeeper.property.syncLimit	5	hbase
926	1	hbase.zookeeper.property.dataDir	${hbase.tmp.dir}/zookeeper	hbase
927	1	hbase.regionserver.hostname		hbase
928	1	hbase.client.max.total.tasks	100	hbase
929	1	hbase.regionserver.info.port.auto	false	hbase
930	1	hbase.regionserver.keytab.file		hbase
931	1	hbase.storescanner.parallel.seek.enable	false	hbase
932	1	hbase.mob.file.cache.size	1000	hbase
933	1	hbase.local.dir	${hbase.tmp.dir}/local/	hbase
934	1	hbase.regionserver.global.memstore.size.lower.limit		hbase
935	1	hbase.master.keytab.file		hbase
936	1	hbase.zookeeper.quorum	localhost	hbase
937	1	hbase.hstore.compaction.max	10	hbase
938	1	hbase.rpc.shortoperation.timeout	10000	hbase
939	1	hbase.thrift.maxWorkerThreads	1000	hbase
940	1	hbase.client.write.buffer	2097152	hbase
941	1	hbase.data.umask	0	hbase
942	1	hbase.bucketcache.bucket.sizes		hbase
943	1	hbase.regionserver.kerberos.principal		hbase
944	1	hbase.coprocessor.user.enabled	true	hbase
945	1	hbase.hregion.memstore.mslab.enabled	true	hbase
946	1	hbase.hstore.flusher.count	2	hbase
947	1	hbase.regionserver.hostname.disable.master.reversedns	false	hbase
948	1	hbase.column.max.version	1	hbase
949	1	hbase.offpeak.end.hour	-1	hbase
950	1	hbase.hstore.compaction.ratio.offpeak	5.0F	hbase
951	1	hbase.regionserver.thrift.framed	false	hbase
952	1	hbase.snapshot.restore.take.failsafe.snapshot	true	hbase
953	1	dfs.domain.socket.path	none	hbase
954	1	hbase.security.visibility.mutations.checkauths	false	hbase
955	1	hbase.bucketcache.size		hbase
956	1	hbase.regionserver.dns.interface	default	hbase
957	1	hbase.master.loadbalancer.class	org.apache.hadoop.hbase.master.balancer.StochasticLoadBalancer	hbase
958	1	hbase.hregion.majorcompaction.jitter	0.5	hbase
959	1	hbase.ipc.client.tcpnodelay	true	hbase
960	1	hbase.wal.dir.perms	700	hbase
961	1	hbase.master.kerberos.principal		hbase
962	1	hbase.coprocessor.abortonerror	true	hbase
963	1	hbase.regionserver.msginterval	3000	hbase
964	1	hbase.tmp.dir	${java.io.tmpdir}/hbase-${user.name}	hbase
965	1	hbase.master.logcleaner.ttl	600000	hbase
966	1	hbase.superuser		hbase
967	1	hbase.coprocessor.region.classes		hbase
968	1	hbase.regionserver.handler.count	30	hbase
969	1	hbase.regionserver.port	16020	hbase
970	1	hbase.regionserver.compaction.enabled	true	hbase
971	1	hbase.defaults.for.version.skip	false	hbase
972	1	hbase.rpc.rows.warning.threshold	5000	hbase
973	1	hbase.coprocessor.master.classes		hbase
974	1	hfile.block.cache.size	0.4	hbase
975	1	hbase.zookeeper.dns.interface	default	hbase
976	1	hbase.mob.compaction.mergeable.threshold	1342177280	hbase
977	1	hbase.display.keys	true	hbase
978	1	hbase.server.compactchecker.interval.multiplier	1000	hbase
979	1	hbase.mob.delfile.max.count	3	hbase
980	1	zookeeper.znode.acl.parent	acl	hbase
981	1	hbase.zookeeper.property.initLimit	10	hbase
982	1	hbase.lease.recovery.dfs.timeout	64000	hbase
983	1	hbase.regionserver.info.port	16030	hbase
984	1	hbase.regionserver.thrift.compact	false	hbase
985	1	hbase.table.lock.enable	true	hbase
986	1	hbase.snapshot.master.timeout.millis	300000	hbase
987	1	hbase.replication.source.maxthreads	10	hbase
988	1	zookeeper.znode.parent	/1	hbase
989	1	hbase.master.info.port	16010	hbase
990	1	hbase.rest.port	8080	hbase
991	1	hbase.rest-csrf.browser-useragents-regex	^Mozilla.*,^Opera.*	hbase
992	1	hbase.regionserver.storefile.refresh.period	0	hbase
993	1	hbase.mob.compaction.threads.max	1	hbase
994	1	hbase.master.wait.on.service.seconds	30	hbase
995	1	hbase.hstore.compaction.min.size	134217728	hbase
996	1	hbase.ipc.server.callqueue.scan.ratio	0	hbase
997	1	hbase.hstore.compaction.max.size	9.22337203685478E+018	hbase
998	1	hfile.block.bloom.cacheonwrite	false	hbase
999	1	hbase.mob.compaction.chore.period	604800	hbase
1000	1	hbase.master.infoserver.redirect	true	hbase
1001	1	hbase.client.pause	100	hbase
1002	1	hbase.rest.threads.max	100	hbase
1003	1	hbase.master.info.bindAddress	0.0.0.0	hbase
1004	1	hbase.hregion.percolumnfamilyflush.size.lower.bound.min	16777216	hbase
1005	1	hbase.lease.recovery.timeout	900000	hbase
1006	1	hbase.regionserver.thrift.framed.max_frame_size_in_mb	2	hbase
1007	1	hbase.zookeeper.property.maxClientCnxns	300	hbase
1008	1	hfile.block.index.cacheonwrite	false	hbase
1009	1	hbase.mob.cache.evict.remain.ratio	0.5f	hbase
1010	1	hbase.ipc.server.callqueue.read.ratio	0	hbase
1011	1	hbase.hregion.memstore.flush.size	134217728	hbase
1012	1	hbase.regionserver.global.memstore.size		hbase
1013	1	hbase.normalizer.period	300000	hbase
1014	1	hbase.master.procedurewalcleaner.ttl	604800000	hbase
1015	1	hbase.regionserver.logroll.errors.tolerated	2	hbase
1016	1	hbase.rest.filter.classes	org.apache.hadoop.hbase.rest.filter.GzipFilter	hbase
1017	1	hadoop.policy.file	hbase-policy.xml	hbase
1018	1	hbase.bulkload.retries.number	10	hbase
1019	1	hbase.security.exec.permission.checks	false	hbase
1020	1	hbase.rootdir.perms	700	hbase
1021	1	hbase.regionserver.hlog.reader.impl	org.apache.hadoop.hbase.regionserver.wal.ProtobufLogReader	hbase
1022	1	hfile.index.block.max.size	131072	hbase
1023	1	hbase.procedure.regionserver.classes		hbase
1024	1	hbase.http.max.threads	16	hbase
1025	1	hbase.regionserver.info.bindAddress	0.0.0.0	hbase
1026	1	hbase.zookeeper.peerport	2888	hbase
1027	1	hbase.bucketcache.ioengine		hbase
1028	2	mapreduce.jobtracker.address	local	mapred
1029	2	mapreduce.job.counters.limit	120	mapred
1030	2	mapreduce.job.speculative.minimum-allowed-tasks	10	mapred
1031	2	mapreduce.jobhistory.recovery.store.class	org.apache.hadoop.mapreduce.v2.hs.HistoryServerFileSystemStateStoreService	mapred
1032	2	mapreduce.task.combine.progress.records	10000	mapred
1033	2	mapreduce.jobhistory.client.thread-count	10	mapred
1034	2	mapred.child.java.opts	-Xmx200m	mapred
1035	2	yarn.app.mapreduce.am.containerlauncher.threadpool-initial-size	10	mapred
1036	2	mapreduce.shuffle.transfer.buffer.size	131072	mapred
1037	2	yarn.app.mapreduce.am.job.committer.cancel-timeout	60000	mapred
1038	2	yarn.app.mapreduce.client-am.ipc.max-retries-on-timeouts	3	mapred
1039	2	mapreduce.job.emit-timeline-data	false	mapred
1040	2	mapreduce.job.end-notification.retry.attempts	0	mapred
1041	2	mapreduce.job.am.node-label-expression		mapred
1042	2	mapreduce.job.reduces	1	mapred
1043	2	mapreduce.cluster.acls.enabled	false	mapred
1044	2	mapreduce.job.acl-modify-job	 	mapred
1045	2	mapreduce.task.profile.reduces	0-2	mapred
1046	2	mapreduce.job.ubertask.maxmaps	9	mapred
1047	2	mapreduce.input.fileinputformat.list-status.num-threads	1	mapred
1048	2	mapreduce.app-submission.cross-platform	false	mapred
1049	2	mapreduce.job.classloader.system.classes		mapred
1050	2	mapreduce.job.reducer.preempt.delay.sec	0	mapred
1051	2	mapreduce.map.output.compress.codec	org.apache.hadoop.io.compress.DefaultCodec	mapred
1052	2	mapreduce.jobhistory.cleaner.interval-ms	86400000	mapred
1053	2	mapreduce.shuffle.listen.queue.size	128	mapred
1054	2	mapreduce.jobhistory.intermediate-done-dir	${yarn.app.mapreduce.am.staging-dir}/history/done_intermediate	mapred
1055	2	mapreduce.client.libjars.wildcard	true	mapred
1056	2	mapreduce.input.fileinputformat.split.minsize	0	mapred
1057	2	mapreduce.jobtracker.system.dir	${hadoop.tmp.dir}/mapred/system	mapred
1058	2	mapreduce.map.node-label-expression		mapred
1059	2	mapreduce.job.end-notification.max.attempts	5	mapred
1060	2	mapreduce.reduce.shuffle.input.buffer.percent	0.7	mapred
1061	2	mapreduce.reduce.markreset.buffer.percent	0	mapred
1062	2	mapreduce.reduce.speculative	true	mapred
1063	2	mapreduce.map.maxattempts	4	mapred
1064	2	mapreduce.reduce.shuffle.read.timeout	180000	mapred
1065	2	yarn.app.mapreduce.am.admin.user.env		mapred
1066	2	mapreduce.jobhistory.recovery.store.fs.uri	${hadoop.tmp.dir}/mapred/history/recoverystore	mapred
1067	2	mapreduce.jobhistory.webapp.rest-csrf.enabled	false	mapred
1068	2	mapreduce.ifile.readahead.bytes	4194304	mapred
1069	2	mapreduce.job.maps	2	mapred
1070	2	mapreduce.cluster.local.dir	${hadoop.tmp.dir}/mapred/local	mapred
1071	2	mapreduce.job.ubertask.enable	false	mapred
1072	2	mapreduce.reduce.skip.maxgroups	0	mapred
1073	2	mapreduce.job.complete.cancel.delegation.tokens	true	mapred
1074	2	mapreduce.local.clientfactory.class.name	org.apache.hadoop.mapred.LocalClientFactory	mapred
1075	2	mapreduce.shuffle.connection-keep-alive.timeout	5	mapred
1076	2	mapreduce.am.max-attempts	2	mapred
1077	2	mapreduce.reduce.shuffle.parallelcopies	5	mapred
1078	2	mapreduce.job.map.output.collector.class	org.apache.hadoop.mapred.MapTask$MapOutputBuffer	mapred
1079	2	mapreduce.job.finish-when-all-reducers-done	false	mapred
1080	2	mapreduce.shuffle.max.threads	0	mapred
1081	2	mapreduce.jobhistory.done-dir	${yarn.app.mapreduce.am.staging-dir}/history/done	mapred
1082	2	mapreduce.reduce.node-label-expression		mapred
1083	2	mapreduce.reduce.shuffle.connect.timeout	180000	mapred
1084	2	yarn.app.mapreduce.client.job.max-retries	3	mapred
1085	2	mapreduce.jobhistory.cleaner.enable	true	mapred
1086	2	mapreduce.jobhistory.webapp.rest-csrf.methods-to-ignore	GET,OPTIONS,HEAD	mapred
1087	2	yarn.app.mapreduce.am.container.log.backups	0	mapred
1088	2	mapreduce.job.max.map	-1	mapred
1089	2	yarn.app.mapreduce.shuffle.log.backups	0	mapred
1090	2	yarn.app.mapreduce.am.container.log.limit.kb	0	mapred
1091	2	mapreduce.cluster.temp.dir	${hadoop.tmp.dir}/mapred/temp	mapred
1092	2	mapreduce.reduce.maxattempts	4	mapred
1093	2	mapreduce.client.submit.file.replication	10	mapred
1094	2	mapreduce.shuffle.port	13562	mapred
1095	2	mapreduce.job.ubertask.maxreduces	1	mapred
1096	2	mapreduce.shuffle.transferTo.allowed		mapred
1097	2	mapreduce.job.speculative.speculative-cap-total-tasks	0.01	mapred
1098	2	yarn.app.mapreduce.client.job.retry-interval	2000	mapred
1099	2	mapreduce.job.speculative.slowtaskthreshold	1	mapred
1100	2	mapreduce.job.ubertask.maxbytes		mapred
1101	2	mapreduce.task.skip.start.attempts	2	mapred
1102	2	mapred.child.env		mapred
1103	2	mapreduce.task.files.preserve.failedtasks	false	mapred
1104	2	mapreduce.job.reduce.slowstart.completedmaps	0.05	mapred
1105	2	mapreduce.jobhistory.minicluster.fixed.ports	false	mapred
1106	2	mapreduce.reduce.skip.proc-count.auto-incr	true	mapred
1107	2	mapreduce.application.classpath		mapred
1108	2	mapreduce.job.end-notification.max.retry.interval	5000	mapred
1109	2	mapreduce.jobhistory.joblist.cache.size	20000	mapred
1110	2	mapreduce.job.acl-view-job	 	mapred
1111	2	mapreduce.job.classloader	false	mapred
1112	2	mapreduce.reduce.shuffle.fetch.retry.interval-ms	1000	mapred
1113	2	mapreduce.jobhistory.loadedtasks.cache.size		mapred
1114	2	yarn.app.mapreduce.am.job.task.listener.thread-count	30	mapred
1115	2	yarn.app.mapreduce.am.resource.cpu-vcores	1	mapred
1116	2	mapreduce.output.fileoutputformat.compress.type	RECORD	mapred
1117	2	mapreduce.map.skip.proc-count.auto-incr	true	mapred
1118	2	mapreduce.job.end-notification.url		mapred
1119	2	mapreduce.job.token.tracking.ids		mapred
1120	2	mapreduce.job.end-notification.retry.interval	1000	mapred
1121	2	mapreduce.reduce.shuffle.fetch.retry.timeout-ms	30000	mapred
1122	2	yarn.app.mapreduce.shuffle.log.separate	true	mapred
1123	2	mapreduce.jobhistory.webapp.rest-csrf.custom-header	X-XSRF-Header	mapred
1124	2	mapreduce.map.memory.mb	1024	mapred
1125	2	yarn.app.mapreduce.am.job.client.port-range		mapred
1126	2	mapreduce.job.log4j-properties-file		mapred
1127	2	mapreduce.jobhistory.jhist.format	json	mapred
1128	2	mapreduce.map.cpu.vcores	1	mapred
1129	2	mapreduce.job.running.reduce.limit	0	mapred
1130	2	mapreduce.task.profile.maps	0-2	mapred
1131	2	mapreduce.job.reduce.shuffle.consumer.plugin.class	org.apache.hadoop.mapreduce.task.reduce.Shuffle	mapred
1132	2	mapreduce.shuffle.ssl.file.buffer.size	65536	mapred
1133	2	mapreduce.task.io.sort.factor	10	mapred
1134	2	mapreduce.job.tags		mapred
1135	2	yarn.app.mapreduce.am.command-opts	-Xmx1024m	mapred
1136	2	mapreduce.job.skip.outdir		mapred
1137	2	mapreduce.jobhistory.admin.acl	*	mapred
1138	2	mapreduce.job.reducer.unconditional-preempt.delay.sec	300	mapred
1139	2	mapreduce.map.skip.maxrecords	0	mapred
1140	2	yarn.app.mapreduce.am.hard-kill-timeout-ms	10000	mapred
1141	2	mapreduce.job.node-label-expression		mapred
1142	2	mapreduce.jobhistory.principal	jhs/_HOST@REALM.TLD	mapred
1143	2	mapreduce.job.maxtaskfailures.per.tracker	3	mapred
1144	2	mapreduce.jobhistory.recovery.enable	false	mapred
1145	2	mapreduce.shuffle.max.connections	0	mapred
1146	2	mapreduce.jobhistory.loadedjobs.cache.size	5	mapred
1147	2	mapreduce.reduce.merge.inmem.threshold	1000	mapred
1148	2	mapreduce.client.output.filter	FAILED	mapred
1149	2	mapreduce.job.cache.limit.max-single-resource-mb	0	mapred
1150	2	mapreduce.task.profile	false	mapred
1151	2	mapreduce.task.exit.timeout	60000	mapred
1152	2	mapreduce.jobhistory.http.policy	HTTP_ONLY	mapred
1153	2	mapreduce.job.speculative.retry-after-no-speculate	1000	mapred
1154	2	mapreduce.job.queuename	default	mapred
1155	2	mapreduce.jobhistory.max-age-ms	604800000	mapred
1156	2	mapreduce.job.token.tracking.ids.enabled	false	mapred
1157	2	yarn.app.mapreduce.am.log.level	INFO	mapred
1158	2	mapreduce.jobhistory.move.thread-count	3	mapred
1159	2	mapreduce.job.split.metainfo.maxsize	10000000	mapred
1160	2	mapreduce.task.io.sort.mb	100	mapred
1161	2	yarn.app.mapreduce.client-am.ipc.max-retries	3	mapred
1162	2	mapreduce.jobhistory.jobname.limit	50	mapred
1163	2	mapreduce.reduce.cpu.vcores	1	mapred
1164	2	mapreduce.task.profile.params	-agentlib:hprof=cpu=samples,heap=sites,force=n,thread=y,verbose=n,file=%s	mapred
1165	2	mapreduce.jobhistory.datestring.cache.size	200000	mapred
1166	2	mapreduce.jobhistory.address	0.0.0.0:10020	mapred
1167	2	mapreduce.jobhistory.loadedjob.tasks.max	-1	mapred
1168	2	mapreduce.task.timeout	600000	mapred
1169	2	yarn.app.mapreduce.client.max-retries	3	mapred
1170	2	mapreduce.job.committer.setup.cleanup.needed	true	mapred
1171	2	mapreduce.task.local-fs.write-limit.bytes	-1	mapred
1172	2	mapreduce.framework.name	local	mapred
1173	2	mapreduce.fileoutputcommitter.algorithm.version	1	mapred
1174	2	mapreduce.job.max.split.locations	10	mapred
1175	2	mapreduce.job.speculative.retry-after-speculate	15000	mapred
1176	2	mapreduce.shuffle.connection-keep-alive.enable	false	mapred
1177	2	mapreduce.jobhistory.webapp.https.address	0.0.0.0:19890	mapred
1178	2	mapreduce.input.lineinputformat.linespermap	1	mapred
1179	2	mapreduce.task.profile.map.params	${mapreduce.task.profile.params}	mapred
1180	2	mapreduce.task.exit.timeout.check-interval-ms	20000	mapred
1181	2	mapreduce.map.speculative	true	mapred
1182	2	mapreduce.jobhistory.keytab	/etc/security/keytab/jhs.service.keytab	mapred
1183	2	mapreduce.shuffle.ssl.enabled	false	mapred
1184	2	mapreduce.reduce.log.level	INFO	mapred
1185	2	yarn.app.mapreduce.am.webapp.port-range		mapred
1186	2	yarn.app.mapreduce.am.admin-command-opts		mapred
1187	2	mapreduce.job.cache.limit.max-resources-mb	0	mapred
1188	2	mapreduce.job.speculative.speculative-cap-running-tasks	0.1	mapred
1189	2	mapreduce.map.log.level	INFO	mapred
1190	2	yarn.app.mapreduce.am.scheduler.heartbeat.interval-ms	1000	mapred
1191	2	yarn.app.mapreduce.am.staging-dir	/tmp/hadoop-yarn/staging	mapred
1192	2	mapreduce.reduce.shuffle.merge.percent	0.66	mapred
1193	2	mapreduce.job.redacted-properties		mapred
1194	2	mapreduce.output.fileoutputformat.compress	false	mapred
1195	2	mapreduce.reduce.shuffle.memory.limit.percent	0.25	mapred
1196	2	mapreduce.job.sharedcache.mode	disabled	mapred
1197	2	mapreduce.job.hdfs-servers	${fs.defaultFS}	mapred
1198	2	mapreduce.application.framework.path		mapred
1199	2	mapreduce.map.output.compress	false	mapred
1200	2	mapreduce.job.running.map.limit	0	mapred
1201	2	mapreduce.reduce.input.buffer.percent	0	mapred
1202	2	mapreduce.task.merge.progress.records	10000	mapred
1203	2	mapreduce.job.send-token-conf		mapred
1204	2	map.sort.class	org.apache.hadoop.util.QuickSort	mapred
1205	2	mapreduce.reduce.shuffle.retry-delay.max.ms	60000	mapred
1206	2	yarn.app.mapreduce.shuffle.log.limit.kb	0	mapred
1207	2	mapreduce.client.progressmonitor.pollinterval	1000	mapred
1208	2	yarn.app.mapreduce.am.job.committer.commit-window	10000	mapred
1209	2	mapreduce.jobhistory.move.interval-ms	180000	mapred
1210	2	mapreduce.jvm.system-properties-to-log	os.name,os.version,java.home,java.runtime.version,java.vendor,java.version,java.vm.name,java.class.path,java.io.tmpdir,user.dir,user.name	mapred
1211	2	mapreduce.map.sort.spill.percent	0.8	mapred
1212	2	mapreduce.admin.user.env		mapred
1213	2	mapreduce.task.profile.reduce.params	${mapreduce.task.profile.params}	mapred
1214	2	mapreduce.ifile.readahead	true	mapred
1215	2	mapreduce.jobtracker.staging.root.dir	${hadoop.tmp.dir}/mapred/staging	mapred
1216	2	mapreduce.reduce.memory.mb	1024	mapred
1217	2	mapreduce.jobhistory.admin.address	0.0.0.0:10033	mapred
1218	2	yarn.app.mapreduce.am.env		mapred
1219	2	mapreduce.output.fileoutputformat.compress.codec	org.apache.hadoop.io.compress.DefaultCodec	mapred
1220	2	mapreduce.jobhistory.webapp.address	0.0.0.0:19888	mapred
1221	2	mapreduce.task.userlog.limit.kb	0	mapred
1222	2	mapreduce.client.completion.pollinterval	5000	mapred
1223	2	mapreduce.reduce.shuffle.fetch.retry.enabled	${yarn.nodemanager.recovery.enabled}	mapred
1224	2	yarn.app.mapreduce.task.container.log.backups	0	mapred
1225	2	mapreduce.jobhistory.recovery.store.leveldb.path	${hadoop.tmp.dir}/mapred/history/recoverystore	mapred
1226	2	mapreduce.jobhistory.store.class		mapred
1227	2	mapreduce.jobhistory.webapp.xfs-filter.xframe-options	SAMEORIGIN	mapred
1228	2	mapreduce.job.cache.limit.max-resources	0	mapred
1229	2	yarn.app.mapreduce.am.resource.mb	1536	mapred
1230	4	spark.app.name		spark_defaults
1231	4	spark.driver.cores	1	spark_defaults
1232	4	spark.driver.maxResultSize	1g	spark_defaults
1233	4	spark.driver.memory	1g	spark_defaults
1234	4	spark.executor.memory	1g	spark_defaults
1235	4	spark.extraListeners		spark_defaults
1236	4	spark.local.dir	/tmp	spark_defaults
1237	4	spark.logConf	false	spark_defaults
1239	4	spark.submit.deployMode		spark_defaults
1240	4	spark.log.callerContext		spark_defaults
1241	4	spark.driver.supervise	false	spark_defaults
1242	4	spark.driver.extraClassPath		spark_defaults
1243	4	spark.driver.extraJavaOptions		spark_defaults
1244	4	spark.driver.extraLibraryPath		spark_defaults
1245	4	spark.driver.userClassPathFirst	false	spark_defaults
1246	4	spark.executor.extraClassPath		spark_defaults
1247	4	spark.executor.extraJavaOptions		spark_defaults
1248	4	spark.executor.extraLibraryPath		spark_defaults
1249	4	spark.executor.logs.rolling.maxRetainedFiles		spark_defaults
1250	4	spark.executor.logs.rolling.enableCompression	false	spark_defaults
1251	4	spark.executor.logs.rolling.maxSize		spark_defaults
1252	4	spark.executor.logs.rolling.strategy		spark_defaults
1253	4	spark.executor.logs.rolling.time.interval	daily	spark_defaults
1254	4	spark.executor.userClassPathFirst	false	spark_defaults
1255	4	spark.executorEnv.[EnvironmentVariableName]		spark_defaults
1256	4	spark.redaction.regex	(?i)secret|password	spark_defaults
1257	4	spark.python.profile	false	spark_defaults
1258	4	spark.python.profile.dump		spark_defaults
1259	4	spark.python.worker.memory	512m	spark_defaults
1260	4	spark.python.worker.reuse	true	spark_defaults
1261	4	spark.files		spark_defaults
1262	4	spark.submit.pyFiles		spark_defaults
1263	4	spark.jars		spark_defaults
1264	4	spark.jars.packages		spark_defaults
1265	4	spark.jars.excludes		spark_defaults
1266	4	spark.jars.ivy		spark_defaults
1267	4	spark.jars.ivySettings		spark_defaults
1268	4	spark.pyspark.driver.python		spark_defaults
1269	4	spark.pyspark.python		spark_defaults
1270	4	spark.reducer.maxSizeInFlight	48m	spark_defaults
1271	4	spark.reducer.maxReqsInFlight	Int.MaxValue	spark_defaults
1272	4	spark.shuffle.compress	true	spark_defaults
1273	4	spark.shuffle.file.buffer	32k	spark_defaults
1274	4	spark.shuffle.io.maxRetries	3	spark_defaults
1275	4	spark.shuffle.io.numConnectionsPerPeer	1	spark_defaults
1276	4	spark.shuffle.io.preferDirectBufs	true	spark_defaults
1277	4	spark.shuffle.io.retryWait	5s	spark_defaults
1278	4	spark.shuffle.service.enabled	false	spark_defaults
1279	4	spark.shuffle.service.port	7337	spark_defaults
1280	4	spark.shuffle.service.index.cache.entries	1024	spark_defaults
1281	4	spark.shuffle.sort.bypassMergeThreshold	200	spark_defaults
1282	4	spark.shuffle.spill.compress	true	spark_defaults
1283	4	spark.shuffle.accurateBlockThreshold	100 * 1024 * 1024	spark_defaults
1284	4	spark.io.encryption.enabled	false	spark_defaults
1285	4	spark.io.encryption.keySizeBits	128	spark_defaults
1286	4	spark.io.encryption.keygen.algorithm	HmacSHA1	spark_defaults
1287	4	spark.eventLog.compress	false	spark_defaults
1288	4	spark.eventLog.dir	file:///tmp/spark-events	spark_defaults
1289	4	spark.eventLog.enabled	false	spark_defaults
1290	4	spark.ui.enabled	true	spark_defaults
1291	4	spark.ui.killEnabled	true	spark_defaults
1292	4	spark.ui.port	4040	spark_defaults
1293	4	spark.ui.retainedJobs	1000	spark_defaults
1294	4	spark.ui.retainedStages	1000	spark_defaults
1295	4	spark.ui.retainedTasks	100000	spark_defaults
1296	4	spark.ui.reverseProxy	false	spark_defaults
1297	4	spark.ui.reverseProxyUrl		spark_defaults
1298	4	spark.ui.showConsoleProgress	true	spark_defaults
1299	4	spark.worker.ui.retainedExecutors	1000	spark_defaults
1300	4	spark.worker.ui.retainedDrivers	1000	spark_defaults
1301	4	spark.sql.ui.retainedExecutions	1000	spark_defaults
1303	4	spark.ui.retainedDeadExecutors	100	spark_defaults
1304	4	spark.broadcast.compress	true	spark_defaults
1305	4	spark.io.compression.codec	lz4	spark_defaults
1306	4	spark.io.compression.lz4.blockSize	32k	spark_defaults
1307	4	spark.io.compression.snappy.blockSize	32k	spark_defaults
1308	4	spark.kryo.classesToRegister		spark_defaults
1309	4	spark.kryo.referenceTracking	true	spark_defaults
1310	4	spark.kryo.registrationRequired	false	spark_defaults
1311	4	spark.kryo.registrator		spark_defaults
1312	4	spark.kryo.unsafe	false	spark_defaults
1313	4	spark.kryoserializer.buffer.max	64m	spark_defaults
1314	4	spark.kryoserializer.buffer	64k	spark_defaults
1315	4	spark.rdd.compress	false	spark_defaults
1316	4	spark.serializer	"org.apache.spark.serializer.JavaSerializer"	spark_defaults
1317	4	spark.serializer.objectStreamReset	100	spark_defaults
1318	4	spark.memory.fraction	0.6	spark_defaults
1319	4	spark.memory.storageFraction	0.5	spark_defaults
1320	4	spark.memory.offHeap.enabled	false	spark_defaults
1321	4	spark.memory.offHeap.size	0	spark_defaults
1322	4	spark.memory.useLegacyMode	false	spark_defaults
1323	4	spark.shuffle.memoryFraction	0.2	spark_defaults
1324	4	spark.storage.memoryFraction	0.6	spark_defaults
1325	4	spark.storage.unrollFraction	0.2	spark_defaults
1326	4	spark.storage.replication.proactive 	false	spark_defaults
1327	4	spark.broadcast.blockSize	4m	spark_defaults
1328	4	spark.executor.cores		spark_defaults
1329	4	spark.default.parallelism		spark_defaults
1330	4	spark.executor.heartbeatInterval	10s	spark_defaults
1331	4	spark.files.fetchTimeout	60s	spark_defaults
1332	4	spark.files.useFetchCache	true	spark_defaults
1333	4	spark.files.overwrite	false	spark_defaults
1334	4	spark.files.maxPartitionBytes	134217728 (128 MB)	spark_defaults
1335	4	spark.files.openCostInBytes	4194304 (4 MB)	spark_defaults
1336	4	spark.hadoop.cloneConf	false	spark_defaults
1337	4	spark.hadoop.validateOutputSpecs	true	spark_defaults
1338	4	spark.storage.memoryMapThreshold	2m	spark_defaults
1339	4	spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version	1	spark_defaults
1340	4	spark.rpc.message.maxSize	128	spark_defaults
1341	4	spark.blockManager.port	(random)	spark_defaults
1342	4	spark.driver.blockManager.port	(value of spark.blockManager.port)	spark_defaults
1343	4	spark.driver.bindAddress	(value of spark.driver.host)	spark_defaults
1344	4	spark.driver.host	(local hostname)	spark_defaults
1345	4	spark.driver.port	(random)	spark_defaults
1346	4	spark.network.timeout	120s	spark_defaults
1347	4	spark.port.maxRetries	16	spark_defaults
1348	4	spark.rpc.numRetries	3	spark_defaults
1349	4	spark.rpc.retry.wait	3s	spark_defaults
1350	4	spark.rpc.askTimeout	spark.network.timeout	spark_defaults
1351	4	spark.rpc.lookupTimeout	120s	spark_defaults
1352	4	spark.cores.max	(not set)	spark_defaults
1353	4	spark.locality.wait	3s	spark_defaults
1354	4	spark.locality.wait.node	spark.locality.wait	spark_defaults
1355	4	spark.locality.wait.process	spark.locality.wait	spark_defaults
1356	4	spark.locality.wait.rack	spark.locality.wait	spark_defaults
1357	4	spark.scheduler.maxRegisteredResourcesWaitingTime	30s	spark_defaults
1358	4	spark.scheduler.minRegisteredResourcesRatio	0.8 for YARN mode	spark_defaults
1359	4	spark.scheduler.mode	FIFO	spark_defaults
1360	4	spark.scheduler.revive.interval	1s	spark_defaults
1361	4	spark.blacklist.enabled	false 	spark_defaults
1362	4	spark.blacklist.timeout	1h	spark_defaults
1363	4	spark.blacklist.task.maxTaskAttemptsPerExecutor	1	spark_defaults
1364	4	spark.blacklist.task.maxTaskAttemptsPerNode	2	spark_defaults
1365	4	spark.blacklist.stage.maxFailedTasksPerExecutor	2	spark_defaults
1366	4	spark.blacklist.stage.maxFailedExecutorsPerNode	2	spark_defaults
1367	4	spark.blacklist.application.maxFailedTasksPerExecutor	2	spark_defaults
1368	4	spark.blacklist.application.maxFailedExecutorsPerNode	2	spark_defaults
1369	4	spark.blacklist.killBlacklistedExecutors	false	spark_defaults
1370	4	spark.speculation	false	spark_defaults
1371	4	spark.speculation.interval	100ms	spark_defaults
1372	4	spark.speculation.multiplier	1.5	spark_defaults
1373	4	spark.speculation.quantile	0.75	spark_defaults
1374	4	spark.task.cpus	1	spark_defaults
1375	4	spark.task.maxFailures	4	spark_defaults
1376	4	spark.task.reaper.enabled	false	spark_defaults
1377	4	spark.task.reaper.pollingInterval	10s	spark_defaults
1378	4	spark.task.reaper.threadDump	true	spark_defaults
1379	4	spark.task.reaper.killTimeout	-1	spark_defaults
1380	4	spark.stage.maxConsecutiveAttempts	4	spark_defaults
1381	4	spark.dynamicAllocation.enabled	false	spark_defaults
1382	4	spark.dynamicAllocation.executorIdleTimeout	60s	spark_defaults
1383	4	spark.dynamicAllocation.cachedExecutorIdleTimeout	infinity	spark_defaults
1384	4	spark.dynamicAllocation.initialExecutors	spark.dynamicAllocation.minExecutors	spark_defaults
1385	4	spark.dynamicAllocation.maxExecutors	infinity	spark_defaults
1386	4	spark.dynamicAllocation.minExecutors	0	spark_defaults
1387	4	spark.dynamicAllocation.schedulerBacklogTimeout	1s	spark_defaults
1388	4	spark.dynamicAllocation.sustainedSchedulerBacklogTimeout	schedulerBacklogTimeout	spark_defaults
1389	4	spark.acls.enable	false	spark_defaults
1390	4	spark.admin.acls	Empty	spark_defaults
1391	4	spark.admin.acls.groups	Empty	spark_defaults
1392	4	spark.user.groups.mapping	org.apache.spark.security.ShellBasedGroupsMappingProvider	spark_defaults
1393	4	spark.authenticate	false	spark_defaults
1394	4	spark.authenticate.secret		spark_defaults
1395	4	spark.network.crypto.enabled	false	spark_defaults
1396	4	spark.network.crypto.keyLength	128	spark_defaults
1397	4	spark.network.crypto.keyFactoryAlgorithm	PBKDF2WithHmacSHA1	spark_defaults
1398	4	spark.network.crypto.saslFallback	true	spark_defaults
1399	4	spark.network.crypto.config.*		spark_defaults
1400	4	spark.authenticate.enableSaslEncryption	false	spark_defaults
1401	4	spark.network.sasl.serverAlwaysEncrypt	false	spark_defaults
1402	4	spark.core.connection.ack.wait.timeout	spark.network.timeout	spark_defaults
1403	4	spark.modify.acls	Empty	spark_defaults
1404	4	spark.modify.acls.groups	Empty	spark_defaults
1405	4	spark.ui.filters		spark_defaults
1406	4	spark.ui.view.acls	Empty	spark_defaults
1407	4	spark.ui.view.acls.groups	Empty	spark_defaults
1408	4	spark.ssl.enabled	false	spark_defaults
1409	4	spark.ssl.[namespace].port		spark_defaults
1410	4	spark.ssl.enabledAlgorithms	Empty	spark_defaults
1411	4	spark.ssl.keyPassword		spark_defaults
1412	4	spark.ssl.keyStore		spark_defaults
1413	4	spark.ssl.keyStorePassword		spark_defaults
1414	4	spark.ssl.keyStoreType	JKS	spark_defaults
1415	4	spark.ssl.protocol		spark_defaults
1416	4	spark.ssl.needClientAuth	false	spark_defaults
1417	4	spark.ssl.trustStore		spark_defaults
1418	4	spark.ssl.trustStorePassword		spark_defaults
1419	4	spark.ssl.trustStoreType	JKS	spark_defaults
1420	4	spark.streaming.backpressure.enabled	false	spark_defaults
1421	4	spark.streaming.backpressure.initialRate	not set	spark_defaults
1422	4	spark.streaming.blockInterval	200ms	spark_defaults
1423	4	spark.streaming.receiver.maxRate	not set	spark_defaults
1424	4	spark.streaming.receiver.writeAheadLog.enable	false	spark_defaults
1425	4	spark.streaming.unpersist	true	spark_defaults
1426	4	spark.streaming.stopGracefullyOnShutdown	false	spark_defaults
1427	4	spark.streaming.kafka.maxRatePerPartition	not set	spark_defaults
1428	4	spark.streaming.kafka.maxRetries	1	spark_defaults
1429	4	spark.streaming.ui.retainedBatches	1000	spark_defaults
1430	4	spark.streaming.driver.writeAheadLog.closeFileAfterWrite	false	spark_defaults
1431	4	spark.streaming.receiver.writeAheadLog.closeFileAfterWrite	false	spark_defaults
1432	4	spark.r.numRBackendThreads	2	spark_defaults
1433	4	spark.r.command	Rscript	spark_defaults
1434	4	spark.r.driver.command	spark.r.command	spark_defaults
1435	4	spark.r.shell.command	R	spark_defaults
1436	4	spark.r.backendConnectionTimeout	6000	spark_defaults
1437	4	spark.r.heartBeatInterval	100	spark_defaults
1438	4	spark.graphx.pregel.checkpointInterval	-1	spark_defaults
1439	4	spark.deploy.recoveryMode		spark_defaults
1440	4	spark.deploy.zookeeper.url		spark_defaults
1441	4	spark.deploy.zookeeper.dir		spark_defaults
1445	4	SPARK_LOCAL_IP		spark_env
1447	4	SPARK_LOCAL_DIRS		spark_env
1448	4	MESOS_NATIVE_JAVA_LIBRARY		spark_env
1450	4	HADOOP_CONF_DIR		spark_env
1451	4	YARN_CONF_DIR		spark_env
1452	4	SPARK_EXECUTOR_CORES	1	spark_env
1453	4	SPARK_EXECUTOR_MEMORY	1G	spark_env
1454	4	SPARK_DRIVER_MEMORY	1G	spark_env
1455	4	SPARK_MASTER_HOST		spark_env
1456	4	SPARK_MASTER_PORT		spark_env
1457	4	SPARK_MASTER_OPTS		spark_env
1458	4	SPARK_WORKER_CORES		spark_env
1459	4	SPARK_WORKER_MEMORY		spark_env
1460	4	SPARK_WORKER_PORT		spark_env
1461	4	SPARK_WORKER_DIR		spark_env
1462	4	SPARK_WORKER_OPTS		spark_env
1463	4	SPARK_DAEMON_MEMORY	1g	spark_env
1464	4	SPARK_HISTORY_OPTS		spark_env
1465	4	SPARK_SHUFFLE_OPTS		spark_env
1466	4	SPARK_DAEMON_JAVA_OPTS		spark_env
1467	4	SPARK_DAEMON_CLASSPATH		spark_env
1469	4	SPARK_CONF_DIR	${SPARK_HOME}/conf	spark_env
1470	4	SPARK_LOG_DIR	${SPARK_HOME}/logs	spark_env
1471	4	SPARK_PID_DIR	/tmp	spark_env
1472	4	SPARK_IDENT_STRING	$USER	spark_env
1473	4	SPARK_NICENESS	0	spark_env
1474	4	SPARK_NO_DAEMONIZE		spark_env
1475	4	MKL_NUM_THREADS	1	spark_env
1476	4	OPENBLAS_NUM_THREADS	1	spark_env
1477	4	JAVA_HOME	${JAVA_HOME}	spark_env
1478	4	PYSPARK_PYTHON		spark_env
1479	4	PYSPARK_DRIVER_PYTHON	${PYSPARK_PYTHON}	spark_env
1480	4	SPARKR_DRIVER_R		spark_env
1482	4	SPARK_PUBLIC_DNS		spark_env
1483	1	ssl.client.truststore.reload.interval	10000	ssl_client
1484	1	ssl.client.keystore.keypassword		ssl_client
1485	1	ssl.client.keystore.location		ssl_client
1486	1	ssl.client.truststore.password		ssl_client
1487	1	ssl.client.truststore.type	jks	ssl_client
1488	1	ssl.client.truststore.location		ssl_client
1489	1	ssl.client.keystore.password		ssl_client
1490	1	ssl.client.keystore.type	jks	ssl_client
1491	1	ssl.server.truststore.password		ssl_server
1492	1	ssl.server.truststore.type	jks	ssl_server
1493	1	ssl.server.exclude.cipher.list	"TLS_ECDHE_RSA_WITH_RC4_128_SHA,SSL_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA,SSL_RSA_WITH_DES_CBC_SHA,SSL_DHE_RSA_WITH_DES_CBC_SHA,SSL_RSA_EXPORT_WITH_RC4_40_MD5,SSL_RSA_EXPORT_WITH_DES40_CBC_SHA,SSL_RSA_WITH_RC4_128_MD5"	ssl_server
1494	1	ssl.server.keystore.keypassword		ssl_server
1495	1	ssl.server.truststore.location		ssl_server
1496	1	ssl.server.truststore.reload.interval	10000	ssl_server
1497	1	ssl.server.keystore.location		ssl_server
1498	1	ssl.server.keystore.type	jks	ssl_server
1499	1	ssl.server.keystore.password		ssl_server
1500	2	yarn.log-aggregation.file-formats	TFile	yarn
1501	2	yarn.resourcemanager.scheduler.monitor.policies	org.apache.hadoop.yarn.server.resourcemanager.monitor.capacity.ProportionalCapacityPreemptionPolicy	yarn
1502	2	yarn.nodemanager.node-labels.provider.configured-node-partition		yarn
1503	2	yarn.router.webapp.interceptor-class.pipeline	org.apache.hadoop.yarn.server.router.webapp.DefaultRequestInterceptorREST	yarn
1504	2	yarn.nodemanager.runtime.linux.docker.enable-userremapping.allowed	false	yarn
1505	2	yarn.resourcemanager.leveldb-state-store.compaction-interval-secs	3600	yarn
1506	2	yarn.application.classpath		yarn
1507	2	yarn.admin.acl	*	yarn
1508	2	yarn.timeline-service.entity-group-fs-store.cleaner-interval-seconds	3600	yarn
1509	2	yarn.nodemanager.runtime.linux.docker.userremapping-gid-threshold	1	yarn
1510	2	yarn.federation.enabled	false	yarn
1511	2	yarn.timeline-service.leveldb-timeline-store.ttl-interval-ms	300000	yarn
1512	2	yarn.nodemanager.node-labels.provider.script.opts		yarn
1513	2	yarn.resourcemanager.leveldb-state-store.path	${hadoop.tmp.dir}/yarn/system/rmstore	yarn
1514	2	yarn.nodemanager.runtime.linux.allowed-runtimes	default	yarn
1515	2	yarn.ipc.rpc.class	org.apache.hadoop.yarn.ipc.HadoopYarnProtoRPC	yarn
1516	2	yarn.nodemanager.process-kill-wait.ms	2000	yarn
1517	2	yarn.nodemanager.node-labels.provider.script.path		yarn
1518	2	yarn.minicluster.use-rpc	false	yarn
1519	2	yarn.nodemanager.aux-services		yarn
1520	2	yarn.nodemanager.runtime.linux.docker.default-container-network	host	yarn
1521	2	yarn.nodemanager.runtime.linux.docker.userremapping-uid-threshold	1	yarn
1522	2	yarn.nodemanager.container-manager.thread-count	20	yarn
1523	2	yarn.resourcemanager.container-tokens.master-key-rolling-interval-secs	86400	yarn
1524	2	yarn.nodemanager.windows-container.memory-limit.enabled	false	yarn
1525	2	yarn.timeline-service.webapp.rest-csrf.methods-to-ignore	GET,OPTIONS,HEAD	yarn
1526	2	yarn.timeline-service.entity-group-fs-store.cache-store-class	org.apache.hadoop.yarn.server.timeline.MemoryTimelineStore	yarn
1527	2	yarn.ipc.server.factory.class		yarn
1528	2	yarn.nodemanager.localizer.cache.cleanup.interval-ms	600000	yarn
1529	2	yarn.nodemanager.node-labels.resync-interval-ms	120000	yarn
1530	2	yarn.nodemanager.webapp.xfs-filter.xframe-options	SAMEORIGIN	yarn
1531	2	yarn.timeline-service.leveldb-timeline-store.start-time-read-cache-size	10000	yarn
1532	2	yarn.resourcemanager.zk-state-store.root-node.acl		yarn
1533	2	yarn.nodemanager.keytab	/etc/krb5.keytab	yarn
1534	2	yarn.resourcemanager.admin.address	${yarn.resourcemanager.hostname}:8033	yarn
1535	2	yarn.timeline-service.webapp.xfs-filter.xframe-options	SAMEORIGIN	yarn
1536	2	yarn.resourcemanager.fs.state-store.retry-policy-spec	2000, 500	yarn
1537	2	yarn.nodemanager.delete.debug-delay-sec	0	yarn
1538	2	yarn.timeline-service.ttl-enable	true	yarn
1539	2	yarn.timeline-service.entity-group-fs-store.retain-seconds	604800	yarn
1540	2	yarn.nodemanager.resource-monitor.interval-ms	3000	yarn
1541	2	yarn.nodemanager.webapp.spnego-keytab-file		yarn
1542	2	yarn.resourcemanager.container.liveness-monitor.interval-ms	600000	yarn
1543	2	yarn.nodemanager.env-whitelist	JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME	yarn
1544	2	yarn.nodemanager.linux-container-executor.cgroups.hierarchy	/hadoop-yarn	yarn
1545	2	yarn.resourcemanager.recovery.enabled	false	yarn
1547	2	yarn.nodemanager.disk-health-checker.enable	true	yarn
1548	2	yarn.nodemanager.container-monitor.enabled	true	yarn
1549	2	yarn.nodemanager.disk-health-checker.interval-ms	120000	yarn
1550	2	yarn.nodemanager.node-labels.provider.fetch-interval-ms	600000	yarn
1551	2	yarn.resourcemanager.resource-tracker.client.thread-count	50	yarn
1552	2	yarn.fail-fast	false	yarn
1553	2	yarn.resourcemanager.webapp.cross-origin.enabled	false	yarn
1554	2	yarn.resourcemanager.bind-host		yarn
1555	2	yarn.nodemanager.delete.thread-count	4	yarn
1556	2	yarn.scheduler.configuration.mutation.acl-policy.class	org.apache.hadoop.yarn.server.resourcemanager.scheduler.DefaultConfigurationMutationACLPolicy	yarn
1557	2	yarn.nodemanager.admin-env	MALLOC_ARENA_MAX=$MALLOC_ARENA_MAX	yarn
1558	2	yarn.nodemanager.linux-container-executor.cgroups.mount-path		yarn
1559	2	yarn.timeline-service.hostname	0.0.0.0	yarn
1560	2	yarn.resourcemanager.proxy-user-privileges.enabled	false	yarn
1561	2	yarn.resourcemanager.nm-container-queuing.load-comparator	QUEUE_LENGTH	yarn
1562	2	yarn.acl.enable	false	yarn
1563	2	yarn.nodemanager.resourcemanager.connect.max-wait.ms		yarn
1564	2	yarn.sharedcache.cleaner.initial-delay-mins	10	yarn
1565	2	yarn.resourcemanager.delegation-token-renewer.thread-count	50	yarn
1566	2	yarn.resourcemanager.application-timeouts.monitor.interval-ms	3000	yarn
1567	2	yarn.nodemanager.default-container-executor.log-dirs.permissions	710	yarn
1568	2	yarn.resourcemanager.client.thread-count	50	yarn
1569	2	yarn.timeline-service.entity-group-fs-store.leveldb-cache-read-cache-size	10485760	yarn
1570	2	yarn.sharedcache.admin.address	0.0.0.0:8047	yarn
1571	2	yarn.nodemanager.linux-container-executor.nonsecure-mode.user-pattern	^[_.A-Za-z0-9][-@_.A-Za-z0-9]{0,255}?[$]?$	yarn
1572	2	yarn.resourcemanager.max-completed-applications	10000	yarn
1573	2	yarn.sharedcache.cleaner.period-mins	1440	yarn
1574	2	yarn.nodemanager.linux-container-executor.cgroups.mount	false	yarn
1575	2	yarn.sharedcache.checksum.algo.impl	org.apache.hadoop.yarn.sharedcache.ChecksumSHA256Impl	yarn
1576	2	yarn.node-labels.fs-store.retry-policy-spec	2000, 500	yarn
1577	2	yarn.resourcemanager.nodemanager.minimum.version	NONE	yarn
1578	2	yarn.log-aggregation-enable	false	yarn
1579	2	yarn.nodemanager.log.retain-seconds	10800	yarn
1580	2	yarn.timeline-service.entity-group-fs-store.done-dir	/tmp/entity-file-history/done/	yarn
1581	2	yarn.nodemanager.local-cache.max-files-per-directory	8192	yarn
1582	2	yarn.sharedcache.root-dir	/sharedcache	yarn
1583	2	yarn.nodemanager.bind-host		yarn
1584	2	yarn.resourcemanager.connect.retry-interval.ms	30000	yarn
1585	2	yarn.timeline-service.webapp.address	${yarn.timeline-service.hostname}:8188	yarn
1586	2	yarn.scheduler.minimum-allocation-mb	1024	yarn
1587	2	yarn.sharedcache.cleaner.resource-sleep-ms	0	yarn
1588	2	yarn.resourcemanager.nm-container-queuing.sorting-nodes-interval-ms	1000	yarn
1589	2	yarn.nodemanager.container-executor.os.sched.priority.adjustment		yarn
1590	2	yarn.scheduler.maximum-allocation-mb	8192	yarn
1591	2	yarn.nodemanager.container.stderr.tail.bytes 	4096	yarn
1592	2	yarn.nodemanager.vmem-check-enabled	true	yarn
1593	2	yarn.timeline-service.entity-group-fs-store.with-user-dir	false	yarn
1594	2	yarn.resourcemanager.nm-tokens.master-key-rolling-interval-secs	86400	yarn
1595	2	yarn.nodemanager.log.deletion-threads-count	4	yarn
1596	2	yarn.nodemanager.linux-container-executor.nonsecure-mode.limit-users	true	yarn
1597	2	yarn.resourcemanager.delegation.token.renew-interval	86400000	yarn
1598	2	yarn.nodemanager.linux-container-executor.nonsecure-mode.local-user	nobody	yarn
1599	2	yarn.web-proxy.address		yarn
1600	2	yarn.resourcemanager.webapp.spnego-principal		yarn
1601	2	yarn.timeline-service.entity-group-fs-store.active-dir	/tmp/entity-file-history/active	yarn
1602	2	yarn.log.server.web-service.url		yarn
1603	2	yarn.nodemanager.linux-container-executor.group		yarn
1604	2	yarn.resourcemanager.am-rm-tokens.master-key-rolling-interval-secs	86400	yarn
1605	2	yarn.resourcemanager.delegation.key.update-interval	86400000	yarn
1606	2	yarn.nodemanager.container-localizer.java.opts	-Xmx256m	yarn
1607	2	yarn.nodemanager.webapp.https.address	0.0.0.0:8044	yarn
1608	2	yarn.resourcemanager.reservation-system.plan.follower		yarn
1609	2	yarn.nodemanager.container-monitor.resource-calculator.class		yarn
1610	2	yarn.client.application-client-protocol.poll-interval-ms	200	yarn
1611	2	yarn.nodemanager.localizer.address	${yarn.nodemanager.hostname}:8040	yarn
1612	2	yarn.ipc.record.factory.class		yarn
1613	2	yarn.nodemanager.resource.count-logical-processors-as-cores	false	yarn
1614	2	yarn.nodemanager.resource.system-reserved-memory-mb	-1	yarn
1615	2	yarn.timeline-service.client.best-effort	false	yarn
1616	2	yarn.sharedcache.admin.thread-count	1	yarn
1617	2	yarn.nodemanager.resource.cpu-vcores	-1	yarn
1618	2	yarn.resourcemanager.webapp.delegation-token-auth-filter.enabled	true	yarn
1619	2	yarn.resourcemanager.reservation-system.class		yarn
1620	2	yarn.log-aggregation.retain-check-interval-seconds	-1	yarn
1621	2	yarn.resourcemanager.application-master-service.processors		yarn
1622	2	yarn.timeline-service.ui-names		yarn
1623	2	yarn.nodemanager.webapp.rest-csrf.methods-to-ignore	GET,OPTIONS,HEAD	yarn
1624	2	yarn.resourcemanager.node-ip-cache.expiry-interval-secs	-1	yarn
1625	2	yarn.resourcemanager.webapp.spnego-keytab-file		yarn
1626	2	yarn.timeline-service.client.fd-clean-interval-secs	60	yarn
1627	2	yarn.client.nodemanager-connect.max-wait-ms	180000	yarn
1628	2	yarn.resourcemanager.zk-state-store.parent-path	/rmstore	yarn
1629	2	yarn.nodemanager.container-diagnostics-maximum-size	10000	yarn
1630	2	yarn.resourcemanager.nm-container-queuing.min-queue-length	5	yarn
1631	2	yarn.nodemanager.linux-container-executor.cgroups.strict-resource-usage	false	yarn
1632	2	yarn.client.failover-retries	0	yarn
1633	2	yarn.scheduler.configuration.leveldb-store.compaction-interval-secs	86400	yarn
1634	2	yarn.resourcemanager.configuration.file-system-based-store	/yarn/conf	yarn
1635	2	yarn.nodemanager.localizer.cache.target-size-mb	10240	yarn
1636	2	yarn.resourcemanager.admin.client.thread-count	1	yarn
1637	2	yarn.nodemanager.log-aggregation.policy.class	org.apache.hadoop.yarn.server.nodemanager.containermanager.logaggregation.AllContainerLogAggregationPolicy	yarn
1638	2	yarn.nodemanager.webapp.spnego-principal		yarn
1639	2	yarn.timeline-service.store-class	org.apache.hadoop.yarn.server.timeline.LeveldbTimelineStore	yarn
1640	2	yarn.resourcemanager.nm-container-queuing.queue-limit-stdev	1.0f	yarn
1641	2	yarn.resourcemanager.zk-appid-node.split-index	0	yarn
1642	2	yarn.resourcemanager.reservation-system.planfollower.time-step	1000	yarn
1643	2	yarn.resourcemanager.ha.automatic-failover.embedded	true	yarn
1644	2	yarn.node-labels.configuration-type	centralized	yarn
1645	2	yarn.nodemanager.log-container-debug-info.enabled	false	yarn
1646	2	yarn.timeline-service.ttl-ms	604800000	yarn
1647	2	yarn.resourcemanager.nm-container-queuing.min-queue-wait-time-ms	10	yarn
1648	2	yarn.resourcemanager.nodemanagers.heartbeat-interval-ms	1000	yarn
1649	2	yarn.nodemanager.linux-container-executor.cgroups.delete-timeout-ms	1000	yarn
1650	2	yarn.timeline-service.recovery.enabled	false	yarn
1651	2	yarn.nodemanager.recovery.dir	${hadoop.tmp.dir}/yarn-nm-recovery	yarn
1652	2	yarn.resourcemanager.keytab	/etc/krb5.keytab	yarn
1653	2	yarn.nodemanager.linux-container-executor.cgroups.delete-delay-ms	20	yarn
1654	2	yarn.webapp.ui2.enable	false	yarn
1655	2	yarn.cluster.max-application-priority	0	yarn
1656	2	yarn.log-aggregation-status.time-out.ms	600000	yarn
1657	2	yarn.federation.state-store.class	org.apache.hadoop.yarn.server.federation.store.impl.MemoryFederationStateStore	yarn
1658	2	yarn.client.max-cached-nodemanagers-proxies	0	yarn
1659	2	yarn.sharedcache.app-checker.class	org.apache.hadoop.yarn.server.sharedcachemanager.RemoteAppChecker	yarn
1660	2	yarn.nm.liveness-monitor.expiry-interval-ms	600000	yarn
1661	2	yarn.nodemanager.docker-container-executor.exec-name	/usr/bin/docker	yarn
1662	2	yarn.resourcemanager.fs.state-store.retry-interval-ms	1000	yarn
1663	2	yarn.nodemanager.local-dirs	${hadoop.tmp.dir}/nm-local-dir	yarn
1664	2	yarn.scheduler.configuration.store.class	file	yarn
1665	2	yarn.nodemanager.recovery.enabled	false	yarn
1666	2	yarn.sharedcache.store.in-memory.staleness-period-mins	10080	yarn
1667	2	yarn.resourcemanager.am.max-attempts	2	yarn
1668	2	yarn.timeline-service.client.internal-timers-ttl-secs	420	yarn
1669	2	yarn.nodemanager.resource.pcores-vcores-multiplier	1	yarn
1670	2	yarn.node-labels.fs-store.root-dir		yarn
1671	2	yarn.nodemanager.webapp.address	${yarn.nodemanager.hostname}:8042	yarn
1672	2	yarn.app.attempt.diagnostics.limit.kc	64	yarn
1674	2	yarn.ipc.client.factory.class		yarn
1675	2	yarn.nodemanager.disk-health-checker.max-disk-utilization-per-disk-percentage	90	yarn
1676	2	yarn.nodemanager.container-monitor.procfs-tree.smaps-based-rss.enabled	false	yarn
1677	2	yarn.timeline-service.webapp.rest-csrf.enabled	false	yarn
1678	2	yarn.nodemanager.runtime.linux.docker.privileged-containers.acl		yarn
1679	2	yarn.router.pipeline.cache-max-size	25	yarn
1680	2	yarn.timeline-service.reader.class	org.apache.hadoop.yarn.server.timelineservice.storage.HBaseTimelineReaderImpl	yarn
1681	2	yarn.log-aggregation.file-controller.TFile.class	org.apache.hadoop.yarn.logaggregation.filecontroller.tfile.LogAggregationTFileController	yarn
1682	2	yarn.timeline-service.writer.class	org.apache.hadoop.yarn.server.timelineservice.storage.HBaseTimelineWriterImpl	yarn
1683	2	yarn.client.nodemanager-client-async.thread-pool-max-size	500	yarn
1684	2	yarn.minicluster.yarn.nodemanager.resource.memory-mb	4096	yarn
1685	2	yarn.timeline-service.entity-group-fs-store.summary-store	org.apache.hadoop.yarn.server.timeline.LeveldbTimelineStore	yarn
1686	2	yarn.tracking.url.generator		yarn
1687	2	yarn.nodemanager.health-checker.interval-ms	600000	yarn
1688	2	yarn.timeline-service.keytab	/etc/krb5.keytab	yarn
1689	2	yarn.sharedcache.store.in-memory.initial-delay-mins	10	yarn
1690	2	yarn.router.rmadmin.interceptor-class.pipeline	org.apache.hadoop.yarn.server.router.rmadmin.DefaultRMAdminRequestInterceptor	yarn
1691	2	yarn.nodemanager.container-state-transition-listener.classes		yarn
1692	2	yarn.sharedcache.webapp.address	0.0.0.0:8788	yarn
1693	2	yarn.nodemanager.log-aggregation.compression-type	none	yarn
1694	2	yarn.resourcemanager.rm.container-allocation.expiry-interval-ms	600000	yarn
1695	2	yarn.resourcemanager.work-preserving-recovery.scheduling-wait-ms	10000	yarn
1696	2	yarn.nodemanager.log-dirs	${yarn.log.dir}/userlogs	yarn
1697	2	yarn.nodemanager.container-retry-minimum-interval-ms	1000	yarn
1698	2	yarn.nodemanager.container-monitor.interval-ms		yarn
1699	2	yarn.nodemanager.recovery.supervised	false	yarn
1700	2	yarn.nodemanager.amrmproxy.interceptor-class.pipeline	org.apache.hadoop.yarn.server.nodemanager.amrmproxy.DefaultRequestInterceptor	yarn
1701	2	yarn.nodemanager.node-labels.provider		yarn
1702	2	yarn.nodemanager.address	${yarn.nodemanager.hostname}:0	yarn
1703	2	yarn.resourcemanager.nodemanager-graceful-decommission-timeout-secs	3600	yarn
1704	2	yarn.scheduler.maximum-allocation-vcores	4	yarn
1705	2	yarn.nodemanager.sleep-delay-before-sigkill.ms	250	yarn
1706	2	yarn.scheduler.queue-placement-rules	user-group	yarn
1707	2	 yarn.router.webapp.https.address	0.0.0.0:8091	yarn
1708	2	yarn.resourcemanager.configuration.provider-class	org.apache.hadoop.yarn.LocalConfigurationProvider	yarn
1709	2	yarn.timeline-service.address	${yarn.timeline-service.hostname}:10200	yarn
1710	2	yarn.sharedcache.enabled	false	yarn
1711	2	yarn.resourcemanager.cluster-id		yarn
1712	2	yarn.timeline-service.http-cross-origin.enabled	false	yarn
1713	2	yarn.resourcemanager.decommissioning-nodes-watcher.poll-interval-secs	20	yarn
1714	2	yarn.nodemanager.recovery.compaction-interval-secs	3600	yarn
1715	2	yarn.http.policy	HTTP_ONLY	yarn
1716	2	yarn.nodemanager.opportunistic-containers-max-queue-length	0	yarn
1717	2	yarn.resourcemanager.reservation-system.enable	false	yarn
1718	2	yarn.nodemanager.webapp.rest-csrf.custom-header	X-XSRF-Header	yarn
1719	2	yarn.node-labels.fs-store.impl.class	org.apache.hadoop.yarn.nodelabels.FileSystemNodeLabelsStore	yarn
1720	2	yarn.nodemanager.container.stderr.pattern	{*stderr*,*STDERR*}	yarn
1721	2	yarn.router.bind-host		yarn
1722	2	yarn.timeline-service.http-authentication.type	simple	yarn
1723	2	yarn.dispatcher.drain-events.timeout	300000	yarn
1724	2	yarn.log-aggregation.retain-seconds	-1	yarn
1725	2	yarn.resourcemanager.fail-fast	${yarn.fail-fast}	yarn
1726	2	yarn.scheduler.minimum-allocation-vcores	1	yarn
1727	2	yarn.nodemanager.runtime.linux.docker.privileged-containers.allowed	false	yarn
1728	2	yarn.resourcemanager.node-labels.provider.fetch-interval-ms	1800000	yarn
1729	2	yarn.nodemanager.container-metrics.enable	true	yarn
1730	2	yarn.timeline-service.client.max-retries	30	yarn
1731	2	yarn.timeline-service.client.retry-interval-ms	1000	yarn
1732	2	yarn.webapp.ui2.war-file-path		yarn
1734	2	yarn.timeline-service.bind-host		yarn
1735	2	yarn.nodemanager.container-metrics.unregister-delay-ms	10000	yarn
1736	2	yarn.nodemanager.container-metrics.period-ms	-1	yarn
1737	2	yarn.resourcemanager.fs.state-store.uri	${hadoop.tmp.dir}/yarn/system/rmstore	yarn
1738	2	yarn.timeline-service.client.drain-entities.timeout.ms	2000	yarn
1739	2	yarn.nodemanager.health-checker.script.opts		yarn
1740	2	yarn.nodemanager.resourcemanager.connect.retry-interval.ms		yarn
1741	2	yarn.timeline-service.client.fd-flush-interval-secs	10	yarn
1742	2	yarn.resourcemanager.webapp.rest-csrf.methods-to-ignore	GET,OPTIONS,HEAD	yarn
1743	2	yarn.nodemanager.health-checker.script.path		yarn
1744	2	yarn.nodemanager.resourcemanager.minimum.version	NONE	yarn
1745	2	yarn.log.server.url		yarn
1746	2	yarn.resourcemanager.address	${yarn.resourcemanager.hostname}:8032	yarn
1747	2	yarn.resourcemanager.scheduler.monitor.enable	false	yarn
1748	2	yarn.resourcemanager.nodemanager-connect-retries	10	yarn
1749	2	yarn.sharedcache.nm.uploader.thread-count	20	yarn
1750	2	yarn.nodemanager.logaggregation.threadpool-size-max	100	yarn
1751	2	yarn.nodemanager.collector-service.address	${yarn.nodemanager.hostname}:8048	yarn
1752	2	yarn.sharedcache.client-server.address	0.0.0.0:8045	yarn
1753	2	yarn.scheduler.configuration.store.max-logs	1000	yarn
1754	2	yarn.client.nodemanager-connect.retry-interval-ms	10000	yarn
1755	2	yarn.timeline-service.version	1.0f	yarn
1756	2	yarn.timeline-service.webapp.rest-csrf.custom-header	X-XSRF-Header	yarn
1757	2	yarn.am.liveness-monitor.expiry-interval-ms	600000	yarn
1758	2	yarn.nodemanager.linux-container-executor.resources-handler.class	org.apache.hadoop.yarn.server.nodemanager.util.DefaultLCEResourcesHandler	yarn
1759	2	yarn.timeline-service.leveldb-timeline-store.read-cache-size	104857600	yarn
1760	2	yarn.timeline-service.app-collector.linger-period.ms	1000	yarn
1761	2	yarn.timeline-service.leveldb-timeline-store.path	${hadoop.tmp.dir}/yarn/timeline	yarn
1762	2	yarn.federation.machine-list		yarn
1763	2	yarn.resourcemanager.delegation.token.max-lifetime	604800000	yarn
1764	2	yarn.resourcemanager.ha.automatic-failover.enabled	true	yarn
1765	2	yarn.nodemanager.amrmproxy.client.thread-count	25	yarn
1766	2	yarn.federation.cache-ttl.secs	300	yarn
1767	2	yarn.nodemanager.log-aggregation.policy.parameters		yarn
1768	2	yarn.resourcemanager.work-preserving-recovery.enabled	true	yarn
1769	2	yarn.timeline-service.principal		yarn
1770	2	yarn.resourcemanager.store.class	org.apache.hadoop.yarn.server.resourcemanager.recovery.FileSystemRMStateStore	yarn
1771	2	yarn.nodemanager.webapp.rest-csrf.enabled	false	yarn
1772	2	yarn.timeline-service.leveldb-state-store.path	${hadoop.tmp.dir}/yarn/timeline	yarn
1773	2	yarn.resourcemanager.webapp.ui-actions.enabled	true	yarn
1774	2	yarn.scheduler.configuration.zk-store.parent-path	/confstore	yarn
1775	2	yarn.rm.system-metrics-publisher.emit-container-events	false	yarn
1776	2	yarn.resourcemanager.ha.rm-ids		yarn
1777	2	yarn.resourcemanager.nodes.exclude-path		yarn
1778	2	yarn.nodemanager.container-executor.class	org.apache.hadoop.yarn.server.nodemanager.DefaultContainerExecutor	yarn
1779	2	yarn.timeline-service.writer.flush-interval-seconds	60	yarn
1780	2	yarn.resourcemanager.scheduler.client.thread-count	50	yarn
1781	2	yarn.resourcemanager.auto-update.containers	false	yarn
1782	2	yarn.scheduler.configuration.leveldb-store.path	${hadoop.tmp.dir}/yarn/system/confstore	yarn
1783	2	yarn.nodemanager.amrmproxy.address	0.0.0.0:8049	yarn
1784	2	yarn.resourcemanager.webapp.rest-csrf.enabled	false	yarn
1785	2	yarn.webapp.xfs-filter.enabled	true	yarn
1786	2	yarn.resourcemanager.zk-delegation-token-node.split-index	0	yarn
1787	2	yarn.resourcemanager.nodes.include-path		yarn
1788	2	yarn.nodemanager.collector-service.thread-count	5	yarn
1789	2	yarn.nodemanager.runtime.linux.docker.capabilities	CHOWN,DAC_OVERRIDE,FSETID,FOWNER,MKNOD,NET_RAW,SETGID,SETUID,SETFCAP,SETPCAP,NET_BIND_SERVICE,SYS_CHROOT,KILL,AUDIT_WRITE	yarn
1790	2	yarn.nodemanager.distributed-scheduling.enabled	false	yarn
1791	2	yarn.minicluster.fixed.ports	false	yarn
1792	2	yarn.nodemanager.pmem-check-enabled	true	yarn
1793	2	yarn.nodemanager.remote-app-log-dir	/tmp/logs	yarn
1794	2	yarn.timeline-service.entity-group-fs-store.scan-interval-seconds	60	yarn
1795	2	yarn.nodemanager.disk-health-checker.disk-utilization-watermark-low-per-disk-percentage		yarn
1796	2	yarn.timeline-service.webapp.https.address	${yarn.timeline-service.hostname}:8190	yarn
1797	2	yarn.nodemanager.resource.percentage-physical-cpu-limit	100	yarn
1798	2	yarn.resourcemanager.amlauncher.thread-count	50	yarn
1799	2	yarn.timeline-service.timeline-client.number-of-async-entities-to-merge	10	yarn
1800	2	yarn.sharedcache.nm.uploader.replication.factor	10	yarn
1801	2	yarn.client.failover-proxy-provider	org.apache.hadoop.yarn.client.ConfiguredRMFailoverProxyProvider	yarn
1802	2	yarn.resourcemanager.ha.id		yarn
1803	2	yarn.timeline-service.client.fd-retain-secs	300	yarn
1804	2	yarn.nodemanager.resource-calculator.class		yarn
1805	2	yarn.nodemanager.amrmproxy.enabled	false	yarn
1806	2	yarn.resourcemanager.display.per-user-apps	false	yarn
1807	2	yarn.nodemanager.remote-app-log-dir-suffix	logs	yarn
1808	2	yarn.resourcemanager.node-removal-untracked.timeout-ms	60000	yarn
1809	2	yarn.resourcemanager.webapp.address	${yarn.resourcemanager.hostname}:8088	yarn
1810	2	yarn.sharedcache.store.in-memory.check-period-mins	720	yarn
1811	2	yarn.nodemanager.windows-secure-container-executor.group		yarn
1812	2	yarn.timeline-service.enabled	false	yarn
1813	2	yarn.router.webapp.address	0.0.0.0:8089	yarn
1814	2	yarn.nodemanager.hostname	0.0.0.0	yarn
1815	2	yarn.resourcemanager.nm-container-queuing.max-queue-length	15	yarn
1816	2	yarn.nodemanager.localizer.client.thread-count	5	yarn
1817	2	yarn.web-proxy.keytab		yarn
1818	2	yarn.sharedcache.uploader.server.thread-count	50	yarn
1819	2	yarn.resourcemanager.webapp.rest-csrf.custom-header	X-XSRF-Header	yarn
1820	2	yarn.resourcemanager.nm-container-queuing.max-queue-wait-time-ms	100	yarn
1821	2	security.applicationhistory.protocol.acl		yarn
1822	2	yarn.timeline-service.http-authentication.simple.anonymous.allowed	true	yarn
1823	2	yarn.nodemanager.runtime.linux.docker.allowed-container-networks	host,none,bridge	yarn
1824	2	yarn.sharedcache.client-server.thread-count	50	yarn
1825	2	yarn.resourcemanager.resource-tracker.address	${yarn.resourcemanager.hostname}:8031	yarn
1826	2	yarn.acl.reservation-enable	false	yarn
1827	2	yarn.federation.subcluster-resolver.class	org.apache.hadoop.yarn.server.federation.resolver.DefaultSubClusterResolverImpl	yarn
1828	2	yarn.client.failover-sleep-base-ms		yarn
1829	2	yarn.nodemanager.resource.memory-mb	-1	yarn
1830	2	yarn.nodemanager.disk-health-checker.min-healthy-disks	0.25	yarn
1831	2	yarn.node-labels.enabled	false	yarn
1832	2	yarn.timeline-service.handler-thread-count	10	yarn
1833	2	yarn.resourcemanager.connect.max-wait.ms	900000	yarn
1834	2	yarn.nodemanager.resource.detect-hardware-capabilities	false	yarn
1835	2	yarn.resourcemanager.history-writer.multi-threaded-dispatcher.pool-size	10	yarn
1836	2	yarn.router.clientrm.interceptor-class.pipeline	org.apache.hadoop.yarn.server.router.clientrm.DefaultClientRequestInterceptor	yarn
1837	2	yarn.resourcemanager.node-labels.provider		yarn
1838	2	yarn.resourcemanager.scheduler.class	org.apache.hadoop.yarn.server.resourcemanager.scheduler.capacity.CapacityScheduler	yarn
1839	2	yarn.resourcemanager.system-metrics-publisher.enabled	false	yarn
1840	2	yarn.is.minicluster	false	yarn
1841	2	yarn.sharedcache.nested-level	3	yarn
1842	2	yarn.nodemanager.disk-validator	basic	yarn
1843	2	yarn.resourcemanager.delayed.delegation-token.removal-interval-ms	30000	yarn
1844	2	yarn.nodemanager.localizer.fetch.thread-count	4	yarn
1845	2	yarn.resourcemanager.scheduler.address	${yarn.resourcemanager.hostname}:8030	yarn
1846	2	yarn.nodemanager.webapp.cross-origin.enabled	false	yarn
1847	2	yarn.nodemanager.opportunistic-containers-use-pause-for-preemption	false	yarn
1848	2	yarn.minicluster.control-resource-monitoring	false	yarn
1849	2	yarn.client.failover-sleep-max-ms		yarn
1850	2	yarn.timeline-service.leveldb-timeline-store.start-time-write-cache-size	10000	yarn
1851	2	yarn.nodemanager.health-checker.script.timeout-ms	1200000	yarn
1852	2	yarn.resourcemanager.fs.state-store.num-retries	0	yarn
1853	2	yarn.timeline-service.entity-group-fs-store.group-id-plugin-classes		yarn
1854	2	yarn.resourcemanager.ha.automatic-failover.zk-base-path	/yarn-leader-election	yarn
1855	2	yarn.resourcemanager.delegation-token.max-conf-size-bytes	12800	yarn
1856	2	yarn.intermediate-data-encryption.enable	false	yarn
1857	2	yarn.resourcemanager.opportunistic-container-allocation.nodes-used	10	yarn
1858	2	yarn.resourcemanager.system-metrics-publisher.dispatcher.pool-size	10	yarn
1859	2	yarn.nodemanager.principal		yarn
1860	2	yarn.resourcemanager.ha.enabled	false	yarn
1861	2	yarn.system-metrics-publisher.enabled	false	yarn
1862	2	yarn.timeline-service.entity-group-fs-store.app-cache-size	10	yarn
1863	2	yarn.timeline-service.hbase.configuration.file		yarn
1864	2	yarn.resourcemanager.metrics.runtime.buckets	60,300,1440	yarn
1865	2	yarn.client.application-client-protocol.poll-timeout-ms	-1	yarn
1866	2	yarn.scheduler.include-port-in-node-name	false	yarn
1867	2	yarn.resourcemanager.state-store.max-completed-applications	${yarn.resourcemanager.max-completed-applications}	yarn
1868	2	yarn.nodemanager.aux-services.mapreduce_shuffle.class	org.apache.hadoop.mapred.ShuffleHandler	yarn
1869	2	yarn.nodemanager.docker-container-executor.image-name		yarn
1870	2	yarn.sharedcache.uploader.server.address	0.0.0.0:8046	yarn
1871	2	yarn.resourcemanager.zk-max-znode-size.bytes	1048576	yarn
1872	2	yarn.timeline-service.hbase-schema.prefix	prod.	yarn
1873	2	yarn.nodemanager.log-aggregation.roll-monitoring-interval-seconds	-1	yarn
1874	2	yarn.timeline-service.state-store-class	org.apache.hadoop.yarn.server.timeline.recovery.LeveldbTimelineStateStore	yarn
1875	2	yarn.resourcemanager.opportunistic-container-allocation.enabled	false	yarn
1876	2	yarn.resourcemanager.webapp.xfs-filter.xframe-options	SAMEORIGIN	yarn
1877	2	yarn.timeline-service.generic-application-history.max-applications	10000	yarn
1878	2	yarn.resourcemanager.hostname	0.0.0.0	yarn
1879	2	yarn.resourcemanager.principal		yarn
1880	2	yarn.nodemanager.disk-health-checker.min-free-space-per-disk-mb	0	yarn
1881	2	yarn.client.failover-retries-on-socket-timeouts	0	yarn
1882	2	yarn.resourcemanager.ha.failover-controller.active-standby-elector.zk.retries		yarn
1883	2	yarn.sharedcache.store.class	org.apache.hadoop.yarn.server.sharedcachemanager.store.InMemorySCMStore	yarn
1884	2	yarn.resourcemanager.webapp.https.address	${yarn.resourcemanager.hostname}:8090	yarn
1885	2	yarn.resourcemanager.max-log-aggregation-diagnostics-in-memory	10	yarn
1886	2	yarn.nodemanager.linux-container-executor.path		yarn
1887	2	yarn.nodemanager.windows-container.cpu-limit.enabled	false	yarn
1888	2	yarn.client.failover-max-attempts		yarn
1889	2	yarn.nodemanager.container-monitor.process-tree.class		yarn
1890	2	yarn.nodemanager.vmem-pmem-ratio	2.1	yarn
1891	2	yarn.web-proxy.principal		yarn
1892	2	yarn.nodemanager.node-labels.provider.fetch-timeout-ms	1200000	yarn
1893	2	yarn.authorization-provider		yarn
\.

