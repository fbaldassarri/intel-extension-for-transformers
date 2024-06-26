<!--
  Copyright (c) 2024 Intel Corporation
 
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
 
     http://www.apache.org/licenses/LICENSE-2.0
 
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->

<script lang="ts">
	import VoiceButton from "./imgs/voice-button.svelte";
	import stopRecordingIcon from "$lib/assets/stop-recording.svg";
	import { afterUpdate, createEventDispatcher, onMount } from "svelte";
	import DeleteIcon from "./imgs/Delete.svelte";
	export let name: string;
	export let audio: string;
	export let notLibrary: boolean = false;
	export let needChangeName = false;

	const dispatch = createEventDispatcher();
	let inputEl: HTMLInputElement;

	onMount(() => {
		music = new Audio(audio);
		music.onended = () => {
			music.currentTime = 0;
			play = false;
			music.pause();
		};
		if (needChangeName) {
			changeName();
		}
	});

	afterUpdate(() => {
		if (inputEl) {
			inputEl.focus();
			inputEl.onblur = () => {
				needChangeName = false;
			};
		}
	});

	let play = false;
	let music: HTMLAudioElement;

	function handleAudioPlayer() {
		play = !play;
		if (play) {
			music.play();
		} else {
			music.pause();
		}
	}

	function changeName() {
		needChangeName = true;
	}
</script>

<div
	class="relative flex h-32 w-32 flex-col items-center rounded-xl pt-4 shadow-[0_2px_30px_0_rgba(0,0,0,0.1)]"
>
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	<div
		class="flex items-center justify-center"
		on:click|stopPropagation={() => {
			handleAudioPlayer();
		}}
	>
		{#if play}
			<img class="my-1 h-11 w-11" src={stopRecordingIcon} alt="" />
		{:else}
			<VoiceButton />
		{/if}
	</div>
	<!-- svelte-ignore a11y-click-events-have-key-events -->
	{#if notLibrary}
		<DeleteIcon on:DeleteAvatar={() => dispatch("delete")} />
	{/if}
	<span
		class="relative mt-2 w-9/12 overflow-hidden text-ellipsis whitespace-nowrap text-sm text-gray-600"
	>
		{name}
	</span>
</div>
