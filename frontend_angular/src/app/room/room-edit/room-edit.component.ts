import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {ActivatedRoute, ParamMap, Router} from '@angular/router';


import {Room, RoomService, VlanService} from '../../api';
import {finalize, first, switchMap, tap} from 'rxjs/operators';
import { Observable } from 'rxjs';
import { AppConstantsService } from '../../app-constants.service';

@Component({
  selector: 'app-room-edit',
  templateUrl: './room-edit.component.html',
  styleUrls: ['./room-edit.component.css']
})

export class RoomEditComponent implements OnInit {
  public disabled = false;
  public roomEdit: FormGroup;
  public room$: Observable<Room>;

  constructor(
    private roomService: RoomService,
    private vlanService: VlanService,
    private fb: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private appConstantService: AppConstantsService,
  ) {
    this.createForm();
  }

  createForm() {
    this.disabled = false;
    this.roomEdit = this.fb.group({
      id: ['', [Validators.required]],
      roomNumber: ['', [Validators.min(0), Validators.max(9999), Validators.required]],
      vlan: ['', [Validators.min(41), Validators.max(49), Validators.required]],
      description: ['', Validators.required],
    });
  }

  onSubmit() {
    const v = this.roomEdit.value;
    this.vlanService.getFromNumber(v.vlan)
      .pipe(
        first(() => this.disabled = true),
        finalize(() => this.disabled = false)
      )
      .subscribe(vlan => {
        const room: Room = {
          roomNumber: v.roomNumber,
          vlan: vlan.id,
          description: v.description
        };
        this.roomService.roomRoomIdPut(room, v.id)
          .subscribe(() => {
            this.router.navigate(['/room/view', v.roomNumber]);
            this.appConstantService.Toast.fire({
              title: 'Success',
            });
          });
      });
  }

  ngOnInit() {
    this.room$ = this.route.paramMap
      .pipe(
        switchMap((params: ParamMap) => this.roomService.roomRoomIdGet(+params.get('room_id'))),
        tap(room => this.roomEdit.patchValue({
          id: room.id,
          roomNumber: room.roomNumber,
          description: room.description,
          vlan: (typeof(room.vlan) === 'number') ? room.vlan : room.vlan.number
        }))
      );
  }
}
